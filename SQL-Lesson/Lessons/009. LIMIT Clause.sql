-- LIMIT Clause
-- The LIMIT clause is used to specify the number of records to return.
-- The LIMIT clause is useful on large tables with thousands of records. 
-- Returning a large number of records can impact performance.

SELECT * FROM Customer
LIMIT 3;


-- What if we want to select records 4 - 6 (inclusive)?
-- MySQL provides a way to handle this: by using OFFSET.
-- The SQL query below says "return only 3 records, start on record 4 (OFFSET 3)":

SELECT * FROM Customer
LIMIT 3 OFFSET 3;


-- ADD a WHERE CLAUSE

SELECT * FROM Customer
WHERE Country='Germany'
LIMIT 3;