# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))

# Run unit tests automatically
main(module='test_module', exit=False)


# -----------------------------------------------------------------------------
# ------------------------------------MY OWN CODE------------------------------
# -----------------------------------------------------------------------------

def budget_app() :
  import budget
  from budget import create_spend_chart
  
  #----------------------------------------Test 1----------------------------------------
  # food = budget.Category("Food")
  # food.deposit(1000, "initial deposit")
  # food.withdraw(10.15, "groceries")
  # food.withdraw(15.89, "restaurant and more food for dessert")
  # print(food.get_balance())
  
  # clothing = budget.Category("Clothing")
  # food.transfer(50, clothing)
  # clothing.withdraw(25.55)
  # clothing.withdraw(100)
  
  # auto = budget.Category("Auto")
  # auto.deposit(1000, "initial deposit")
  # auto.withdraw(15)
  # print(food)
  # print(clothing)
  # print(auto)
  # print(create_spend_chart([food, clothing, auto]))

  #----------------------------------------Test 2----------------------------------------
  food = budget.Category("Food")
  business = budget.Category('business')
  entertainment = budget.Category('entertainment')
  food.deposit(900, "deposit")
  entertainment.deposit(900, "deposit")
  business.deposit(900, "deposit")
  food.withdraw(105.55)
  entertainment.withdraw(33.40)
  business.withdraw(10.99)
  # create_spend_chart([business, food, entertainment])
  print(len(create_spend_chart([business, food, entertainment])))
  print(len("Percentage spent by category\n100|..........\n.90|..........\n.80|..........\n.70|....o.....\n.60|....o.....\n.50|....o.....\n.40|....o.....\n.30|....o.....\n.20|....o..o..\n.10|....o..o..\n..0|.o..o..o..\n....----------\n.....B..F..E..\n.....u..o..n..\n.....s..o..t..\n.....i..d..e..\n.....n.....r..\n.....e.....t..\n.....s.....a..\n.....s.....i..\n...........n..\n...........m..\n...........e..\n...........n..\n...........t.."))
  
  
  print(create_spend_chart([business, food, entertainment]))
  print("Percentage spent by category\n100|..........\n.90|..........\n.80|..........\n.70|....o.....\n.60|....o.....\n.50|....o.....\n.40|....o.....\n.30|....o.....\n.20|....o..o..\n.10|....o..o..\n..0|.o..o..o..\n....----------\n.....B..F..E..\n.....u..o..n..\n.....s..o..t..\n.....i..d..e..\n.....n.....r..\n.....e.....t..\n.....s.....a..\n.....s.....i..\n...........n..\n...........m..\n...........e..\n...........n..\n...........t..")
  
# budget_app()