#Eliminate repetitions on string; e.g. aaaaaaaaaa4444444++++ becomes a4+
def elim_ch_repet(string_to_clean):
    j=0
    stringnr=" "
    for i in string_to_clean:
        if stringnr[j]!=i:
            stringnr=stringnr+i
            j+=1
    stringnr=stringnr[1:] # to eliminate the inicial space setted on criation
    return(stringnr)
# End of function definition

# Aplication:
#------------------------------------------------------------
print("Type something with character repetition and I will eliminate the sequences of repetition.", end="")
sentence=input("->") #For example, type >aaaaaaaaaaabbbbbbbbcccccccccc                 1111111122222233<
newstring=elim_ch_repet(sentence) #call funciont sending the argument
print(newstring)
exit()
#------------------------------------------------------------
