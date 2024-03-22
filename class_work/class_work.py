name1 = "bolaji"
name2 = "chichi"
name3 = "dayo"

print(name1 == name2)
print(name1 < name2)
#checks the ordinal value of the character in ASCII table
print(ord('b'))
#check if a character is present in a string
print("c" in name2)
#setting a field width
print(f'[{name1:10}]')
#set to left side
print(f'[{name1:>10}]')
#set to right
print(f'[{name1:<10}')
#set to centre
print(f'[{name1:^10}]')
#concatenate Strings
print(name1 + name2 + name3)
#seperates
print(f'{name1} {name2} {name3}')
#repeats string
print(name1 * 5)
#strip off all the white space
name4 = "   moh   "
print(len(name4))
name4.strip()
print(len(name4.strip()))
#after strip
print(len(name4))
#removes the space in a collected input
name = input().strip()
#removes space from the left side
print(len(name4.lstrip()))
#change to uppercase
print(name1.upper())
#change to lowercase
print(name2.lower())
#change the first letter to capital
print(name3.capitalize())
#change tittle to capital letter
sentence = "welcome to my first"
print(sentence.title())
#capital letter
print(name2.casefold())
#counts number of character
print(sentence.count("e"))
#gets the index from the rigth
print(sentence.rindex("e"))
#gets index from left
print(sentence.index("e"))
#character checks  if its not an alphabet, the isalpha() removes it
name1.isalpha()

name = input("Enter your name: ").strip()
if name.isalpha():
    print("valid")
else:
    print("invalid name")
#validates only numerical and string
name.isalnum()

#checks your args to be only digit
name.isdigit()

#to check the functionality of a funrtion
print(help(name1.isprintable()))

#method that replaces characters
print(sentence.replace("q", "x"))

#method that splits a string, the reslt exludes the argument and then puts it in a list
print(sentence.split())

#python string joint method
name = ["don", "punta", "kolo", "obodo"]
print("-".join(name))

