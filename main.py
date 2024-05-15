from Entity import Product,User
from DAO import OrderProcessor


class OrderManagement:
    order_processor=OrderProcessor()
    def main(self):
        while True:
                print("""
                    1. Create User
                    2. Create Product
                    3. Create Order
                    4. Cancel Order
                    5. Get All Products
                    6. Get Orders by User
                    7. Exit
                    """)
                choice=int(input("Please choose what you want to do: "))
                if choice == 1:
                    userId = int(input("Enter User ID: "))
                    username = input("Enter Username: ")
                    password = input("Enter Password: ")
                    role = input("Enter Role (Admin/User): ")
                    user = User(userId, username, password, role)
                    self.order_processor.createUser(user)

                elif choice == 2:
                    user_id = int(input("Enter User ID: "))
                    product_id = int(input("Enter Product ID: "))
                    productName = input("Enter Product Name: ")
                    description = input("Enter Product Description: ")
                    price = float(input("Enter Product Price: "))
                    Quantity = int(input("Enter Product Quantity: "))
                    productType = input("Enter Product Type (Electronics/Clothing): ")
                    product = Product(product_id, productName, description, price, Quantity, productType)
                    self.order_processor.createProduct(user_id, product)

                elif choice == 3:
                    userId = int(input("Enter User ID: "))
                    productId = int(input("Enter Product ID (0 to finish): "))
                    self.order_processor.createOrder(userId, productId)

                elif choice == 4:
                    userId = int(input("Enter User ID: "))
                    orderId = int(input("Enter Order ID: "))
    
                    self.order_processor.cancelOrder(userId, orderId)

                   
                elif choice == 5:
                    self.order_processor.getAllProducts()

                elif choice == 6:
                    userId = int(input("Enter User ID: "))  # userid 2 has 1,3 product
                    self.order_processor.getOrderByUser(userId)
        
                elif choice == 7:
                    print("Thank You !! Exiting...")
                    main_menu.order_processor.close()
                    break
                else:
                    print("Invalid choice. Please try again.")



if __name__=="__main__":
    print("WELCOME TO ORDER MANAGEMENT")
    main_menu=OrderManagement()
    main_menu.main()