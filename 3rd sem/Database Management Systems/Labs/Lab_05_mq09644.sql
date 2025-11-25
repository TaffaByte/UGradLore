-- Q1 Solution
--select *
--from Customers

-- Q2 solution
--select OrderID, OrderDate, ShipCity, ShipCountry from Orders

-- Q3 solution
--select OrderID, OrderDate, CustomerID from orders where ShipCountry = 'France'

-- Q4 solution
--select OrderID, OrderDate, CustomerID from orders where ShipCountry = 'France' or ShipCountry = 'Brazil'

-- Q5 solution
--select OrderID, OrderDate, Freight, CustomerID from orders where (ShipCountry = 'France' or ShipCountry = 'Sweden') and  Freight > 40


-- Q6 solution
--select FirstName + ' ' + LastName, Title from Employees

-- Q7 solution
--select OrderId, OrderDate, ShipName, ShipAddress, ShipCity, ShipCountry from Orders where ShipAddress like  '%box%'

-- Q8 solution
--select OrderID, CustomerID from orders where CustomerID like 'C%' and CustomerID like '%S'

-- Q9 solution
--select FirstName + ' ' + LastName from Employees where DATEDIFF(year, HireDate, GETDATE()) > 10

-- Q10 Solution
--select *, Day(ShippedDate - OrderDate) as ProcessTime from Orders

-- Q11 Solution
 --select * from Customers where Fax is null

 -- Q12 Solution
 --select * from Products where QuantityPerUnit like '%box%'