-- __define-ocg__ This query returns employees with higher salaries than their managers and includes promotion opportunities.

SELECT 
    e.Name AS EmployeeName,
    e.Salary AS EmployeeSalary,
    IFNULL(m.Name, 'No Manager') AS ManagerName,
    IF(m.Salary IS NULL OR e.Salary > m.Salary, 'Yes', 'No') AS PromotionOpportunity
FROM 
    maintable_0A6UY e
LEFT JOIN 
    maintable_0A6UY m ON e.ManagerID = m.ID
ORDER BY 
    ABS(e.Salary - IFNULL(m.Salary, 0)) DESC;  -- Ordering by salary difference
