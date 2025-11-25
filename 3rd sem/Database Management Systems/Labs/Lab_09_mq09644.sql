-- Q1
insert into Products(ProductName, CategoryID, UnitPrice)
values ('Coca Cola', 1, 90)
--select * from Products

-- Q2
insert into Products(ProductName, CategoryID, UnitPrice)
values ('Fish', 8, 50)
--select * from Products

-- Q3
update Products
set UnitPrice = UnitPrice * 1.25
where CategoryID = (select CategoryID from Categories where CategoryName = 'Confections')
--select * from Products

-- Q4
insert into Categories (CategoryName)
values ('Drinks')
--select * from Categories

-- Q5
insert into Products (ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued)
select ProductName, SupplierID, (select CategoryID from Categories where CategoryName = 'Drinks'), QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued
from Products
where CategoryID = (select CategoryID from Categories where CategoryName = 'Beverages')
--select * from Products

-- Q6
update Categories
set CategoryName = 'Drinks'
where CategoryName = 'Beverages'
--select * from Categories

-- Q7
delete from EmployeeTerritories
where EmployeeID = (select EmployeeID from Employees where FirstName = 'Robert' and LastName = 'King')

insert into EmployeeTerritories(EmployeeID, TerritoryID)
select (select EmployeeID from Employees where FirstName = 'Robert' and LastName = 'King'), TerritoryID from EmployeeTerritories
where EmployeeID = (select EmployeeID from Employees where FirstName = 'Andrew' and LastName = 'Fuller')

-- Q8
delete from Products
where CategoryID = 8 and UnitsInStock < 5

-- Q9
delete from [Order Details]
where OrderID in (select OrderID from Orders where CustomerID = 'Chops')

delete from Orders
where CustomerID = 'CHOPS'
--select * from Orders where CustomerID = 'CHOPS'

-- Q10
delete from [Order Details]
where OrderID in (select OrderID from Orders where year(ShippedDate) = 1998 and month(ShippedDate) = 4)

delete from Orders
where year(ShippedDate) = 1998 and month(ShippedDate) = 4