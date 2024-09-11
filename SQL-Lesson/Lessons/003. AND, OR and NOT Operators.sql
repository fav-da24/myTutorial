-- AND, OR and NOT Operators

-- AND example

SELECT * FROM customer
WHERE Country = 'Germany' AND City = 'Berlin';


-- OR example

SELECT * FROM customer
WHERE City = 'Berlin' OR City = 'Stuttgart';


-- NOT example

SELECT * FROM customer
WHERE NOT Country = 'Mexico';


-- Combining AND, OR and NOT

SELECT * FROM customer
WHERE Country = 'Germany' AND (City = 'Berlin' OR City = 'Stuttgart');


SELECT * FROM customer
WHERE NOT Country = 'Germany' AND NOT Country = 'USA';