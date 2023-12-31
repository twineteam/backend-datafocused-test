import sqlite3
import json

import click
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

    # insert employees
    with open('./mockdata/employees.json', 'r') as json_file:
        data = json.load(json_file)
        for item in data:
            db.execute("INSERT INTO employees (employee_id, first_name, last_name, division, department) VALUES (?, ?, ?, ?, ?)",
                       (item["id"], item["firstName"], item["lastName"], item["division"], item["department"]))
            db.commit()

    # insert candidates
    with open('./mockdata/candidates.json', 'r') as json_file:
        data = json.load(json_file)
        for item in data:
            db.execute("INSERT INTO candidates (candidate_id, first_name, last_name, division, department) VALUES (?, ?, ?, ?, ?)",
                       (item["id"], item["firstName"], item["lastName"], item["division"], item["department"]))
            db.commit()

    # insert interviews
    with open('./mockdata/interviews.json', 'r') as json_file:
        data = json.load(json_file)
        for item in data:
            db.execute("INSERT INTO interviews (interview_id, effective_date, candidate_id, stage) VALUES (?, ?, ?, ?)",
                       (item["id"], item["effectiveDate"], item["candidateId"], item["stage"]))
            db.commit()


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    # app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
