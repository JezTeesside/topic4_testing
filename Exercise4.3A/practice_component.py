"""
Exercise 4.3A - Quality Review and Refactor Practice Component

This is a simple working component for a quality review exercise.

Learner instructions:
- Run the program first and record the output.
- Review the code for naming, formatting, readability and duplication.
- Run Black, Ruff or Pylint as instructed by the tutor.
- Make controlled improvements without changing the required behaviour.
- Run the same test cases again after refactoring.
"""

def process_order(customer, price, quantity, member):
    """Calculate and display order details for a customer.
 
    The function computes the order subtotal based on the item price
    and quantity. A 10% discount is applied when the subtotal exceeds
    100. An additional 5% discount is applied if the customer is a
    member. The function then prints a summary of the order, including
    the subtotal, discounts, final total, and order status.
 
    Args:
    customer (str): The customer's name.
    price (float): The price of a single item.
    quantity (int): The number of items ordered.
    member (bool): Indicates whether the customer is a member.
 
    Returns:
    None: This function does not return a value. It prints the
    order details to the console.
   """
    subtotal = price * quantity

    if subtotal > 100:
        discount = subtotal * 0.10
    else:
        discount = 0

    if member:
        member_discount = subtotal * 0.05
    else:
        member_discount = 0

    total = subtotal - discount - member_discount

    print("Customer:", customer)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Subtotal:", subtotal)
    print("Discount:", discount)
    print("Member discount:", member_discount)
    print("Final total:", total)

    if total >= 100:
        print("Order status: Standard")
    else:
        print("Order status: Small")

    print("Customer:", customer)
    print("Final total:", total)


# Test cases
process_order("Aisha", 30, 2, False)
print()
process_order("Ben", 60, 2, True)
print()
process_order("Chloe", 50, 3, False)