SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
WHERE SUBSTRING(ADDRESS, 1,3)="강원도"
ORDER BY FACTORY_ID;