SELECT DISTINCT CITY FROM STATION WHERE LEFT (CITY,1) NOT IN ('A','E','I','O','U')OR RIGHT (CITY,1) NOT IN ('a','A','e','E','i','I','o','O','u','U') ;
