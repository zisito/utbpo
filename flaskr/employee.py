import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flaskr.db import get_db

bp = Blueprint('employee', __name__, url_prefix='/employee')


@bp.route('/fill', methods=('GET', 'POST'))
def fill():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        db = get_db()
        error = None

        if not name:
            error = 'Name is required.'
        elif not surname:
            error = 'Surname is required.'
        elif db.execute(
            'SELECT name FROM employee WHERE name = ?', (name, )
        ).fetchone() is not None:
            error = 'Employee {} is already known.'.format(name)

        if error is None:
            db.execute(
                'INSERT INTO employee (name, surname) VALUES (?, ?)',
                (name, surname)
            )
            db.commit()
            return redirect(url_for('employee.fill'))

        flash(error)

    #return render_template('employee/fill.html')
    return render_template('employee_fill.html')
