# sort by key

dict = {
    'j': 1,
    'd': 2,
    'k': 3,
}
print(sorted(dict.items(), reverse = True))

reverse_map_tuple_list = []
# sort by value, highest first
for k, v in dict.items():
    reverse_map_tuple_list.append((v,k))

# 1:
# reverse_map_tuple_list.sort()
# reverse_map_tuple_list.reverse()

# 2:
# reverse_map_tuple_list = sorted(reverse_map_tuple_list, reverse = True)

# 3 and the one to rule them all
reverse_map_tuple_list = sorted([ (v, k) for k, v in dict.items() ], reverse = True)

print(reverse_map_tuple_list)