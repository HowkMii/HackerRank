SELECT DISTINCT CITY FROM STATION WHERE LEFT (CITY,1) IN ('a','A','e','E','i','I','o','O','u','U')AND RIGHT (CITY,1) IN ('a','A','e','E','i','I','o','O','u','U') ;
