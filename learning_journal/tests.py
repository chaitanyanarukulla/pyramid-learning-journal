""""."""
from pyramid.httpexceptions import HTTPNotFound
from learning_journal.models import Entry
from learning_journal.models.meta import Base
from pyramid import testing
from faker import Faker
from learning_journal.models import (get_tm_session)
import pytest
import transaction


"""Test learning journal."""


def test_list_view_returns__dict(dummy_request):
    """Test if list view returns dictionary."""
    from learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert isinstance(response, dict)


def test_list_view_contains_new_data_added(dummy_request, new_entry):
    """Test if data sent through the request is added to the db."""
    from learning_journal.views.default import list_view
    dummy_request.dbsession.add(new_entry)
    dummy_request.dbsession.commit()
    response = list_view(dummy_request)
    assert new_entry.to_dict() in response['entry']


def test_detail_view_raises_not_found_if_id_not_found(dummy_request):
    """Test if detail raises HTTPNotFound if id not in dict."""
    from learning_journal.views.default import detail_view
    dummy_request.matchdict['id'] = 10000
    with pytest.raises(HTTPNotFound):
        detail_view(dummy_request)


def test_create_view_returns_dict(dummy_request):
    """Test if create view returns a dictionary."""
    from learning_journal.views.default import create_view
    response = create_view(dummy_request)
    assert isinstance(response, dict)


def test_create_view_returns_empty_dict(dummy_request):
    """Test if create view returns a dictionary."""
    from learning_journal.views.default import create_view
    response = create_view(dummy_request)
    assert len(response) == 0


@pytest.fixture(scope='session')
def configuration(request):
    """Set up a Configurator instance."""
    config = testing.setUp(settings={
        'sqlalchemy.url': 'postgres://localhost:5432/test_learning_journal'
    })
    config.include("learning_journal.models")
    config.include("learning_journal.routes")

    def teardown():
        testing.tearDown()

    request.addfinalizer(teardown)
    return config


@pytest.fixture()
def db_session(configuration, request):
    """Create a session for testing the database."""
    SessionFactory = configuration.registry["dbsession_factory"]
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(engine)

    def teardown():
        session.transaction.rollback()

    request.addfinalizer(teardown)
    return session


@pytest.fixture()
def dummy_request(db_session):
    """Instantiate a fake HTTP Request, complete with a database session."""
    return testing.DummyRequest(dbsession=db_session)


def test_list_view_returns_a_dict(dummy_request):
    """Test if list view returns dictionary."""
    from learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert isinstance(response, dict)


def test_detail_view_returns_dict(dummy_request):
    """Test if detail view returns dictionary."""
    from learning_journal.views.default import detail_view
    new_detail = Entry(
        title='Something Awesomer',
        creation_date='November 11, 1982',
        body='All the cool things I write.'
    )
    dummy_request.dbsession.add(new_detail)
    dummy_request.dbsession.commit()
    dummy_request.matchdict['id'] = 2
    response = detail_view(dummy_request)
    assert isinstance(response, dict)


def test_detail_view_returns_sinlgle_item(dummy_request):
    """Test if detail view returns dictionary with contents of 'title'."""
    from learning_journal.views.default import detail_view
    new_detail = Entry(
        title='Something Awesomers',
        creation_date='November 1, 2000',
        body='All the cool things I write.'
    )
    dummy_request.dbsession.add(new_detail)
    dummy_request.dbsession.commit()
    dummy_request.matchdict['id'] = 3
    response = detail_view(dummy_request)
    assert response['entry']['title'] == 'Something Awesomers'


def test_update_view_returns_dict(dummy_request):
    """Test if update view returns a dictionary."""
    from learning_journal.views.default import update_view
    new_detail = Entry(
        title='Something Awesomers',
        creation_date='January 1, 0001',
        body='All the cool things I write.'
    )
    dummy_request.dbsession.add(new_detail)
    dummy_request.dbsession.commit()
    dummy_request.matchdict['id'] = 3
    response = update_view(dummy_request)
    assert isinstance(response, dict)


@pytest.fixture(scope="session")
def testapp(request):
    """Setup session to test front end of app."""
    from webtest import TestApp
    from pyramid.config import Configurator

    def main():
        config = Configurator()
        settings = {
            'sqlalchemy.url': 'postgres://localhost:5432/test_learning_journal'
        }
        config = Configurator(settings=settings)
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.include('.models')
        config.include('.security')
        config.scan()
        return config.make_wsgi_app()

    app = main()

    SessionFactory = app.registry["dbsession_factory"]
    engine = SessionFactory().bind
    Base.metadata.create_all(bind=engine)

    def tearDown():
        Base.metadata.drop_all(bind=engine)

    request.addfinalizer(tearDown)

    return TestApp(app)


@pytest.fixture(scope="session")
def fill_the_db(testapp):
    """Fill the db with dummy data."""
    SessionFactory = testapp.app.registry["dbsession_factory"]
    with transaction.manager:
        dbsession = get_tm_session(SessionFactory, transaction.manager)
        dbsession.add_all(BLOGS)


BLOGS = []


FAKE = Faker()


for i in range(20):
    new_entry = Entry(
        title='journal{}'.format(i),
        creation_date=FAKE.date_time(),
        body='A new entry. {}'.format(FAKE.sentence())
    )
    BLOGS.append(new_entry)


def test_home_route_has_titles(testapp, fill_the_db):
    """Test if home route has all titles from db."""
    assert len(BLOGS) == 20


def test_detail_route_with_has_titles(testapp):
    """Test if detail route shows title expected."""
    response = testapp.get("/journal/5")
    assert 'journal' in response.ubody


def test_detail_route_includes_body(testapp):
    """Test if detail route shows title expected."""
    response = testapp.get("/journal/5")
    assert '<body>' in response.ubody


def test_create_route_no_login_is_403(testapp):
    """Test if detail route shows title expected."""
    assert testapp.get("/journal/new-entry", status=403)


def test_edit_route_no_login_is_403(testapp):
    """Test if edit route shows title expected."""
    assert testapp.get("/journal/5/edit-entry", status=403)


def test_create_view_successful_post_redirects_home(testapp):
    """Test create view redirects to home page after submission."""
    testapp.post('/login', {
        'username': 'chai',
        'password': 'password',
    })
    csrf = testapp.get('/journal/new-entry').html.\
        find('input', {'type': 'hidden'})['value']
    new_entry = {
        "csrf_token": csrf,
        "title": "Day 1",
        "date": 'January 1, 2017',
        "body": 'test test test.'
    }
    response = testapp.post("/journal/new-entry", new_entry)
    assert response.location == 'http://localhost/'


def test_update_view_successfully_updates_title_on_home_page(testapp):
    """Test update view changes title on home page reroute."""
    csrf = testapp.get('/journal/20/edit-entry').html.\
        find('input', {'type': 'hidden'})['value']
    edit_entry = {
        "csrf_token": csrf,
        "title": "Journal Me, edit",
        "date": 'January 1, 0002',
        "body": 'test test test test.'
    }
    response = testapp.post("/journal/20/edit-entry", edit_entry)
    next_page = response.follow()
    assert "Journal Me, edit" in next_page.ubody


def test_login_view_with_correct_login_routes_home(testapp):
    """Test login view routes home with successful login."""
    login = {
        'username': 'chai',
        'password': 'password'
    }
    response = testapp.post("/login", login)
    assert response.status_int == 302


def test_login_view_with_incorrect_login_routes_home(testapp):
    """Test login view routes home with successful login."""
    login = {
        'username': 'chai',
        'password': 'passwordde'
    }
    response = testapp.post("/login", login)
    assert response.status_int == 200
