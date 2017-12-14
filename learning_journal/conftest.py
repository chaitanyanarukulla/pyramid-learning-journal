"""Test fixture."""
import pytest
from pyramid import testing
from learning_journal.models import Entry
from learning_journal.models.meta import Base


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
    """Create a session for interacting with the test database."""
    session_factory = configuration.registry["dbsession_factory"]
    session = session_factory()
    engine = session.bind
    Base.metadata.create_all(engine)

    def teardown():
        session.transaction.rollback()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return session


@pytest.fixture()
def dummy_request(db_session):
    """Instantiate a fake HTTP Request, complete with a database session."""
    return testing.DummyRequest(dbsession=db_session)


@pytest.fixture()
def new_entry(db_session):
    """."""
    new_entry = Entry(
        title='Day 1',
        creation_date='November 19, 1955',
        body='Bla Bla Bla Bla.'
    )
    db_session.add(new_entry)
    db_session.commit()
    return new_entry
