# this first part demonstrates how to concatenate strings
string_1 = "my name"
string_2 = "is charles"
string_3 = " and my sister is called Nora"
string_4 = string_1 + string_2 + string_3
print (string_4)

# to determine the length of a string, the following code is used
print(len(string_4))

#to access a particular character in a string
#PS Python uses zero based indexing meaning characters are counted from zero
print(string_3 [3])
# in this case the output is d

# to obtain a subset of characters

print(string_3 [:5])
print(string_3 [1:5])
print(string_3 [5:])

# to repeat strings
print("Hallo" * 5)

# splitting strings
title = "Moonwalking with Einstein by Joshua Foer"
print("Source string:", title)
print("Split using a space")
print(title.split(" "))
print("Split using a comma")
print(title.split(","))

#counting strings
#use count() method
my_string = "Count, the number of     spaces"
print("my_string.count(""): ", my_string.count(" "))
# this indicates that there are 8 spaces in the original string

#replacing strings
#use the replace() method
welcome_message = "Hello Charles, welcome to the future"
print(welcome_message)
print("No, wait, there is something wrong with this message")
print(welcome_message.replace("Hello", "Master"))

#finding substrings
print(string_1.find("name"))

#converting other data types into strings


