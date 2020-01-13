# ================= Compulsory Task 2 ==================
# Create a Python file called “holiday.py” in this folder.
# You will need to to create four functions:
#   - Hotel cost - This function will take the number of nights as an argument and return a total cost (You can choose the price per a night)
#   - Plane cost - This function will take the city you are flying to as an argument and return a cost for the flight (Hint: use if/else if statements in the function to retrieve a price based on the chosen city)
#   - Car rental - This function will take the number of days  as an argument and return the total cost.
#   - Holiday cost - This function will take three arguments, number of nights, city, and days.
#     Using these three arguments, you can call all three of the above functions with respective arguments and finally return a total cost for your holiday.
# Print out the value of your Holiday function to see the result!
# Try using your app with different combinations to show it’s compatibility with different options


def hotel_cost():
    how_long_hotel = int(input('How many nights will you spend at a hotel?\n'))          # Using the input with in the function so that it only works with in this function
    night_cost = how_long_hotel * 1200                                                   # Calculating the total cost for all nights stayed
    print('The total cost of your stay is:\n', night_cost)
    return night_cost                                                                    # Recalling the amount

def plane_cost():
    price = 0
    places = {'1': 'Cape Town', '2': 'Durban', '3': 'Johannesburg', '4': 'Port Elizabeth', '5': 'Pretoria'}                 # Dictionary of places 
    where_to =  input('Where would you like to fly to \n' + str(places) + ' \nPlease choose the corresponding number:\n')   # Selecting a place to travel to
    if where_to == '1':
        places = places['1']
        price = 2800
    elif where_to == '2':
        places = places['2']
        price = 2900
    elif where_to == '3':
        places = places['3']
        price = 4600
    elif where_to == '4':
        places = places['4']
        price = 2200
    elif where_to == '5':
        places = places['5']
        price = 3800
    print('You will be travelling to ' + str(places) + ' For the price of R' + str(price) + '\n')                        # Showing the place and price that was chosen
    return price
    return places
def car_rental():
    how_long_car = int(input('For how long (in days) will you be renting the car?\n'))                                   # Using the input with in the function so that it only works with in this function
    total_days = how_long_car * 450                                                                                      # Calculating the total cost
    print('It will be R' + str(total_days) + ' to use the car for ' + str(how_long_car) + ' days.\n')
    return total_days

def holiday_cost():
    grand_total = hotel_cost() + plane_cost() + car_rental()                                                            # Calcualting the total cost of the holiday
    print('The total cost of your holiday is R' + str(grand_total))
    return grand_total   
#Running Main Program
main_program = holiday_cost()
