select A.company_code, A.founder,count(distinct B.lead_manager_code), count(distinct B.senior_manager_code),count(distinct B.manager_code),count(distinct employee_code)
from company A
JOIN Employee B
On A.company_code= B.company_code
group by A.company_code, A.founder
Order by A.company_code
