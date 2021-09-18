select id, age, coins_needed, powers
from(select wands.id as id, 
       wands_property.age as age, 
       wands.coins_needed as coins_needed,
       wands.power as powers,
       wands.code as code,
       row_number() over (partition by wands.code,wands.power order by wands.coins_needed) as rn
    from wands join wands_property
    on wands.code=wands_property.code
    where wands_property.is_evil!=1)
where rn=1
order by powers desc,age desc;