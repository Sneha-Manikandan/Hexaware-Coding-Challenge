CREATE TABLE Product (
    productId INT PRIMARY KEY ,
    productName VARCHAR(255) NOT NULL,
    description TEXT,
    price FLOAT NOT NULL,
    quantityInStock INT NOT NULL,
    type VARCHAR(50) CHECK (type IN ('Electronics', 'Clothing'))
);

CREATE TABLE Electronics (
    productId INT,
    brand VARCHAR(255),
    warrantyPeriod INT,
    FOREIGN KEY (productId) REFERENCES Product(productId)
);

CREATE TABLE Clothing (
    productId INT,
    size VARCHAR(50),
    color VARCHAR(50),
    FOREIGN KEY (productId) REFERENCES Product(productId)
);

CREATE TABLE [User] (
    userId INT PRIMARY KEY ,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) CHECK (role IN ('Admin', 'User'))
);


CREATE TABLE [Order] (
    orderId INT PRIMARY KEY ,
    userId INT,
	productId INT,
    FOREIGN KEY (userId) REFERENCES [User](userId),
	FOREIGN KEY (productId) REFERENCES [Product](productId)
);

INSERT INTO Product (productId,productname, description, price, quantityInStock, type) VALUES
(1,'Laptop', 'High performance laptop', 999.99, 50, 'Electronics'),
(2,'Smartphone', 'Latest model smartphone', 699.99, 150, 'Electronics'),
(3,'T-Shirt', 'Comfortable cotton t-shirt', 19.99, 200, 'Clothing'),
(4,'Jeans', 'Stylish blue jeans', 49.99, 100, 'Clothing'),
(5,'Headphones', 'Noise-cancelling headphones', 199.99, 75, 'Electronics');


INSERT INTO Electronics (productId, brand, warrantyPeriod) VALUES
(1, 'Dell', 24),
(2, 'Samsung', 12),
(5, 'Sony', 18);


INSERT INTO Clothing (productId, size, color) VALUES
(3, 'L', 'White'),
(4, '32', 'Blue');


INSERT INTO [User] (userId,username, password, role) VALUES
(1,'admin1', 'password123', 'Admin'),
(2,'user1', 'password123', 'User'),
(3,'user2', 'password123', 'User'),
(4,'admin2', 'password123', 'Admin'),
(5,'user3', 'password123', 'User');


INSERT INTO [Order] (orderid,userId, productId) VALUES
(1,2, 1),
(2,2, 3),
(3,3, 2),
(4,4, 4),
(5,5, 5);

Select productid FROM [order] where userId = 5 group by productid