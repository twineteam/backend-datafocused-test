DROP TABLE IF EXISTS candidates;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS interviews;

CREATE TABLE candidates (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  candidate_id TEXT, -- natural key
  first_name TEXT,
  last_name TEXT,
  division TEXT,
  department TEXT
);

CREATE TABLE employees (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  employee_id TEXT, -- natural key
  first_name TEXT,
  last_name TEXT,
  division TEXT,
  department TEXT
);

CREATE TABLE interviews (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  effective_date DATE,
  interview_id TEXT, -- natural key
  candidate_id TEXT,
  stage TEXT
);