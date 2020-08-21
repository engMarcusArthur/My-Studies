print("p  :",end="")
p=[1, 3, 2, 4, 5]
print(p)
q=[]
print("q  :",end="")
print(q)
print("Number of items:", len(p))   #  5 items
m=0   # 0 to 4
for i in range(len(p)-m):
    q.append(p.pop(m))
print("p  :",end="")
print(p)
print("q  :",end="")
print(q)
