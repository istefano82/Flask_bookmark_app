from flask import render_template, flash, redirect, url_for, request, abort
from flask_login import login_required, current_user

from . import receipts
#from .forms import BookmarkForm
from .. import db
from ..models import User, Bookmark, Tag

@receipts.route('/add', methods=['GET'])
@login_required
def add():
    return "Adding Blueprint"