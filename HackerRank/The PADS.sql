SELECT CONCAT(NAME,CONCAT('(',CONCAT(SUBSTR(OCCUPATION,1,1),')')))
FROM OCCUPATIONS
ORDER BY NAME;

SELECT 'There are a total of', COUNT(NAME), CONCAT(LOWER(OCCUPATION),'s.')
FROM OCCUPATIONS
GROUP BY OCCUPATION
ORDER BY COUNT(NAME), OCCUPATION;