# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:26:57 2023

@author: Valued0
"""

pets = {1 : { 'Muhtar' : { 'type' : 'Dog', 'age' : 9, 'owner' : 'John' }, },
        2 : { 'Kaa' : { 'type' : 'Python', 'age' : 19, ' owner' : 'Alex'}, }, 
        3 : { 'Basia' : { 'type' : 'Cat', 'age' : 5, ' owner' : 'Geneviev'}, },
        }
n = next(reversed(pets.keys()))
print(n)
#print(pets)

def create():
    pet_name = input('Enter your pets name: ')
    pet_type = input('Enter your pet type: ')
    pet_age = input('Enter your pets age:')
    pet_owner = input('Enter the pets owners name: ')
    pets[n + 1] = { pet_name : { 'type' : pet_type, 'age' : pet_age, 'owner' : pet_owner }, }
    print(pets)
    return pets
create()
    
def read():
    x = int(input('Enter a number '))
    print(pets.get(x))

read()

def update():
    y = int(input("Type in the number of the pet you would like to update: "))    
    if y in pets:
        print(pets[y])
#        a = int(input('What would you like to change? type in 1 to change Type of Pet, type in 2 to change Pet Age, type in 3 to change Pet Owners Name :'))
        for a in pets[y]:
#            print(pets[y].get(a))
#            b = (input('Enter the " type " to update the type, enter " age " to update the age and " owner " for owner: '))
            for b in pets[y].get(a):
                b = (input('Enter the " type " to update the type, enter " age " to update the age and " owner " for owner: '))
                if b == 'type':
                    type_input = input('Enter the pet type: ')
                    update_info = {'type': type_input}
                    (pets[y].get(a)).update(update_info)
                    print(pets)
                    break
                if b == 'age':
                    age_input = input('Enter the new pets age: ')
                    update_info = {'age': age_input}
                    (pets[y].get(a)).update(update_info)
                    print(pets)
                    break
                if b == 'owner':
                    owner_input = input('Enter the new owners name: ')
                    update_info = {'owner': owner_input}
                    (pets[y].get(a)).update(update_info)
                    print(pets)
                    break
                else:
                    print('wrong input, try one of the three: type, name, age')

update()
        
#def delete():
    