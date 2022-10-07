/*
Table: Department (id int, revenue int, month varchar(5))

Write an SQL query to reformat the table such that there is a department id column 
and a revenue column for each month, total of 13 columns
Return the result table in any order.
*/
SELECT id,
       SUM(IF(month = 'Jan', revenue, NULL)) AS Jan_Revenue,
       SUM(IF(month = 'Feb', revenue, NULL)) AS Feb_Revenue,
       SUM(IF(month = 'Mar', revenue, NULL)) AS Mar_Revenue,
       SUM(IF(month = 'Apr', revenue, NULL)) AS Apr_Revenue,
       SUM(IF(month = 'May', revenue, NULL)) AS May_Revenue,
       SUM(IF(month = 'Jun', revenue, NULL)) AS Jun_Revenue,
       SUM(IF(month = 'Jul', revenue, NULL)) AS Jul_Revenue,
       SUM(IF(month = 'Aug', revenue, NULL)) AS Aug_Revenue,
       SUM(IF(month = 'Sep', revenue, NULL)) AS Sep_Revenue,
       SUM(IF(month = 'Oct', revenue, NULL)) AS Oct_Revenue,
       SUM(IF(month = 'Nov', revenue, NULL)) AS Nov_Revenue,
       SUM(IF(month = 'Dec', revenue, NULL)) AS Dec_Revenue
FROM Department
GROUP BY id;