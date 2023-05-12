DECLARE @dates TABLE(dt DATE)    
DECLARE @dateFrom DATE
DECLARE @randomDays int
DECLARE @count int

SET @dateFrom = CAST(GETDATE() As Date)
SET @count = 0
WHILE(@count < 100)
BEGIN
   INSERT INTO @dates 
   SELECT @dateFrom
   SET @randomDays = ABS(CHECKSUM(NEWID()) % 7) + 2
   SET @dateFrom = DATEADD(day, @randomDays, @dateFrom)
   SET @count = @count + 1
END

SELECT * FROM @dates