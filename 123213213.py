CREATE TABLE employees (
    emp_id INT,
    emp_name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);

INSERT INTO employees VALUES
(1, 'Rita', 'HR', 50000),
(2, 'Sita', 'Finance', 60000),
(3, 'Geeta', 'IT', 75000),
(4, 'Aman', 'IT', 80000),
(5, 'Rohan', 'HR', 55000),
(6, 'Kiran', 'Finance', 70000);

SELECT 
    SUM(salary) AS total_salary,
    AVG(salary) AS average_salary,
    COUNT(department) AS total_departments,
    MIN(salary) AS minimum_salary,
    MAX(salary) AS maximum_salary
FROM employees;
