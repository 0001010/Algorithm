select submissions.hacker_id, hackers.name
from challenges join difficulty 
on challenges.difficulty_level=difficulty.difficulty_level
    join submissions on challenges.challenge_id=submissions.challenge_id
    join hackers on submissions.hacker_id=hackers.hacker_id
where submissions.score=difficulty.score and challenges.difficulty_level=difficulty.difficulty_level
group by submissions.hacker_id, hackers.name
having count(submissions.hacker_id)>=2
order by count(submissions.challenge_id) desc, submissions.hacker_id;