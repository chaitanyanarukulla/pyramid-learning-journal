"""View functions to serve all the routes."""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound, HTTPBadRequest
from learning_journal.models.mymodel import Entry
from learning_journal.security import check_credentials
from pyramid.security import remember, forget


@view_config(route_name='home',
             renderer='learning_journal:templates/index.jinja2')
def list_view(request):
    """This_ serves home page."""
    entries = request.dbsession.query(Entry).order_by(Entry.creation_date.desc()).all()
    entries = [entry.to_dict() for entry in entries]
    return {
        "entry": entries,
        "title": "Chai\'s Blog",
    }


@view_config(route_name='detail',
             renderer='learning_journal:/templates/read.jinja2')
def detail_view(request):
    """This_ serves single blog entry page."""
    the_id = int(request.matchdict['id'])
    entry = request.dbsession.query(Entry).get(the_id)
    if entry:
        return {"entry": entry.to_dict()}
    raise HTTPNotFound


@view_config(route_name='create', permission='add',
             renderer='learning_journal:templates/create.jinja2')
def create_view(request):
    """Receive request and serves create page."""
    if request.method == "POST":
        if not all([field in request.POST for field in ['title', 'body']]):
            raise HTTPBadRequest
        new_blog = Entry(
            title=request.POST['title'],
            body=request.POST['body']
        )
        request.dbsession.add(new_blog)
        return HTTPFound(request.route_url('home'))
    return {}


@view_config(route_name='update', permission='add',
             renderer='learning_journal:templates/edit.jinja2')
def update_view(request):
    """Receive request and serves edit page."""
    the_id = int(request.matchdict['id'])
    journal = request.dbsession.query(Entry).get(the_id)
    if journal:
        if request.method == 'POST' and request.POST:
            journal.title = request.POST['title'],
            journal.body = request.POST['body']
            request.dbsession.flush()
            return HTTPFound(request.route_url('detail', id=journal.id))
        return {
            'Entry': journal.to_dict()
        }
    raise HTTPNotFound


@view_config(route_name="login",
             renderer="learning_journal:templates/login.jinja2",
             require_csrf=False)
def login_view(request):
    """."""
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        if check_credentials(username, password):
            # import pdb;pdb.set_trace()
            auth_head = remember(request, username)
            return HTTPFound(
                request.route_url('home'),
                headers=auth_head
            )

    return {}


@view_config(route_name="logout")
def logout_view(request):
    """."""
    auth_head = forget(request)
    return HTTPFound(request.route_url('home'), headers=auth_head)
