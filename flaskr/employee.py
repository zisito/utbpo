import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flaskr.db import get_db

bp = Blueprint('employee', __name__, url_prefix='/employee')


@bp.route('/add', methods=('GET', 'POST'))
def add():
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
    return render_template('add.html')


@bp.route('/view')
def view():
    db = get_db()
    data = db.execute('SELECT name, surname FROM employee').fetchall()

    return render_template('view.html', output_data = data)
