SELECT PRODUCT_CODE, (TOTAL*PRICE) AS SALES
FROM PRODUCT AS T1 JOIN (SELECT PRODUCT_ID, SUM(SALES_AMOUNT) AS TOTAL
FROM OFFLINE_SALE 
GROUP BY PRODUCT_ID) T2
ON (T1.PRODUCT_ID = T2.PRODUCT_ID)
ORDER BY SALES DESC, PRODUCT_CODE;