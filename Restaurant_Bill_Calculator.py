# Restaurant Bill Calculator

# Define the solve function to calculate the total cost
def calculate_total_cost(meal_cost, tip_percent, tax_percent):
    # Calculate tip and tax amounts
    tip = (tip_percent / 100) * meal_cost
    tax = (tax_percent / 100) * meal_cost
    
    # Calculate the total cost of the meal
    total_cost = meal_cost + tip + tax
    
    # Print the rounded total cost
    print("Total cost of the meal:", round(total_cost))

if __name__ == "__main__":
    # Input the meal cost, tip percent, and tax percent
    meal_cost = float(input("Enter the meal cost: "))
    tip_percent = int(input("Enter the tip percentage: "))
    tax_percent = int(input("Enter the tax percentage: "))

    # Calculate and display the total cost
    calculate_total_cost(meal_cost, tip_percent, tax_percent)
