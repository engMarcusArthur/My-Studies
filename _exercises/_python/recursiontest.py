# Using recursion to iterate
def from_to(a,b):   # Defining the function
    if a<b:
        print(a)
        a+=1
        from_to(a,b)   # The recursive calling
    else:
        print(a)

from_to(1,995)  # Calling the function
# Above 995 times -->> RecursionError: maximum recursion depth exceeded while calling a Python object
#----------------------------------------------------------------------
# But, until 995 times, does the same as:
a=1
b=995
for i in range(a, b):
    print(i+1)
