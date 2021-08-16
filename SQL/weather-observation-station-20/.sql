select cast (avg(1*lat_n)as numeric(20.4))
from (select lat_n, ra=row_number()over(order by ))