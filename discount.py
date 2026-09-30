def calculate_discount(amount):
    if(amount < 5000):
        return amount*(15/100)
    else:
        return amount*(10/100)
