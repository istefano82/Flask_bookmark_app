import os
import errno

from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user
from werkzeug.utils import secure_filename

from . import receipts
from .. import db
from ..models import User, Receipt
from ..ocr import process_image


@receipts.route('/add', methods=['GET', 'POST'])
def add():
        # body = 'some text'
        # receipt = Receipt(user=current_user, body=body)
        # db.session.add(receipt)
        # db.session.commit()
        # flash("Stored '{}'".format(receipt.body))
        return render_template('upload.html')


def _store_receit_text(text):
        body = text
        receipt = Receipt(user=current_user, body=body)
        db.session.add(receipt)
        db.session.commit()


@receipts.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        try:
            f = request.files['file']
        except KeyError:
            return redirect(url_for('.add'))
        filename = secure_filename(f.filename)
        try:
            os.makedirs('uploads')
        except FileExistsError as e:
            pass
        save_location = os.path.join('uploads', filename)
        f.save(save_location)
        flash('file "{}" uploaded successfully'.format(f.filename))
        image_text = process_image(save_location)
        _store_receit_text(image_text)
        return redirect(url_for('main.index'))


@receipts.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)


@receipts.route('/receipt_list')
def receipt_list():
    search_results = Receipt.query.all()
    total = len(search_results)
    page = request.args.get('page', 1, type=int)
    results_per_page = 20
    next_url = url_for('main.search', q=g.search_form.q.data, page=page + 1) \
        if total > page * results_per_page else None
    prev_url = url_for('main.search', q=g.search_form.q.data, page=page - 1) \
        if page > 1 else None
    return render_template('search.html', title='Search', search_results=search_results,
                           next_url=next_url, prev_url=prev_url)
