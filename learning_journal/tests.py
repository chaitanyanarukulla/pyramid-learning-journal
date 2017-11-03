"""Testing routes and its response."""
from pyramid import testing
import pytest


from learning_journal.views.default import (
    list_view,
    detail_view,
    create_view,
)


@pytest.fixture
def dummy_request():
    """Dummy request."""
    return testing.DummyRequest()


def test_list_view_test_status_code_200():
    """Testing status code 200 for list view."""
    from .views import list_view
    req = dummy_request()
    response = list_view(req)
    assert response.status_code == 200


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
    """Test that list view returns expected content."""
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
