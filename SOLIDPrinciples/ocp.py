class Product:
    def __init__(self, price, discount_function=None):
        self.price = price
        self.discount_function = discount_function

    def get_price_with_discount(self):
        if self.discount_function:
            return self.price - self.discount_function(self.price)
        return self.price


def normal_discount(price):
    discount_percentage = 10
    return price * discount_percentage / 100


def calculate_total_price(products):

    total_price = sum(product.get_price_with_discount() for product in products)
    return total_price


# Using the calculate_total_price function with a list of products and normal discount
products = [Product(100, normal_discount), Product(50, normal_discount), Product(75)]
print("Total Price with Normal Discount:", calculate_total_price(products))



'''
Explaining how it follows the open close principle: 




The code provided follows the Open/Closed Principle (OCP) because it allows for easy extension without modifying the existing code. It achieves this by utilizing the Strategy design pattern to handle different discount strategies.

Here's how it adheres to the Open/Closed Principle:

1. **Using Function as a Strategy:** The `Product` class accepts a `discount_function` as a parameter in its constructor. This function represents the discount strategy and allows for different discount calculations. By passing different discount functions, we can apply various types of discounts to the products without modifying the `Product` class.

2. **Adding New Discount Strategies:** To introduce a new discount strategy, such as a flat discount or a percentage discount, we can define a new function for the specific discount calculation (e.g., `flat_discount`, `percentage_discount`). We can then pass these functions to the `Product` objects when creating them. This way, we extend the behavior of the `Product` class to support new discount types without changing the class's implementation.

3. **calculate_total_price Function:** The `calculate_total_price` function takes a list of `Product` objects and calculates the total price with the applied discount. It uses the `get_price_with_discount` method of each `Product` object, which, in turn, uses the provided discount function. Since the `calculate_total_price` function relies on the `get_price_with_discount` method, it doesn't need to be modified when introducing new discount strategies.

By allowing the `Product` class to accept different discount functions and using these functions to calculate discounts, the codebase remains open for extension to new discount strategies without modifying the existing code. This adherence to the Open/Closed Principle promotes a more maintainable and flexible design.



'''