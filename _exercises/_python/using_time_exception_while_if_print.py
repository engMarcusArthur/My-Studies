#An exercise using exception dealing, laces 'while', condicional 'if' and 'print' with time argument
import time
print("Type 1 to program wait three seconds and print 'The End' or 2 to print a message first and end in three seconds")
esp=int(0)
while esp!=1 and esp!=2:
    while True:#this lace is just to avoid of typing nothing or something invalid
        try:
            esp=int(input("-->"))#An atribution to integer must to be forced, because python understands the input as a string
            break #If a valid value was typed, so go ahead
        except ValueError:
            print("Oops!  You must to type something valid.  Try again...")
    if esp==1:#as a number non-decimal on the code, python understands as an integer (and not a string).
        print('The End', end='')
    elif esp==2:
        print('The program is ending...', end='', flush=True)
    else:
        print("... Please, type 1 or 2 and Enter! Thank you!!")
time.sleep(3) #three seconds