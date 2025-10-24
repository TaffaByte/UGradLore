-- Q1
select TOP 1 EmployeeID from Orders where OrderDate = (select min(OrderDate) from Orders where year(OrderDate) = 1998)

-- Q2
select EmployeeID from Employees where ReportsTo = (select TOP 1 ReportsTo from Employees)

-- Q3
select Distinct EmployeeID from EmployeeTerritories 
where TerritoryID in (select TerritoryID from Territories 
where RegionID in (Select RegionID from Region where RegionDescription = 'Western' or RegionDescription = 'Eastern'))

-- Q4
select ContactName from Customers where Country = 'Germany'
union select ContactName from Suppliers where Country = 'Germany' 

-- Q5
select Top 1 ProductName, UnitPrice from Products where UnitPrice in (select Top 3 UnitPrice from Products Group by UnitPrice order by UnitPrice desc)
group by ProductName, UnitPrice order by UnitPrice asc

-- Q6
select E.EmployeeID, Case when DateDiff(year, E.HireDate, GETDATE()) > 5 THEN 3
WHEN DateDiff(year, E.HireDate, GETDATE()) between 3 and 5 THEN  2
ELSE 1
END AS SeniorityLevel from Employees E

-- Q7
select ProductName, Case when UnitPrice > 80 Then 'Costly'
when UnitPrice between 30 and 80 then 'Economical'
Else 'Cheap'
End As Types from Products

-- Q8
SELECT ProductName, CASE 
WHEN (SELECT COUNT(OrderID) FROM [Order Details] WHERE ProductID = P.ProductID AND OrderID IN (SELECT OrderID FROM Orders WHERE YEAR(OrderDate) = 1997)) >= 50 THEN 'Customer Favourite'
WHEN (SELECT COUNT(OrderID) FROM [Order Details] WHERE ProductID = P.ProductID AND OrderID IN (SELECT OrderID FROM Orders WHERE YEAR(OrderDate) = 1997)) between 30 and 49 THEN 'Trending'
WHEN (SELECT COUNT(OrderID) FROM [Order Details] WHERE ProductID = P.ProductID AND OrderID IN (SELECT OrderID FROM Orders WHERE YEAR(OrderDate) = 1997)) between 10 and 29 THEN 'on the rise'
Else 'Not Popular'
End As Trend from Products as P

-- Q9
select CustomerID, (select count(OrderID) from Orders where Orders.CustomerID = Customers.CustomerID) as OrderCount from Customers

-- Q10
select Distinct CustomerID from Orders where OrderID in (select OrderID from [Order Details] where UnitPrice > (select avg(UnitPrice) from Products))

-- Q11
select distinct ContactName from Customers 
where CustomerID in (select CustomerID from Orders 
where OrderID in (select OrderID from [Order Details] 
where ProductID in (select ProductID from Products 
where CategoryID = (select CategoryID from Products 
where ProductName = 'Chai'))))

-- Q12
select TOP 1 ContactName, (select count(OrderID) from Orders 
where Orders.CustomerID = Customers.CustomerID) as NumberOfOrders from Customers order by NumberOfOrders desc;

-- Q13
select distinct ContactName from Customers 
where CustomerID in (select CustomerID from Orders 
where OrderID in (select OrderID from [Order Details] 
where ProductID = (select top 1 ProductID from Products order by UnitPrice desc)))

-- Q14
select avg(ProductCount) as AverageProductsPerOrder from (select count(ProductID) as ProductCount from [Order Details] group by OrderID) as OrderProductCounts;

-- Q15
select CategoryName from Categories 
where CategoryID in (select CategoryID from Products group by CategoryID having avg(UnitPrice) > (select avg(UnitPrice) from Products))

-- Q16
select top 1 ProductName, UnitPrice from Products 
where UnitPrice < (select max(UnitPrice) from Products) order by UnitPrice desc;

-- Q17
select avg(OrderAmount) as AverageOrderAmount from (select o.OrderID, sum(od.UnitPrice * od.Quantity) as OrderAmount from Orders o 
join [Order Details] od on o.OrderID = od.OrderID 
where o.CustomerID in (select CustomerID from Customers 
where Country = 'France') group by o.OrderID) as CustomerOrders;
