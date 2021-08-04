select ceil((sum(salary)-sum(replace(cast(salary as char),'0','')))/count(*))from Employees;
