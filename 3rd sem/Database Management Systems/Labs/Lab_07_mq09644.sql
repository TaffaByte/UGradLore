-- Q1
select CompanyName, count(UnitsInStock) from Suppliers 
join Products on Products.SupplierID = Suppliers.SupplierID 
Group By CompanyName 
Order by count(UnitsInStock) DESC

-- Q2
select CompanyName, CategoryName, count(DISTINCT ProductID) as NumOfProducts, avg(UnitPrice) as AvgPrice, count(UnitsInStock) as TotalUnits from Suppliers
join Products on Products.SupplierID = Suppliers.SupplierID 
join Categories on Categories.CategoryID = Products.CategoryID
Group By CompanyName, CategoryName

-- Q3
select CompanyName from Suppliers 
join Products on Products.SupplierID = Suppliers.SupplierID
group by CompanyName
Having count(ProductID) > 4

-- Q4
select RegionDescription, count(Employees.EmployeeID) from Employees
join EmployeeTerritories on EmployeeTerritories.EmployeeID = Employees.EmployeeID
join Territories on Territories.TerritoryID = EmployeeTerritories.TerritoryID
join Region on Region.RegionID = Territories.RegionID
Group by RegionDescription
Order by RegionDescription ASC

-- Q5
select OrderID, sum((UnitPrice * Quantity) - Discount) as TotalAmount from [Order Details] 
Group by OrderID

-- Q6
select CategoryName, sum(ProductID) as TotalNoOfProducts from Categories
join Products on Products.CategoryID = Categories.CategoryID
Group by CategoryName

-- Q7
select Customers.ContactName, Suppliers.CompanyName, count(Distinct [Order Details].ProductID) from Suppliers
join Products on Products.SupplierID = Suppliers.SupplierID
join [Order Details] on [Order Details].ProductID = Products.ProductID
join Orders on Orders.OrderID = [Order Details].OrderID
join Customers on Customers.CustomerID = Orders.CustomerID
Group by Customers.ContactName, Suppliers.CompanyName

-- Q8
select (FirstName + ' ' + LastName) as FullName, year(OrderDate), count(DISTINCT OrderID) from Orders
join Employees on Employees.EmployeeID = Orders.EmployeeID
Group by FirstName, LAstName, year(OrderDate)

-- Q9
select (M.FirstName + ' ' + M.LastName) as ManagedBy, (E.FirstName + ' ' + E.LastName), count(DISTINCT OrderID) from Employees as E
inner join Employees as M on E.ReportsTo = M.EmployeeID
join Orders on Orders.EmployeeID = E.EmployeeID
Group by M.FirstName, M.LastName, E.FirstName, E.LastName

-- Q10
select Region.RegionDescription, count(Employees.EmployeeID) from Region
left join Territories on Territories.RegionID = Region.RegionID
left join EmployeeTerritories on EmployeeTerritories.TerritoryID = Territories.TerritoryID
left join Employees on Employees.EmployeeID = EmployeeTerritories.EmployeeID
Group by Region.RegionDescription

-- Q11
select  (E.FirstName + ' ' + E.LastName) as Employee, C.ContactName from Employees as E
cross join Customers as c

-- Q12
select CustomerID, ContactName from Customers
order by Country, ContactName ASC

--Q13
select distinct count(Employees.EmployeeID) as Employees, count(distinct Customers.ContactName), Employees.City from Employees
left join Customers on Customers.City = Employees.City
Group by Employees.City
order by Employees.City

-- Q14
select count(EmployeeID) as [No of employees], count(C.CustomerID) as [No of Customers], E.City as [Employee City], C.City as CustomerCity
from Employees E
full outer join Customers c  on E.City = C.City
group by C.City, E.City
order by C.City,E.City


-- Q15
select o.OrderID, e.FirstName + ' ' + e.LastName as employeeFullName
from Orders o
join Employees e on o.EmployeeID = e.EmployeeID
where o.ShippedDate > o.RequiredDate

 -- Q16
select ProductID, sum(Quantity) as TotalQuantity
from [order details]
group by ProductID
having sum(Quantity) < 200

-- Q17
select CustomerID, count(OrderID) as TotalNumberOfOrders
from Orders
where OrderDate > '1996-12-31'
group by CustomerID
having count(OrderID) > 15