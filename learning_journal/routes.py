"""Routes with names and uris associated."""


def includeme(config):
    """Include the following routes for static files and uri paths."""
    config.add_static_view('static', 'learning_journal:static')
    config.add_route('home', '/')
    config.add_route('detail', '/journal/{id:\d+}')
    config.add_route('create', '/journal/new-entry')
    config.add_route('update', '/journal/{id:\d+}/edit-entry')
