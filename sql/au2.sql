CREATE TABLE Employee(
    ID int NOT NULL PRIMARY KEY,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int
); 

INSERT into Employee(ID, LastName, FirstName, Age)
VALUES(1, 'kusar', 'rajhans', 23)

SELECT * from Employee; 



