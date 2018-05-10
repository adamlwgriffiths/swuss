from __future__ import absolute_import, print_function
from flask import Blueprint, render_template

blueprint = Blueprint('index', __name__)

def pages():
    return {
        'PlantUML': '/plantuml',
    }

def context():
    return {
        'pages': pages(),
    }

@blueprint.route('/')
def index():
    return render_template('index.html', **context())
