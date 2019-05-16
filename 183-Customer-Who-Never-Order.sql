Select Customers.Name AS Customers from Customers left JOIN Orders ON Customers.ID = Orders.CustomerID where Orders.CustomerId is null
