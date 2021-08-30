select n, case when levels=min_level then 'Root'
               when levels=max_level then 'Leaf' 
               else 'Inner' end
from (select n,p, level as levels, min(level) over () as min_level, max(level) over () as max_level
      from bst
      start with p is null
      connect by prior n=p
      order by n);