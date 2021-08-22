select*
from(select months*salary as earnings, count(*)
     from Employee
     group by months*salary
     order by earnings desc)
where rownum=1;