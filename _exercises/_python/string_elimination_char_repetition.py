print("Type something with character repetition and I will eliminate the repetition.", end="")
sentence=input("->") #For example, type aaaaaaaaaaabbbbbbbbcccccccccc1111111122222233
j=0
sentence1=" "
for i in sentence:
    if sentence1[j]!=i:
        sentence1=sentence1+i
        j+=1
sentence1=sentence1[1:] # to eliminate the inicial space setted on criation
print(sentence1)
