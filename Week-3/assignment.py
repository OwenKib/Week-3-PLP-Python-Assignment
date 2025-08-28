def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

if __name__ == "__main__":
    while True:
        try:
            original_price_input = input("Enter the original price of the item: ")
            discount_percent_input = input("Enter the discount percentage: ")

            original_price = float(original_price_input)
            discount_percentage = float(discount_percent_input)

            if original_price < 0 or discount_percentage < 0:
                print("Invalid input. Please enter non-negative values for price and discount.")
                continue

            # Calculate the final price using the function
            final_price = calculate_discount(original_price, discount_percentage)

            # Print the result
            if discount_percentage >= 20:
                print(f"A {discount_percentage:.2f}% discount was applied.")
                print(f"The final price is ${final_price:.2f}.")
            else:
                print("No discount was applied.")
                print(f"The final price is ${final_price:.2f}.")
            break 
            
        except ValueError:
            print("Invalid input. Please enter numeric values for price and percentage.")