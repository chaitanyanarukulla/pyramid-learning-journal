"""security."""
import os
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Allow, Authenticated
from pyramid.session import SignedCookieSessionFactory

from passlib.apps import custom_app_context as pwd_context


class NewRoot(object):
    """."""

    def __init__(self, request):
        """."""
        self.request = request

    __acl__ = [
        (Allow, Authenticated, 'add')
    ]


def check_credentials(username, password):
    """Return True if correct username and password, else False."""
    if username and password:
        # proceed to check credentials
        if username == os.environ.get("AUTH_USERNAME", ''):
            return pwd_context.verify(password, os.environ.get("AUTH_PASSWORD",
                                      ''))
    return False


def includeme(config):
    """Pyramid security configuration."""
    auth_secret = os.environ.get("AUTH_SECRET", "password")
    authn_policy = AuthTktAuthenticationPolicy(
        secret=auth_secret,
        hashalg="sha512"
    )
    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.set_root_factory(NewRoot)
    # Session stuff for CSRF Protection
    session_secret = os.environ.get("SESSION_SECRET", "chaipassword")
    session_factory = SignedCookieSessionFactory(session_secret)
    config.set_session_factory(session_factory)
    config.set_default_csrf_options(require_csrf=True)