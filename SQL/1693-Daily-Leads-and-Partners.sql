/*
Table: DailySales(date_id date, make_name varchar(20), lead_id int, partner_id int)

Write an SQL query that will, for each date_id and make_name, 
return the number of distinct lead_id's and distinct partner_id's.

Return the result table in any order.
*/
SELECT date_id, make_name, COUNT(DISTINCT(lead_id)) AS unique_leads, COUNT(DISTINCT(partner_id)) AS unique_partners
FROM DailySales
GROUP BY date_id, make_name;