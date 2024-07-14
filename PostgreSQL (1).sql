CREATE PROCEDURE sp_DailyProductSalesReport
AS
BEGIN
    SELECT 
        CONVERT(date, o.OrderDate) AS OrderDate,
        p.ProductName,
        COUNT(o.OrderID) AS QuantitySold
    FROM 
        Orders o
    INNER JOIN 
        Products p ON o.ProductID = p.ProductID
    WHERE 
        o.OrderDate >= DATEADD(day, -1, GETDATE())
    GROUP BY 
        CONVERT(date, o.OrderDate),
        p.ProductName
    ORDER BY 
        OrderDate, ProductName;
END;