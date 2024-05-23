# List menjadi Set
list_data = [1, 2, 3, 4, 5, 1, 2]
print("List sebelum konversi:", list_data)

set_data_from_list = set(list_data)
print("Set setelah konversi dari List:", set_data_from_list)

# Set menjadi List
set_data = {1, 2, 3, 4, 5}
print("Set sebelum konversi:", set_data)

list_data_from_set = list(set_data)
print("List setelah konversi dari Set:", list_data_from_set)

# Tuple menjadi Set
tuple_data = (1, 2, 3, 4, 5, 1, 2)
print("Tuple sebelum konversi:", tuple_data)

set_data_from_tuple = set(tuple_data)
print("Set setelah konversi dari Tuple:", set_data_from_tuple)

# Set menjadi Tuple
set_data_for_tuple = {1, 2, 3, 4, 5}
print("Set sebelum konversi:", set_data_for_tuple)

tuple_data_from_set = tuple(set_data_for_tuple)
print("Tuple setelah konversi dari Set:", tuple_data_from_set)