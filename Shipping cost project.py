#define a weight variable and set it equal to any number.
def cost_to_ship_ground(weight):

#Create an if/elif/else statement for the cost of ground shipping.
  if weight <= 2:
    price_per_lbs = 1.50
  elif weight <= 6:
    price_per_lbs = 3.00
  elif weight <= 10:
    price_per_lbs = 4.00
  else:
    price_per_lbs = 4.75

  return 20 + (price_per_lbs * weight)

print(cost_to_ship_ground(41.5))

#Create a variable for the cost of premium ground shipping.
cost_to_ship_premium_ground = 125.00

print(125.00)

#Create a variable for the cost of drone shipping.
def cost_to_ship_drone(weight):

  if weight <= 2:
    price_per_lbs = 4.50
  elif weight <= 6:
    price_per_lbs = 9.00
  elif weight <= 10:
    price_per_lbs = 12.00
  else:
    price_per_lbs = 14.25

  return price_per_lbs * weight

print(cost_to_ship_drone(41.5))

#What is the cheapest method of shipping a 4.8 pound package and how much would it cost?

#What is the cheapest method of shipping a 41.5 pound package and how much would it cost?