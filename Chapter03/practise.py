# Name=input("Enter your name: ")#taking input from the user and store it in the variable name
# print(f"Good Afternoon MR. : {Name}")#f string is used to format the string and print the value of the variable name in the string
#Problem no 02 Where print the date ,name in the sequence 
# Prbleem is to print the name and date and print the message that your selected 
letter='''Dear <|Name|> ' 
'Your selected ' 
'Date <|Date|>'''
print(letter.replace("<|Name|>","Ali Hamza").replace("<|Date|>","20th June 2024"))
#replace method is used to replace the value of the variable name and date in the string
reverse="Hamza"
print(reverse[::-1])#reverse the string using slicing