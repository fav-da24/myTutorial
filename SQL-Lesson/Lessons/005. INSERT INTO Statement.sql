-- INSERT INTO Statement

INSERT INTO Customer (CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');

SELECT * FROM customer
where CustomerName = 'Cardinal';


-- Insert Data Only in Specified Columns

INSERT INTO Customer (CustomerName, City, Country)
VALUES ('Cardinal', 'Stavanger', 'Norway');