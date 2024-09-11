-- UPDATE Statement
-- Be careful when updating records in a table! 
-- Notice the WHERE clause in the UPDATE statement. 
-- The WHERE clause specifies which record(s) that should be updated. 
-- If you omit the WHERE clause, all records in the table will be updated!

-- UPDATE Table

UPDATE Customer
SET ContactName = 'Alfred Schmidt', City = 'Frankfurt'
WHERE CustomerID = 1;

select *
from customer
where ContactName = 'Alfred Schmidt';


-- UPDATE Multiple Records

UPDATE Customer
SET PostalCode = 00000
WHERE Country = 'Mexico';

select *
from customer
where Country = 'Mexico';