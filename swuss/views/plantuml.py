from __future__ import absolute_import, print_function
import json
from flask import Blueprint, render_template, request
from . import index

blueprint = Blueprint('plantuml', __name__)

@blueprint.route('/plantuml')
def plantuml():
    return render_template('plantuml.html', **index.context())

@blueprint.route('/plantuml/generate', methods=['POST'])
def generate():
    data = json.loads(request.data)
    content = data['text']
    return content
