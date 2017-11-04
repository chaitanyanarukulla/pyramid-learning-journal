"""Tests for learning journal."""
from pyramid.testing import DummyRequest

import pytest


from learning_journal.views.default import (
    list_view,
    detail_view,
    create_view,
)


@pytest.fixture
def dummy_request():
    """Set up a dummy request for testing."""
    return DummyRequest()

"""some of the test code was used from this repos
https://github.com/codefellows/expense_tracker_401d7

https://github.com/markreynoso/pyramid-learning-journal"""

def test_list_view_returns_list_of_entries_in_dict(dummy_request):
    """Test if entries dict is in list view."""
    from learning_journal.views.default import list_view
    req = dummy_request


def test_list_view_test_status_code_200():
    """Testing status code 200 for list view."""
    from .views import list_view
    req = dummy_request()
    response = list_view(req)
    assert 'entries' in response


@pytest.fixture
def testapp():
    """Test app fixture."""
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


def test_the_detail_route_has_title(testapp):
    """Test detail has a title in the response."""
    response = testapp.get('/journal/1')
    assert 'title' in response


def test_the_entry_1_body_has_entry_text(testapp):
    """Test detail page has specific text in body."""
    response = testapp.get('/journal/1')
    assert b'with virtual environment' in response.body


def test_the_entry_2_body_has_entry_text(testapp):
    """Test detail page has specific text in body."""
    response = testapp.get('/journal/2')
    assert b'Python Dictionaries and its methods' in response.body


def test_detail_view_test_status_code_200():
    """Testing status code 200 for detail view."""
    from .views import detail_view
    req = dummy_request()
    response = detail_view(req)
    assert response.status_code == 200


def test_create_view_test_status_code_200():
    """Testing status code 200 for create view."""
    from .views import create_view
    req = dummy_request()
    response = create_view(req)
    assert response.status_code == 200


def test_update_view_test_status_code_200():
    """Testing status code 200 for update view."""
    from .views import update_view
    req = dummy_request()
    response = update_view(req)
    assert response.status_code == 200


def test_list_view_response_text_has_proper_content_type(dummy_request):
    """Test that list view returns expected content."""
    response = list_view(dummy_request)
    assert response.content_type == 'text/html'


def test_detail_view_response_text_has_proper_content_type(dummy_request):
    """Test that list view returns expected content type."""
    response = detail_view(dummy_request)
    assert response.content_type == 'text/html'


def test_create_view_response_text_has_proper_content_type(dummy_request):
    """Test that list view returns expected content."""
    response = create_view(dummy_request)
    assert response.content_type == 'text/html'


def test_create_view_response_text_has_proper_content(dummy_request):
    """Test that list view returns expected content."""
    response = create_view(dummy_request)
    text = '<p>Create your Owne Blog</p>'
    assert text in response.ubody


def test_detail_view_response_text_has_proper_content(dummy_request):
    """Test that list view returns expected content."""
    response = detail_view(dummy_request)
    text = '<h1>Man must explore, and this is exploration at its greatest</h1>'
    assert text in response.ubody


def test_list_view_response_text_has_proper_content(dummy_request):
    """Test that list view returns expected content."""
    response = list_view(dummy_request)
    text = '<h1>Chaitany.Narukulla</h1>'
    assert text in response.ubody
