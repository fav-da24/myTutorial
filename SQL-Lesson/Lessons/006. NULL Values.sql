-- NULL Values

-- IS NULL Operator

SELECT CustomerName, ContactName, Address
FROM Customer
WHERE Address IS NULL;


-- IS NOT NULL Operator

SELECT CustomerName, ContactName, Address
FROM Customer
WHERE Address IS NOT NULL;