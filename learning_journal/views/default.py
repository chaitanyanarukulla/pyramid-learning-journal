"""View functions to serve all the routes."""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from learning_journal.Data.entry import ENTRIES


HERE = os.path.dirname(__file__)


@view_config(route_name='home',
             renderer='learning_journal:templates/index.jinja2')
def list_view(request):
    """This_ serves home page."""
    return {
        "entries": ENTRIES,
        "title": "Chai\'s Blog",
    }


@view_config(route_name='detail',
             renderer='learning_journal:/templates/read.jinja2')
def detail_view(request):
    """This_ serves single blog entry page."""
    the_id = int(request.matchdict['id'])
    for entry in ENTRIES:
        if entry['id'] == the_id:
            title = "Chai\'s Blog - {}".format(entry["title"])
            return {
                "entry": entry,
                "title": title,
            }
    raise HTTPNotFound()


@view_config(route_name='create',
             renderer='learning_journal:templates/create.jinja2')
def create_view(request):
    """This_ serves create blog page."""
    return {"title": "Chai\'s Blog - New Post"}


@view_config(route_name='update',
             renderer='learning_journal:/templates/update.jinja2')
def update_view(request):
    """This_ serves update view."""
    the_id = int(request.matchdict['id'])
    for entry in ENTRIES:
        if entry['id'] == the_id:
            return {
                "entry": entry,
                "title": "Chai\'s Blog - Update Post",

            }
    raise HTTPNotFound()

