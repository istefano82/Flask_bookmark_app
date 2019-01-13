from elasticsearch import NotFoundError
from flask import render_template, redirect, url_for, request, g
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from . import main
from .. import login_manager
from ..models import User, Bookmark, Tag, Receipt
from .forms import SearchForm


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

@main.route('/')
def index():
    return render_template('index.html', new_bookmarks=Bookmark.newest(5))


@main.route('/search')
@login_required
def search():
    if not g.search_form.validate():
        return redirect(url_for('.index'))
    page = request.args.get('page', 1, type=int)
    results_per_page = 20
    try:
        search_results, total = Receipt.search(g.search_form.q.data, page, results_per_page)
    except NotFoundError:
        total = 0
    if not total:
        return render_template('search.html', search_results=None)
    next_url = url_for('main.search', q=g.search_form.q.data, page=page + 1) \
        if total > page * results_per_page else None
    prev_url = url_for('main.search', q=g.search_form.q.data, page=page - 1) \
        if page > 1 else None
    return render_template('search.html', title='Search', search_results=search_results,
                           next_url=next_url, prev_url=prev_url)

@main.app_errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@main.app_context_processor
def inject_tags():
    return dict(all_tags=Tag.all)


@main.before_app_request
def before_request():
    if current_user.is_authenticated:
        g.search_form = SearchForm()
