#Date:19.03.2023
#Topic: String Slicing

    # Slicing only works for sequence types including mutable and immutable sequences.
    # A slice is an object the slice type.
    
    
# +---+---+---+---+---+---+---+---+---+---+---+---+---+
# | P | y | t | h | o | n |   | S | t | r | i | n | g | 
# +---+---+---+---+---+---+---+---+---+---+---+---+---+
#   0   1   2   3   4   5   6   7   8   9   10  11  12
# -13  -12  -11  -10 -9  -8  -7  -6  -5  -4  -3  -2  -1 

string = "hello python"
print(string[0:2])


# string[start:end:step]
# The substring always includes the character at the start and excludes the string at the end.

# Python strings are immutable. It means that you cannot change the string.
#Example:
# str = "Python String"
# str[0] = 'J'
#throw a error

# solution:
str = "Python String"
new_str = 'J' + str[1:]
print(new_str)

#Negative Indexing
string = "hello python"
print(string[-12:-10])


#Reverse a String
print(string[::-1])