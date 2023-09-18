import functools
import json

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/data-issues')


@bp.route('/', methods=('GET', 'POST'))
def get_data_issues():
    # TODO: Find employees without a candidate using SQL
    employees_without_candidate_query = """
                SELECT e.* 
                FROM employees e 
                LEFT JOIN candidates c 
                    ON e.first_name = c.first_name AND e.last_name = c.last_name 
                WHERE c.id IS NULL
    """
    employees_without_candidate = get_db().execute(
        employees_without_candidate_query).fetchall()

    # TODO: Find candidates without employee SQL
    candidates_matched_multiple_times_query = """
                SELECT c.id, c.first_name, c.last_name, COUNT(e.id) matches
                FROM candidates c
                LEFT JOIN employees e
                    ON e.first_name = c.first_name AND e.last_name = c.last_name 
                GROUP BY 1, 2, 3
                HAVING matches > 1

    """
    candidates_matched_multiple_times = get_db().execute(
        candidates_matched_multiple_times_query).fetchall()

    # TODO: ETC.

    data_issues = [
        {
            "title": "Employees without candidate",
            "rows": [tuple(employee) for employee in employees_without_candidate],
            "total_count": len(employees_without_candidate),
            "columns": ['id', 'natural_key', 'first_name',
                        'last_name', 'division', 'department']
        },
        {
            "title": "Candidates with multiple matches",
            "rows": [tuple(candidate) for candidate in candidates_matched_multiple_times],
            "total_count": len(candidates_matched_multiple_times),
            "columns": ['id', 'first_name', 'last_name', 'count']
        }
    ]
    print(data_issues)

    return render_template('table.html', data_issues=data_issues)
