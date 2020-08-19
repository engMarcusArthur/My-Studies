# Here you can see >>>>>>>STRING METHODS<<<<<<<
# I have inserted as a learning intent a mark on each comment to easy visualization as <number_index>
# Note: be free to correct my english if identify some mistake...
# Be free to copy and spread
# https://github.com/engMarcusArthur/
txt=(input("Type a string (the 'first string') to analise code response according with the string method aplicated->")) # This will be the 'first string' mentioned all over this code.
print("<1>",txt.capitalize())	#<1>Converts the first character to upper case
print("<2>",txt.casefold())	#<2>Converts string into lower case
print("<3>This method will center the string. Type a previous lenght you want to set the string:", end='')
lenght_str=int(input("->"))
around_str=str(input("Now type what you want the first string are going to stay between ->"))
print(txt.center(lenght_str,around_str))	#<3>Returns a centered string. First argument required to the parameter. Second opcional.
print("<4>This method will count how many times a string (case sensitive) appears inside the first string. Type a string you want to know how many times it appears:", end='')
appear_str=str(input("->"))
print(txt.count(appear_str))	#<4>Returns the number of times a specified value occurs in a string
print("<5>",txt.encode(),"<---This is a encoded version. Look for UTF-8 and related to know more about.")	#<5>Returns an encoded version of the string.
print("<6>This method will verify if the first string ends with some string. Type a string to test (one test must to be as part of the first string to make sense for you):", end='')
end_string=input("->")
print(txt.endswith(end_string))	#<6>Returns true if the string ends with the specified value.
tupla=(txt,txt,txt) # Create a tuple with the firts string. 
print("It was created a tuple to use in the next samples.")
print("<7> Lets joint all the tuple's elements with an * between them. -->    ", end="")
print("*".join(tupla))	#<7>Joint the elements.
print("<8> Now lets insert tabs between them. I create the tabs and you choose the length of the tabs:", end='')
new_text=str("\t".join(tupla)) # Create a new string joining the tuple elements with tabs between them.
len_tabs=int(input("->"))
print(new_text.expandtabs(len_tabs))	#<8> Expand tabs in a string.
print("<9> I am going to told you where is the first appearance of a string you type in the first string. Type what string you want to know where it is.", end='')
where_string=input("->")
print("<9>", txt.find(where_string))	#<9>Searches the string and returns the position where it was found.
print("<10>", txt.format())	#<10>Formats specified values in a string; not explored here
# input stored in variable a. 
b="John"
c="Wick"
a = {"x":b, "y":c}
# Use of format_map() function
print("<11> {x}'s last name is {y}".format_map(a)) #<11>Formats specified values in a string
"""
print("<12>", txt.index())	#<12>Searches the string for a specified value and returns the position of where it was found
print("<13>", txt.isalnum())	#<13>Returns True if all characters in the string are alphanumeric
print("<14>", txt.isalpha())	#<14>Returns True if all characters in the string are in the alphabet
print("<15>", txt.isdecimal())	#<15>Returns True if all characters in the string are decimals
print("<16>", txt.isdigit())	#<16>Returns True if all characters in the string are digits
print("<17>", txt.isidentifier())	#<17>Returns True if the string is an identifier
print("<18>", txt.islower())	#<18>Returns True if all characters in the string are lower case
print("<19>", txt.isnumeric())	#<19>Returns True if all characters in the string are numeric
print("<20>", txt.isprintable())	#<20>Returns True if all characters in the string are printable
print("<21>", txt.isspace())	#<21>Returns True if all characters in the string are whitespaces
print("<22>", txt.istitle())	#<22>Returns True if the string follows the rules of a title
print("<23>", txt.isupper())	#<23>Returns True if all characters in the string are upper case
print("<24>", txt.ljust())	#<24>Returns a left justified version of the string
print("<25>", txt.lower())	#<25>Converts a string into lower case
print("<26>", txt.lstrip())	#<26>Returns a left trim version of the string
print("<27>", txt.maketrans())	#<27>Returns a translation table to be used in translations
print("<28>", txt.partition())	#<28>Returns a tuple where the string is parted into three parts
print("<29>", txt.replace())	#<29>Returns a string where a specified value is replaced with a specified value
print("<30>", txt.rfind())	#<30>Searches the string for a specified value and returns the last position of where it was found
print("<31>", txt.rindex())	#<31>Searches the string for a specified value and returns the last position of where it was found
print("<32>", txt.rjust())	#<32>Returns a right justified version of the string
print("<33>", txt.rpartition())	#<33>Returns a tuple where the string is parted into three parts
print("<34>", txt.rsplit())	#<34>Splits the string at the specified separator, and returns a list
print("<35>", txt.rstrip())	#<35>Returns a right trim version of the string
print("<36>", txt.split())	#<36>Splits the string at the specified separator, and returns a list
print("<37>", txt.splitlines())	#<37>Splits the string at line breaks and returns a list
print("<38>", txt.startswith())	#<38>Returns true if the string starts with the specified value
print("<39>", txt.strip())	#<39>Returns a trimmed version of the string
print("<40>", txt.swapcase())	#<40>Swaps cases, lower case becomes upper case and vice versa
print("<41>", txt.title())	#<41>Converts the first character of each word to upper case
print("<42>", txt.translate())	#<42>Returns a translated string
print("<42>", txt.upper())	#<43>Converts a string into upper case
print("<44>", txt.zfill())	#<44>Fills the string with a specified number of 0 values at the beginning
"""