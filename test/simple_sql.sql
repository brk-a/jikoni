-- Define the variable for filtering purposes
SET @varOcg = 1;

-- Query to identify employees with a higher salary than their manager
SELECT 
    e.Name AS EmployeeName, 
    e.Salary AS EmployeeSalary, 
    COALESCE(m.Name, 'No Manager') AS ManagerName, 
    CASE 
        WHEN e.Salary > m.Salary THEN 'Yes' 
        ELSE 'No' 
    END AS PromotionOpportunity
FROM 
    maintable_0A6UY e
LEFT JOIN 
    maintable_0A6UY m 
    ON e.ManagerID = m.ID
WHERE 
    @varOcg = 1 -- Using the variable varOcg to filter or control the promotion condition
ORDER BY 
    ABS(e.Salary - m.Salary) DESC;

-- __define-ocg__ The query uses the absolute salary difference to order employees by their promotion opportunity
