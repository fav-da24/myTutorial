-- COUNT(), AVG() and SUM() Functions

-- COUNT() Syntax -- 
-- SELECT COUNT(column_name)
-- FROM table_name
-- WHERE condition;
-- The AVG() function returns the average value of a numeric column. 

-- AVG() Syntax --
-- SELECT AVG(column_name)
-- FROM table_name
-- WHERE condition;
-- The SUM() function returns the total sum of a numeric column. 

-- SUM() Syntax --
-- SELECT SUM(column_name)
-- FROM table_name
-- WHERE condition;


-- COUNT() Example

SELECT COUNT(ProductID)
FROM Products;


-- AVG() Example

SELECT AVG(Price)
FROM Products;

-- Note: NULL values are ignored.


-- SUM Example

SELECT SUM(Quantity)
FROM OrderDetails;