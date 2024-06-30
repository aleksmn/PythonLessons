# Создайте класс Product для хранения информации о товаре с атрибутами name и price
# Создайте класс ShoppingCart для хранения товаров.
# Добавьте методы для добавления товара, удаления товара и подсчета общей стоимости товаров в корзине.
# Создайте объект cart1 и проведите операции с товарами.









class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_product(self, product):
        self.cart.append(product)

    def remove_product(self, product_name):
        for item in self.cart:
            if item.name == product_name:
                self.cart.remove(item)
                break

    def total_price(self):
        total = 0
        for item in self.cart:
            total += item.price
        return total

# Создаем несколько продуктов
product1 = Product("Laptop", 1000)
product2 = Product("Headphones", 100)
product3 = Product("Mouse", 20)

# Создаем объект корзины
cart = ShoppingCart()

# Добавляем продукты в корзину
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

# Выводим общую стоимость товаров в корзине
print("Total price in the shopping cart:", cart.total_price())

# Удаляем продукт "Mouse" из корзины
cart.remove_product("Mouse")

# Выводим общую стоимость товаров после удаления
print("Total price in the shopping cart after removing a product:", cart.total_price())
