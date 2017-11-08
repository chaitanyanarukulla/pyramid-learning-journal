
"""Test learning journal."""
import pytest
from learning_journal.models import Entry
from pyramid.httpexceptions import HTTPNotFound
from learning_journal.models.meta import Base


def test_list_view_returns__dict(dummy_request):
    """Test if list view returns dictionary."""
    from learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert isinstance(response, dict)


def test_list_view_returns_empty_dict_with_no_data(dummy_request):
    """Test if list view returns dictionary with no data."""
    from learning_journal.views.default import list_view
    response = list_view(dummy_request)
    assert len(response['entry']) == 0


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
