from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flaskr.db import get_db

bp = Blueprint('subject', __name__, url_prefix='/subject')


@bp.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        name = request.form['code']
        studytype = request.form['name']
        db = get_db()
        error = None

        if not name:
            error = 'Name is required.'
        elif not studytype:
            error = 'Studytype is required.'
        elif db.execute(
            'SELECT name FROM subject WHERE code = ?', (name, )
        ).fetchone() is not None:
            error = 'Employee {} is already known.'.format(name)

        if error is None:
            db.execute(
                'INSERT INTO subject (code, name) VALUES (?, ?)',
                (name, studytype)
            )
            db.commit()
            return redirect(url_for('subject.add'))

        flash(error)

    #return render_template('employee/fill.html')
    return render_template('add.html')
