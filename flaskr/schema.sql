DROP TABLE IF EXISTS candidates;
DROP TABLE IF EXISTS employees;

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