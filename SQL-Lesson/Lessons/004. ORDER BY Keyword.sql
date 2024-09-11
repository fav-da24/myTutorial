-- ORDER BY Keyword

SELECT * FROM Customer
ORDER BY Country;


-- ORDER BY DESC Example

SELECT * FROM Customer
ORDER BY Country DESC;


-- ORDER BY Several Columns Example

SELECT Country, CustomerName FROM Customer
ORDER BY Country, CustomerName;


-- ORDER BY Several Columns Example 2

SELECT Country, CustomerName FROM Customer
ORDER BY Country ASC, CustomerName DESC;