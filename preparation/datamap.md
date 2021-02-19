#Database (class description aswell)

### Table name: _subject_

Columns:

subject_id - Primary key (varchar 16)

subject_name - varchar (64)

teacher_id - Int // maybe teacher name?

lecture_count - Int

seminar_count - Int

practice_count - Int

weekly_count - Int

semester_count - Int

lang - varchar(2)

study_type - varchar(2)

study_field_list - varchar

year_of_study - Int

semester - Varchar(2)

max_capacity - Int


### Table name: _employee_

Columns:

teacher_id - Primary key - Int

teacher_name - varchar (64)

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

capacity - Int

max_capacity - Int

subject_id - Int/varchar

employee_id - Int













