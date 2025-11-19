# Write a program to calculate the total trip expenditure. Calculate the hotel cost per day, plane cost, price of the vehicle during the trip.

# Define a function called hotel with one parameter 'nights'

def hotel(nights):

    return nights * 2

# Define a function called plane_cost with one parameter 'city'

def plane_cost(city):

    if city.lower() == "paris":

        return 200

    elif city.lower() == "london":

        return 250

    elif city.lower() == "new york":

        return 300



# Define a function called trip_cost with parameters 'city', 'nights', and 'spending_money'

def trip_cost(city, nights, spending_money):

    return hotel(nights) + plane_cost(city) + spending_money

# Example usage:

total_cost = trip_cost("Paris", 5, 100)

print("Total trip cost:", total_cost)