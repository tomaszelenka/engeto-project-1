'''
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Tomáš Zelenka
email: me@tomaszelenka.cz
discord: .toze.
'''

import sys

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

dbusers = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}
lines = "-" * 23

def count_words(sel):
    words = [word.strip(".,:;") for word in TEXTS[sel].split()]
    return len(words)
    
def count_titlecase(sel):
    words = TEXTS[sel].split()
    result = [] 
    for word in words:
        if word.istitle():
            result.append(word)
    return len(result)        

def count_uppercase(sel):
    words = TEXTS[sel].split()
    result = [] 
    for word in words:
        if word.isupper() and word.isalpha():
            result.append(word)
    return len(result)    

def count_lowercase(sel):
    words = TEXTS[sel].split()
    result = [] 
    for word in words:
        if word.islower():
            result.append(word)
    return len(result) 

def count_numeric(sel):
    words = TEXTS[sel].split()
    result = [] 
    for word in words:
        if word.isdigit():
            result.append(word)
    return len(result) 

def sum_numeric(sel):
    words = TEXTS[sel].split()
    result = 0
    for word in words:
        if word.isdigit():
            result+=int(word)
    return result

def view_grafwords(sel):
    words = TEXTS[sel].split()
    result = {}
    for word in words:
        lword = len(word.strip(".,:;"))
        if lword in result:
            result[lword] +=1
        else:
            result[lword] = 1
    
    sorted_keys = sorted(result)
    sorted_result = {}
    for key in sorted_keys:
        sorted_result[key] = result[key]

    return sorted_result

input_usr = input("username:")
input_pasw = input("password:")

if input_usr in dbusers and dbusers[input_usr] == input_pasw:
     print(lines)
     print(f"Welcome to the app, {input_usr}")
     print("We have 3 texts to be analyzed.")
     print(lines)
     choice = input("Enter a number btw. 1 and 3 to select:")
     print(lines)
     
     if choice.isdigit() is not True:
         sys.exit("Your choice is not a number, terminating the program.")
     
     elif choice.isdigit() and choice not in {'1', '2', '3'}:
         sys.exit("Your choice is out of range, terminating the program.")  
     
     elif choice.isdigit() and (choice == '1' or choice == '2' or choice == '3'):
        choice = int(choice) - 1
        
        print(f"There are {count_words(choice)} words in the selected text.") 
        print(f"There are {count_titlecase(choice)} titlecase words.") 
        print(f"There are {count_uppercase(choice)} uppercase words.") 
        print(f"There are {count_lowercase(choice)} lowercase words.")
        print(f"There are {count_numeric(choice)} numeric strings.")
        print(f"The sum of all the numbers {sum_numeric(choice)}")

        grafdict = view_grafwords(choice)
        print(lines)
        print("LEN|  OCCURENCES  |NR.")
        print(lines)
        
        for i in grafdict:
                stars = "*" * grafdict[i] 
                star_width = len(stars)
                if grafdict[i] > 9:
                    star_width-=1
                nr_format = "|" + str(grafdict[i])
                formatted_output = "{:>{}}| {:<{}} {:>{}}".format(i, 3, stars, 0, nr_format, 14 - star_width)
                print(formatted_output)  

else:
    sys.exit("unregistered user or wrong password, terminating the program.")
