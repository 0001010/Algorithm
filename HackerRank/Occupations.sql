select min(case when occupation='Doctor' then name end) as doctor,
       min(case when occupation='Professor' then name end) as Professor,
       min(case when occupation='Singer' then name end) as Singer,
       min(case when occupation='Actor' then name end) as Actor
from (select occupation, 
      name,
      row_number() over (partition by occupation order by name) rn
      from occupations)
group by rn
order by doctor, professor, singer, actor;