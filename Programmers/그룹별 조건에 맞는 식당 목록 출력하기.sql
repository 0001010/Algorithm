SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
FROM(SELECT TTT.MEMBER_NAME, MEMBER_ID
    FROM (SELECT MAX(COUNTS) AS MAX_COUNT
            FROM (SELECT MEMBER_NAME, COUNT(MEMBER_NAME) AS COUNTS
                    FROM REST_REVIEW AS T1 JOIN MEMBER_PROFILE AS T2
                    ON(T1.MEMBER_ID = T2.MEMBER_ID)
                    GROUP BY MEMBER_NAME) AS T) AS TT JOIN (SELECT MEMBER_NAME, COUNT(MEMBER_NAME) AS COUNTS
                                        FROM REST_REVIEW AS T1 JOIN MEMBER_PROFILE AS T2
                                        ON(T1.MEMBER_ID = T2.MEMBER_ID)
                                        GROUP BY MEMBER_NAME) AS TTT
                                        ON (TT.MAX_COUNT = TTT.COUNTS) JOIN 
                                        MEMBER_PROFILE 
                                        ON (TTT.MEMBER_NAME = MEMBER_PROFILE.MEMBER_NAME)) AS TTTT JOIN 
                                        REST_REVIEW
                                        ON (TTTT.MEMBER_ID = REST_REVIEW.MEMBER_ID)
                                        ORDER BY REVIEW_DATE, REVIEW_TEXT;
