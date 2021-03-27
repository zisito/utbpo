#Database (class description aswell)

### Table name: _subject_

Columns:

subject_id - Primary key (varchar 16)

subject_name - varchar (64)

teacher_id - Int // maybe teacher name?

lecture_count - Int

seminar_count - Int

practice_count - Int

weekly_count - Int // weeks of semester?

semester_total - Int //total count of hours

lang - varchar(2) // default CS?

study_type - varchar(2) // PS or KS 

study_field_list - varchar // FK on field_spec?

year_of_study - Int // 

semester - Varchar(2)



### Table name: _subject_class_
Columns:

class_id - varchar

subject_id - varchar

type - varchar // lecture / seminar/practice/ tests

capacity - Int

max_capacity - Int

work_points - Double

### Table name: _employee_

Columns:

teacher_id - Primary key - Int

name - varchar (64)

email - varchar

phone - varchar

mobile_phone - varchar

contract_weight - float <0;1>

study_perc - float <0;1>

study_en_perc - float <0;1>

### Table name: _field_spec_

Columns:

field_id - Primary key 

field_name - varchar (64)

student_count - Int

specialization - varchar(2)

study_type - varchar (2) // BC/ING?

  

### Table name: _contract_

Columns:

contract_id  - Primary key 

assigned - bool

employee_id - Int

work_points - Double

type - varchar(1) // T - teaching, P - project, E - extra















