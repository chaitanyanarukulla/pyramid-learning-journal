"""Test default.py."""
from pyramid.testing import DummyRequest
from pyramid.httpexceptions import HTTPNotFound
import pytest


@pytest.fixture
def testapp():
    """Initialize test route for testing."""
    from webtest import TestApp
    from pyramid.config import Configurator

    def main():
        config = Configurator()
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.scan()
        return config.make_wsgi_app()

    app = main()
    return TestApp(app)


@pytest.fixture
def dummy_request():
    """Set up a dummy request for testing."""
    return DummyRequest()


def test_list_view_returns_dict():
    """Test if list view returns a dictionary."""
    from learning_journal.views.default import list_view
    req = DummyRequest()
    response = list_view(req)
    assert isinstance(response, dict)


def test_create_view_returns_dict():
    """Test if create view returns a dictionary."""
    from learning_journal.views.default import create_view
    req = DummyRequest()
    response = create_view(req)
    assert isinstance(response, dict)


def test_update_view_returns_dict():
    """Test if update view returns a dictionary."""
    from learning_journal.views.default import update_view
    req = DummyRequest()
    req.matchdict['id'] = 1
    response = update_view(req)
    assert isinstance(response, dict)


def test_update_view_raises_exception_id_not_found():
    """Test if update raises exception on non-existent id."""
    from learning_journal.views.default import update_view
    req = DummyRequest()
    req.matchdict['id'] = 20
    with pytest.raises(HTTPNotFound):
        update_view(req)


def test_detail_route_has_text_from_journal(testapp):
    """Test if detail route return text from served journal."""
    response = testapp.get("/journal/1")
    assert "environment and while doing my assignment" in str(response.html)


def test_create_route_has_text_from_journal(testapp):
    """Test if create route return text from served journal."""
    response = testapp.get("/journal/1")
    assert "environment and while doing my assignment" in str(response.html)


def test_update_route_has_text_from_journal(testapp):
    """Test if update route return text from served journal."""
    response = testapp.get("/journal/1")
    assert "environment and while doing my assignment" in str(response.html)


def test_all_entries_in_data_in_request(dummy_request):
    """Test request object has all journal entries."""
    from learning_journal.views.default import list_view
    from learning_journal.Data.entry import ENTRIES
    req = dummy_request
    response = list_view(req)
    assert response['entry'] == ENTRIES
