-- LIKE Operator
-- The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.
-- There are two wildcards often used in conjunction with the LIKE operator:
-- 1. The percent sign (%) represents zero, one, or multiple characters
-- 2. The underscore sign (_) represents one, single character
-- The percent sign and the underscore can also be used in combinations!

-- LIKE Syntax --
-- SELECT column1, column2, ...
-- FROM table_name
-- WHERE columnN LIKE pattern;

-- You can also combine any number of conditions using AND or OR operators.

-- Examples:
-- 1. The following SQL statement selects all customers with a CustomerName starting with "a":

SELECT * FROM Customer
WHERE CustomerName LIKE 'a%';


-- 2. The following SQL statement selects all customers with a CustomerName ending with "a":

SELECT * FROM Customer
WHERE CustomerName LIKE '%a';


-- 3. The following SQL statement selects all customers with a CustomerName that have "or" in any position:

SELECT * FROM Customer
WHERE CustomerName LIKE '%or%';


-- 4. The following SQL statement selects all customers with a CustomerName that have "r" in the second position:

SELECT * FROM Customer
WHERE CustomerName LIKE '_r%';


-- 5. The following SQL statement selects all customers with a CustomerName that starts with "a" and are at least 3 characters in length:

SELECT * FROM Customer
WHERE CustomerName LIKE 'a__%';


-- 6. The following SQL statement selects all customers with a ContactName that starts with "a" and ends with "o":

SELECT * FROM Customer
WHERE ContactName LIKE 'a%o';


-- 7. The following SQL statement selects all customers with a CustomerName that does NOT start with "a":

SELECT * FROM Customer
WHERE CustomerName NOT LIKE 'a%';