#Write the program to store the values entered by user in a list and print the list
List=[]#Empty list
n=int(input("Enter the number of elements you want to add in the list: "))
for i in range(n) :
    element=input("Enter the element you want to add in the list: ")
    List.append(element) #Add the element to the list
print(List) #Print the list