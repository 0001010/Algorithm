select case when grade<8 then NULL else name end, grade,marks
from students, grades
where students.marks between grades.min_mark and grades.max_mark
order by grade desc, name;