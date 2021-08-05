SELECT (salary * months) as max_earnings, COUNT(*) as employee_count from employee group by max_earnings having max_earnings=MAX(salary * months) order by max_earnings desc limit 1;
