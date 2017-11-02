from pyramid.view import view_config
import os

HERE = os.path.abspath(__file__)
TEMPLATE = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'templates')


@view_config(route_name='home', renderer='templates/index.jinja2')
def list_view(request):
    return {}


@view_config(route_name='post', renderer='templates/read.jinja2')
def detail_view(request):
    return {}


@view_config(route_name='new-entry', renderer='templates/create.jinja2')
def create_view(request):
    return {}


@view_config(route_name='edit-entry', renderer='templates/edit.jinja2')
def update_view(request):
    return {}
