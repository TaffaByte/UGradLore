-- Q1
select count(*) from customers where Fax is Null

-- Q2
select count(*) from Orders where year(OrderDate) = 1997

-- Q3
select count(*) from customers where ContactTitle = 'Sales Representative'

-- Q4
select sum(Quantity) from [Order Details] where OrderID = 11070

-- Q5
select count(CustomerID) from Customers where Country = 'UK' or Country = 'USA'

-- Q6
select sum(UnitsInStock) from Products

-- Q7
select sum(UnitsInStock * UnitPrice) from Products

-- Q8
select count(employeeID) from Employees where City = 'London'

-- Q9
select count(EmployeeID) from Employees where (TitleOfCourtesy = 'Ms.' or TitleOfCourtesy = 'Mrs.') and Title <> 'Doctor'

-- Q10
select Orders.OrderID, Orders.OrderDate, Products.ProductName from Orders 
Inner join [Order Details] on Orders.OrderID = [Order Details].OrderID 
Inner join Products on [Order Details].ProductID = Products.ProductID

-- Q11
select Orders.OrderID, Orders.OrderDate, Products.ProductName, Customers.ContactName from Orders 
Inner join [Order Details] on Orders.OrderID = [Order Details].OrderID 
Inner join Products on [Order Details].ProductID = Products.ProductID
Inner join Customers on Orders.CustomerID = Customers.CustomerID

-- Q12
select Orders.OrderID, Orders.OrderDate, Products.ProductName, Categories.CategoryName from Orders 
Inner join [Order Details] on Orders.OrderID = [Order Details].OrderID 
Inner join Products on [Order Details].ProductID = Products.ProductID
Inner join Categories on Products.CategoryID = Categories.CategoryID
where Categories.CategoryName = 'Seafood'

-- Q13
select Customers.CustomerID, Customers.ContactName from Customers
left outer join Orders
on Customers.CustomerID = Orders.CustomerID
where Orders.CustomerID is null 

-- Q14
select distinct [Order Details].OrderID, Products.ProductName, Categories.CategoryName from Products
Inner join [Order Details] on Products.ProductID = [Order Details].ProductID
Inner join Categories on Products.CategoryID = Categories.CategoryID
where Categories.CategoryName = 'Meat/Poultry' or Categories.CategoryName = 'Dairy Products'

-- Q15
select concat(Employees.FirstName, ' ', Employees.LastName), Customers.ContactName from Customers cross join Employees