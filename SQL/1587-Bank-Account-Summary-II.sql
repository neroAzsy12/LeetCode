/*
Table: Users (account int, name varchar(20))
Table: Transactions (trans_id int, account int, amount int, transacted_on date)

Write an SQL query to report the name and balance of users with a balance higher than 10000. 
The balance of an account is equal to the sum of the amounts of all transactions involving that account.
Return the result table in any order.
*/
SELECT Users.name, SUM(Transactions.amount) AS 'balance'
FROM Users
INNER JOIN Transactions ON Users.account = Transactions.account
GROUP BY Users.name
HAVING balance > 10000;