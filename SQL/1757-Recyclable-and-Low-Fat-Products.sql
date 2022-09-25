/*
Table: Products (product_id int, low_fats ENUM('Y', 'N'), recyclable ENUM('Y', 'N'))

Write a query to find the ids of products that are both low fat and recyclable.
*/
SELECT product_id
FROM Products
WHERE low_fats='Y' AND recyclable='Y';