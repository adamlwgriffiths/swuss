from __future__ import absolute_import, print_function
from flask import Blueprint, render_template
from . import index, plantuml


def register_blueprints(app):
    app.register_blueprint(index.blueprint)
    app.register_blueprint(plantuml.blueprint)
    return app
