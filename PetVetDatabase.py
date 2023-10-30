# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:26:57 2023

@author: Valued0
"""

#============================================================

pets = {1 : { 'Muhtar' : { 'type' : 'Dog', 'age' : 9, 'owner' : 'John' }, },
        2 : { 'Kaa' : { 'type' : 'Python', 'age' : 19, 'owner' : 'Alex'}, }, 
        3 : { 'Basia' : { 'type' : 'Cat', 'age' : 5, 'owner' : 'Geneviev'}, },
        }

#============================================================

#The number of current ID's 
n = next(reversed(pets.keys()))
#print(n)
print('Here is the current contents of our database: ')
print(pets)

#============================================================

def pet_ID(ID):

    if ID in pets.keys():
        return pets.get(ID, False)
    else:
        return False

pet_ID(1)

#============================================================

def get_suffix(age):

    if age == 1:
        return "год"
    elif age > 1 and age < 5:
        return "года"
    else:
        return "лет"
    
get_suffix(1)

#============================================================

def create(): 
    
    pet_name = input('Enter your pets name: ')
    pet_type = input('Enter your pet type: ')
    pet_age = input('Enter your pets age: ')
    pet_owner = input('Enter the pets owners name: ')
    pets[n + 1] = { pet_name : { 'type' : pet_type, 'age' : pet_age, 'owner' : pet_owner }, }
    print(pets)
    return pets


#============================================================

def read():
    
    ID = int(input("Введите ID: "))
    pet = pet_ID(ID)
    if not pet:
        print(f"Нет питомца с таким ID:{ID} ")
        return   
    key = [x for x in pet.keys()][0]
    string = f'Это {pet[key]["type"]} по кличке "{key}". Возраст питомца: {pet[key]["age"]} {get_suffix(pet[key]["age"])}. Имя владельца: {pet[key]["owner"]}.'
    print(string)
    return
#============================================================

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

#============================================================

def delete():
    
    x = int(input('Type in the ID of the animal you would like to delete: '))
    pets.pop(x, None)
    print(pets)
    
#============================================================

def pets_list():
    
    for i in pets:
        print(pets[i])
    
#============================================================        

def command():
    
    command = input('Welcome to the pet Data Base, press ''enter'' to continue.')
    while True:
        command = input('Enter one of the following commands: read, create, update, delete or stop to exit the program: ')
        if command == 'read':
            read()
#            return
        elif command == 'create':
            create()
#            break
        elif command == 'update':
            update()
#            break
        elif command == 'delete':
            delete()
#            break
        elif command == 'stop':
            print('Thank you for accessing the best pets ever database, hope to see you again soon! Stay safe!')
            break
        else:
            print('You have entered a non-exsiting command.' )
#            continue
        
#============================================================

#create()
#update()
#read()
#delete() 
#pets_list()
command()

    