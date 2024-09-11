-- MIN() and MAX() Functions

-- MIN() Syntax --
-- SELECT MIN(column_name)
-- FROM table_name
-- WHERE condition;

-- MAX() Syntax --
-- SELECT MAX(column_name)
-- FROM table_name
-- WHERE condition;


-- MIN() Example

select * from products;

SELECT MIN(Price) AS SmallestPrice
FROM Products;


-- MAX() Example

SELECT MAX(Price) AS LargestPrice
FROM Products;