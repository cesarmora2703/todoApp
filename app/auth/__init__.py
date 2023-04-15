from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix="/auth")

#Esta importacion debe hacerse despues de instanciar el Blueprint
from . import views