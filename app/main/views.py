from flask import render_template, request, redirect, url_for,abort
from . import main
from .. import db

@main.route('/')
def index():
    return '<h1> Welcome to Football Fantasy </h1>'
