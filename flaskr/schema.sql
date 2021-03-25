DROP TABLE IF EXISTS subject;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS field_spec;
DROP TABLE IF EXISTS contract;

CREATE TABLE subject (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code VARCHAR(16) NOT NULL,
  subject_name VARCHAR(64) NOT NULL,
  teacher_id INTEGER NOT NULL,
  lecture_count INTEGER DEFAULT 0,
  seminar_count INTEGER DEFAULT 0,
  practice_count INTEGER DEFAULT 0,
  weekly_count INTEGER DEFAULT 0,
  semester_count INTEGER DEFAULT 0,
  lang VARCHAR(2) DEFAULT "CS",
  study_type VARCHAR(2) NOT NULL,
  study_field_list TEXT NULL,
  year_of_study INTEGER NOT NULL,
  semester varchar(2) not null,
  max_capacity INTEGER default 0
);

CREATE TABLE employee (
  id INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE field_spec (
  id INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE contract(
  id INTEGER PRIMARY KEY AUTOINCREMENT
);
