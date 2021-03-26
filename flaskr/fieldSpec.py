import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flaskr.db import get_db

bp = Blueprint('fieldspec', __name__, url_prefix='/fieldspec')


@bp.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        name = request.form['name']
        studytype = request.form['studytype']
        db = get_db()
        error = None

        if not name:
            error = 'Name is required.'
        elif not studytype:
            error = 'Studytype is required.'
        elif db.execute(
            'SELECT name FROM field_spec WHERE name = ?', (name, )
        ).fetchone() is not None:
            error = 'Employee {} is already known.'.format(name)

        if error is None:
            db.execute(
                'INSERT INTO field_spec (name, surname) VALUES (?, ?)',
                (name, studytype)
            )
            db.commit()
            return redirect(url_for('fieldspec.add'))

        flash(error)

    #return render_template('employee/fill.html')
    return render_template('add.html')
