SELECT ROUND(LONG_W,4)from station where LAT_N =(SELECT MAX(LAT_N)FROM Station where lat_N<137.2345);
