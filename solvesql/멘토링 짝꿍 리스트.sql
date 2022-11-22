select mti.employee_id as mentee_id, 
      mti.name as mentee_name, 
      mto.employee_id as mentor_id,
      mto.name as mentor_name
from (select *
  from employees
  where join_date>='2021-09-31') as mti left join 
  (select *
  from employees
  where join_date<='2019-12-31') as mto
  on (mti.department != mto.department)
  
order by mentee_id, mentor_id;