from flask import Blueprint

receipts = Blueprint('receipts', __name__)

from . import views
