"""Testing routes and its response."""
from pyramid import testing
import pytest


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
