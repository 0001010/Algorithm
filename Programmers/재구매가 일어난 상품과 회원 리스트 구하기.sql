SELECT USER_ID, PRODUCT_ID
FROM (SELECT USER_ID,PRODUCT_ID, COUNT(*) AS COUNTS
FROM ONLINE_SALE  
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNTS>=2
ORDER BY USER_ID, PRODUCT_ID DESC) AS T;