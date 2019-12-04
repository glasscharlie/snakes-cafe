print("**************************************")
print("**    Welcome to the Snakes Cafe!   **")
print("**    Please see our menu below.    **")
print("**")
print("** To quit at any time, type 'quit' **")
print("**************************************")

print("Appetizers")
print("----------")
print("Wings")
print("Cookies")
print("Spring Rolls")

print("Entrees")
print("-------")
print("Salmon")
print("Steak")
print("Meat Tornado")
print("A Literal Garden")

print("Desserts")
print("--------")
print("Ice Cream")
print("Cake")
print("Pie")

print("Drinks")
print("------")
print("Coffee")
print("Tea")
print("Unicorn Tears")

print("***********************************")
print("** What would you like to order? **")
print("***********************************")

order = {
    'wings' : 0,
    'cookies' : 0,
    'spring rolls' : 0,
    'salmon' : 0,
    'steak' : 0,
    'meat tornado' : 0,
    'a literal garden' : 0,
    'ice cream' : 0,
    'cake' : 0,
    'pie' : 0,
    'coffee' : 0,
    'tea' : 0,
    'unicorn tears' : 0
}

while True:
    response = input('Choice: ')
    if response == 'quit':
        break
    if response.lower() in order:
        order[response.lower()] += 1
        if order[response.lower()] == 1:
            print('**', f'1 order of {response} has been added to your meal', '**')
        else:
            print('**', f'{order[response.lower()]} orders of {response} have been added to your meal', '**')    