-- WHERE Statement
-- The WHERE clause is not only used in SELECT statements, it is also used in UPDATE, DELETE, etc.!

SELECT * FROM customer
WHERE Country = 'Mexico';


-- Text Fields vs. Numeric Fields

SELECT * FROM customer
WHERE CustomerID = 1;