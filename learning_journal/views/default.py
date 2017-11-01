from pyramid.response import Response
import os

HERE = os.path.abspath(__file__)
TEMPLATE = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'templates')


def list_view(request):
    with open(os.path.join(TEMPLATE, 'index.html')) as file:
        return Response(file.read())


def detail_view(request):
    with open(os.path.join(TEMPLATE, 'read.html')) as file:
        return Response(file.read())


def create_view(request):
    with open(os.path.join(TEMPLATE, 'create.html')) as file:
        return Response(file.read())


def update_view(request):
    with open(os.path.join(TEMPLATE, 'edit.html')) as file:
        return Response(file.read())
