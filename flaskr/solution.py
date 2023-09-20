import sqlite3

from flask import (
    Blueprint, render_template
)

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/')


def sqllite_rows_to_list(values):
    list_accumulator = []
    for item in values:
        list_accumulator.append({k: item[k] for k in item.keys()})
    return list_accumulator


def py_solution():
    # Matching algorithm between <Employees, Candidate> use employee.first_name == candidate.first_name && employee.last_name == candidate.last_name
    cursor = get_db().cursor()
    employees = sqllite_rows_to_list(
        cursor.execute("SELECT * FROM employees").fetchall())
    candidates = sqllite_rows_to_list(
        cursor.execute("SELECT * FROM candidates").fetchall())

    # Level 1.1
    # TODO: Find employees without a candidate using Python --> Should have 5
    employees_without_candidate = []

    # Level 1.2
    # TODO: Find employees without a candidate using Python --> Should have 16
    candidates_matched_multiple_times = []

    tables = [
        {
            "title": "Employees without candidate",
            "rows": [employee.values() for employee in employees_without_candidate],
            "total_count": len(employees_without_candidate),
            "columns": ['id', 'first_name',
                        'last_name', 'division', 'department']
        },
        {
            "title": "Candidates with multiple matches",
            "rows": [candidate.values() for candidate in candidates_matched_multiple_times],
            "total_count": len(candidates_matched_multiple_times),
            "columns": ['id', 'first_name', 'last_name', 'count']
        },
    ]

    return render_template('table.html', tables=tables)


def sql_solution():
    # Matching algorithm between <Employees, Candidate> use employee.first_name == candidate.first_name && employee.last_name == candidate.last_name

    # Level 1.1
    # TODO: Find employees without a candidate using SQL --> Should have 5
    # (FLEXIBLE) "columns": ['id', 'natural_key', 'first_name','last_name', 'division', 'department']
    employees_without_candidate_query = """
    """
    employees_without_candidate = get_db().execute(
        employees_without_candidate_query).fetchall()

    # Level 1.2
    # TODO: Find candidates without employee SQL --> Should have 16
    # "columns": ['id', 'first_name', 'last_name', 'count']
    candidates_matched_multiple_times_query = """
    """
    candidates_matched_multiple_times = get_db().execute(
        candidates_matched_multiple_times_query).fetchall()

    # Level 2.1
    # TODO: Match interviews with candidate to create a table:
    # "columns": ['interview_id', 'candidate_id', 'full_name', 'stage', 'effective_date']
    interviews_and_candidate_query = """
    """
    interviews_and_candidate = get_db().execute(
        interviews_and_candidate_query).fetchall()

    # Level 2.2
    # TODO: Create a Slowly Changing Dimension (SCD) Type 2 table.
    # "columns": ['interview_id', 'candidate_id', 'full_name', 'stage', 'valid_from', 'valid_to']

    # ~~~~~~~~~~~~~~~~~~~~~~ DEFINITIONS ~~~~~~~~~~~~~~~~~~~~~~
    # valid_from = effective_date
    # valid_to = effective_date of the next chronological record

    # ~~~~~~~~~~~~~~~~~~~~~~ EXAMPLE ~~~~~~~~~~~~~~~~~~~~~~
    # Given:
    # stage       |full_name   | effective_date
    # phone call,  Marx Low,     '2023-01-01'
    # offer,       Marx Low,     '2023-02-01'
    # Expected:
    # stage       |full_name   | valid_from     |  valid_to
    # offer,       Marx Low,     '2023-02-01',   '9999-12-31' <-- ** Take note of the '9999-12-31' date for the first record of each Candidate
    # phone call,  Marx Low,     '2023-01-01',   '2023-02-01'

    interviews_and_candidate_scd_type_two_query = """
    """
    interviews_and_candidate_scd_type_two = get_db().execute(
        interviews_and_candidate_scd_type_two_query).fetchall()

    tables = [
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
        },
        {
            "title": "Interview and candidate",
            "rows": [tuple(interview) for interview in interviews_and_candidate],
            "total_count": len(interviews_and_candidate),
            "columns": ['interview_id', 'candidate_id', 'full_name', 'stage', 'effective_date']
        },
        {
            "title": "Interview and candidate SCD Type II",
            "rows": [tuple(interview) for interview in interviews_and_candidate_scd_type_two],
            "total_count": len(interviews_and_candidate_scd_type_two),
            "columns": ['interview_id', 'candidate_id', 'full_name', 'stage', 'valid_from', 'valid_to']
        },
    ]

    return render_template('table.html', tables=tables)


@bp.route('/', methods=('GET', 'POST'))
def get_solution():

    return py_solution()
    # return sql_solution()
