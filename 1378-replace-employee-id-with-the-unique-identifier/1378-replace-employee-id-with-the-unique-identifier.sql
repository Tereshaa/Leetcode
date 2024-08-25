# Write your MySQL query statement belows
select EmployeeUNI.unique_id,employees.name
from employees
LEFT JOIN EmployeeUNI on EmployeeUNI.id=employees.id