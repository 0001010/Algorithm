seleselect distinct city
from station
where substr(city,1,1) not in ('A','E','I','O','U') or substr(city,-1) not in ('a','e','i','o','u');