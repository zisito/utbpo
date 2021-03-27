DROP TABLE IF EXISTS subject;
DROP TABLE IF EXISTS subject_class;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS field_spec;
DROP TABLE IF EXISTS contract;

-- table subject

CREATE TABLE "subject" (
	"id" VARCHAR(20) NOT NULL,
	"subject_name" VARCHAR(64) NOT NULL,
	"teacher_id" INTEGER NULL,
	"lecture_count" INTEGER NULL,
	"seminar_count" INTEGER NULL,
	"practice_count" INTEGER NULL,
	"weekly_count" INTEGER NULL,
	"semester_count" INTEGER NULL,
	"lang" VARCHAR(2) NULL,
	"study_type" VARCHAR(2) NOT NULL,
	"study_field_list" TEXT NULL,
	"year_of_study" INTEGER NOT NULL,
	"semester" VARCHAR(2) NOT NULL,
	PRIMARY KEY ("id")
)
;

-- table subject-class

CREATE TABLE "subject_class" (
	"class_id" INTEGER NOT NULL,
	"subject_id" VARCHAR(20) NULL,
	"type" VARCHAR(8) NOT NULL,
	"capacity" INTEGER NULL,
	"max_capacity" INTEGER NULL,
	"work_points" INTEGER NULL,
	PRIMARY KEY ("class_id"),
	CONSTRAINT "0" FOREIGN KEY ("subject_id") REFERENCES "subject" ("id")
)
;
CREATE TABLE "employee" (
	"teacher_id" INTEGER NOT NULL,
	"name" VARCHAR(64) NULL,
	"surname" VARCHAR(128) NULL,
	"email" VARCHAR(128) NULL,
	"phone" VARCHAR(64) NULL,
	"mobile_phone" VARCHAR(64) NULL,
	"contract_weight" REAL NULL,
	"study_perc" REAL NULL,
	"study_en_perc" REAL NULL,
	PRIMARY KEY ("teacher_id")
)
;

CREATE TABLE "field_spec" (
	"field_id" VARCHAR(64) NOT NULL,
	"field_name" VARCHAR(64) NULL,
	"student_count" INTEGER NULL,
	"specialization" VARCHAR(8) NULL,
	"study_type" VARCHAR(10) NOT NULL,
	PRIMARY KEY ("field_id")
)
;

CREATE TABLE "contract" (
	"id" INTEGER NOT NULL,
	"assigned" INTEGER NULL,
	"teacher_id" INTEGER NULL,
	"work_points" REAL NULL,
	"type" VARCHAR(1) NULL,
	PRIMARY KEY ("id"),
	CONSTRAINT "teacher_fk" FOREIGN KEY ("teacher_id") REFERENCES "employee" ("teacher_id")
	)
;

