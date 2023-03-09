def apt_search1(city, max_rent, min_beds, pets_allowed):
    if pets_allowed:
        print(f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments that allow pets, all within a budget of {max_rent} per month... ')
    else:
        print(f'Welcome to GC Property Managment! Looking up listing in {city} for {min_beds} bedroom apartments, all within a budget of {max_rent} per month...')

result = apt_search1('Detroit', 1200, 2, False)
print(result)

def apt_search2(city, max_rent, min_beds = 2, pets_allowed = True):
    if pets_allowed:
        print(f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments that allow pets, all within a budget of {max_rent} per month... ')
    else:
        print(f'Welcome to GC Property Management! Looking up listing in {city} for {min_beds} bedroom apartments, all within a budget of {max_rent} per month...')

apt_search2('Detroit', 2000)
apt_search2('Detroit', 2000, min_beds=3)
apt_search2('Ann Arbor', 2000, pets_allowed=False)

plus_one_hundred = lambda x: x + 100
print(plus_one_hundred(1))
square_num = lambda x: x**2
print(square_num(2))
concatenate = lambda x:  "-"+ x
print(concatenate('Romana'))
divide_by_three = lambda x: x/3
print(divide_by_three(24))


