select distinct city
from station
where SUBSTR(city,1,1) in ('A', 'E', 'I', 'O','U');