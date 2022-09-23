/*
Table: Person (personId int, firstName varchar(255), lastName varchar(255))
Table: Address (addressId int, personId int, city varchar(255), state varchar(255))

Write a query to report the first name, last name, city, and state of each person in the Person table. 
If the address of a personId is not present in the Address table, report null instead.
*/
SELECT firstName, lastName, city, state
FROM Person
LEFT JOIN Address ON Person.personId = Address.personId;

SELECT firstName, lastName, city, state
FROM Person
LEFT JOIN Address USING(personId);