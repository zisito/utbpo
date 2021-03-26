from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flaskr.db import get_db

bp = Blueprint('contract', __name__, url_prefix='/contract')


@bp.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        code = request.form['code']
        subject = request.form['subject']
        db = get_db()
        error = None

        if not code:
            error = 'Name is required.'
        elif not subject:
            error = 'Studytype is required.'
        elif db.execute(
            'SELECT name FROM contract WHERE name = ?', (code, )
        ).fetchone() is not None:
            error = 'Employee {} is already known.'.format(code)

        if error is None:
            db.execute(
                'INSERT INTO contract (code, subject) VALUES (?, ?)',
                (code, subject)
            )
            db.commit()
            return redirect(url_for('contract.add'))

        flash(error)

    #return render_template('employee/fill.html')
    return render_template('add.html')
