-- DELETE Statement
-- Be careful when deleting records in a table! 
-- Notice the WHERE clause in the DELETE statement. 
-- The WHERE clause specifies which record(s) should be deleted. 
-- If you omit the WHERE clause, all records in the table will be deleted!

select * from customer
where CustomerName = 'Alfreds Futterkiste';

DELETE FROM Customer WHERE CustomerName='Alfreds Futterkiste';


-- Delete All Records (syntax)

DELETE FROM table_name;