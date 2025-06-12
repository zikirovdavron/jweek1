class Product:
    id = 1

    def init(self, name, price, qwantity):
        self.id=Product.id
        self.name=name
        self.price=price
        self.qwantity=qwantity
        Product.id+=1

    def str(self):
        return f"ID: {self.id}  name: {self.name}  price: {self.price} somon || qwantity: {self.qwantity}"


class Allproduct:
    def __init__(self):
        self.list = []

    def add(self):
        name = input("Enter name of product: ")
        price = int(input("Enter price of product "))
        qwantity = int(input("Enter qwantity of product "))
        product = Product(name, price, qwantity)
        self.list.append(product)
        print("Product added succesfuly\n")

    def get(self):
        if not self.list:
            print("Doesnt exist\n")
            return
        print("list of product")
        for product in self.list:
            print(product)
        print()

    def Update(self):
        id = int(input("Enter id : "))
        for product in self.list:
            if product.id == id:
                product.name = input("New name: ")
                product.price = float(input("New  price: "))
                product.qwantity = int(input("New  qwantity: "))
                print("Product Updated succesfuly\n")
                return
        print("Product doesnt exist\n")

    def Delete(self):
        id = int(input("Enter id for delete: "))
        for product in self.list:
            if product.id == id:
                self.list.remove(product)
                print("Product deleted succesfuly\n")
                return
        print("Product doesnt exist \n")

    def Buy(self):
        id = int(input("Enter id for buy "))
        qwantity = int(input("Enter qwantity for buying: "))
        for product in self.list:
            if product.id == id:
                if product.qwantity >= qwantity:
                    All = product.price * qwantity
                    product.qwantity= qwantity
                    print(f'You bought {qwantity} x {product.name} ,price : {All} somoni shud\n')
                    return
                else:
                    print("doesnt exist such many product \n")
                    return
        print("Doesnt exist\n")




def Meny():
    all = Allproduct()
    while True:
        print("""
Menu:
1. Add product
2. Get product
3. Update product
4 .Delete product 
5. Buy product
6. Exit product
""")
        choose = input("choose your option: ")

        if choose == "1":
            all.add()
        elif choose == "2":
            all.get()
        elif choose == "3":
            all.Update()
        elif choose == "4":
            all.Delete()
        elif choose == "5":
            all.Buy()
        elif choose == "6":
            print("You exited")
            break
        else:
            print("Wrong input\n")

Meny()