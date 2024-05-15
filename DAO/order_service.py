from Util.DBConn import DBConnection
from abc import ABC, abstractmethod

class OrderNotFound(Exception):
    def __init__(self,orderId):
        super().__init__(f"{orderId} not found")

class UserNotFound(Exception):
    def __init__(self,userId):
        super().__init__(f"{userId} not found")

class  IOrderManagementRepository:
    @abstractmethod
    def createOrder(self,user,products):
        pass

    @abstractmethod
    def cancelOrder(self,userId, orderId):
        pass

    @abstractmethod
    def createProduct(self,user,product): 
        pass

    @abstractmethod
    def createUser(self,user):
        pass

    @abstractmethod
    def getAllProducts(self):
        pass

    @abstractmethod
    def getOrderByUser(self,user):
        pass

class OrderProcessor(IOrderManagementRepository,DBConnection):

    def createOrder(self,userId,productId):
        
        self.cursor.execute("SELECT * FROM [User] WHERE userId = ?", (userId,))
        user = self.cursor.fetchall()
        
        if len(user)==0:
            self.createUser(user)

        self.cursor.execute("Insert INTO [Order] (userId,productId) VALUES (?,?)", (userId,productId))
        self.conn.commit()

 
    def cancelOrder(self,userId, orderId):
        try:
            self.cursor.execute("Select * FROM [Order] WHERE orderId = ? AND userId = ?", (orderId, userId))
            order = self.cursor.fetchall()

            if len(order)==0:
                raise OrderNotFound(orderId)
            else:
                self.cursor.execute("delete FROM [Order] WHERE orderId = ?", (orderId,))
                self.conn.commit()
        except Exception as e:
            print("Error!!", e)



    def createProduct(self,user_id,product): 
        try:
            self.cursor.execute("SELECT * FROM [User] WHERE userId = ? AND role = 'Admin'", (user_id,))
            admin = self.cursor.fetchall()
            if len(admin)==0:
                raise UserNotFound(user_id)
            else:
                self.cursor.execute("INSERT INTO Product (productid, productName, description, price, quantityInStock, type)VALUES (?, ?, ?, ?, ?, ?)", 
                                    (product.productId, product.productName, product.description, product.price, product.quantityInStock, product.type))
                self.conn.commit()
        except Exception as e:
            print("Error!!",e)
        


    def createUser(self,user):
        self.cursor.execute("Insert INTO [User] (userId, username, password, role)VALUES (?, ?, ?, ?)", (user.userId, user.username, user.password, user.role))

        self.connection.commit()


    def getAllProducts(self):
        self.cursor.execute("Select * FROM Product")
        products = self.cursor.fetchall()
        for product in products:
            print(product)


    def getOrderByUser(self,userId):
        self.cursor.execute("Select Productid FROM [Order] where userId = ? group by productid", (userId))
        products = self.cursor.fetchall()
        if len(products)==0:
            print(f"No orders made by user {userId}")
        else:
            for product in products:
                print(product)



         