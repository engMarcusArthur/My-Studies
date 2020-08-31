lista=["abcde","bfghi"]
l1 = lista[0]
l2 = lista[1]
joined_list1 = [l1, l2]
joined_list2 = [*l1, *l2]  # unpack both iterables in a list literal
print(joined_list1)
print(joined_list2)
joined_list2.reverse()
print(joined_list2)