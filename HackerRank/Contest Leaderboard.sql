select hackers.hacker_id, hackers.name, sum(score)
from (select hacker_id,
             challenge_id,
             score,
             row_number() over (partition by hacker_id, challenge_id order by score desc) as rn
      from submissions) pp join hackers
      on pp.hacker_id=hackers.hacker_id
where rn=1
group by hackers.hacker_id, hackers.name
having sum(score)>0
order by sum(score) desc, hackers.hacker_id;