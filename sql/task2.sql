WITH preptable AS (SELECT id,
			  name,
                          COUNT(sales.employee_id) AS sales_c,
                          SUM(sales.price) AS sales_s
                   FROM employee
                   LEFT JOIN sales
                   ON employee.id == sales.employee_id
                   GROUP BY sales.employee_id) 

SELECT id,
	   name,
       sales_c,
       DENSE_RANK() OVER(ORDER BY sales_c) sales_rank_c,
       sales_s,
       DENSE_RANK() OVER(ORDER BY sales_s) sales_rank_s
FROM preptable
