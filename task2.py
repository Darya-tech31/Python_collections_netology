ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

geo_id = []
for unique_list in ids.values():
    if type(unique_list) == list:
        geo_id += unique_list
    else:
        geo_id.append(unique_list)
print(set(geo_id))