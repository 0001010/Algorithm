SELECT CATEGORY, COUNT(*) AS PRODUCTS
FROM (SELECT SUBSTRING(PRODUCT_CODE,1,2) AS CATEGORY
FROM PRODUCT) AS T
GROUP BY CATEGORY
ORDER BY CATEGORY;
