# 1.  List (Список):

# Create an empty list
my_list = []

# Add numbers to the list
my_list.append(11)
my_list.append(12)
my_list.append(13)

# Print the list
print(my_list)

# Change the second element to 15
my_list[1] = 15

# Print the updated list
print(my_list)

# Remove the third element
del my_list[2]

# Print the updated list
print(my_list)

# 2.  Tuple (Кортеж):

# Create the first tuple
my_tuple_one = (21, 22, 23)

# Print the tuple
print(my_tuple_one)

# changing second element with error
# my_tuple_one[1] = 15

# Create the tuple
my_tuple_two = (31, 32, 33)

# Merge the two tuples into a third tuple
merge_two_tuples = my_tuple_one + my_tuple_two

# Print the merged tuple
print(merge_two_tuples)

# 3.  Set (Множина):

# Create the set
my_set = {1, 2, 3, 4}

# Print the set
print(my_set)

# Adding fifth element
my_set.add(5)

# Print the result set
print(my_set)

# removing element
my_set.remove(2)

# Print the result set
print(my_set)

# 4.  Frozenset (Незмінювана множина):

# Create the first frozenset
frozenset1 = frozenset(("apple", "banana", "orange"))

# Create the second frozenset
frozenset2 = frozenset(("kiwi", "pineapple", "mango"))

# Combine the two frozensets
combined_frozenset = frozenset1.union(frozenset2)

# Print the combined frozenset
print(combined_frozenset)

# 5.  String (Рядок):

# creating string with my name
my_name = 'eugene'

print(my_name.title())

# Change the first letter to uppercase
correct_name = my_name[0].upper() + my_name[1:]

# Print the modified string
print(correct_name)

# Count the number of characters
char_count = len(correct_name)

# Print the character count
print(char_count)

# 6.  Dict (Словник):

# Create the dictionary
my_food_dict = {'vegetable': 'tomato', 'fruit': 'cherry'}

# Print the dictionary
print(my_food_dict)

# Add a new key-value pair
my_food_dict['sweets'] = 'chocolate'

# Print the updated dictionary
print(my_food_dict)

# Remove a key-value pair using del
del my_food_dict['vegetable']

# Print the updated dictionary
print(my_food_dict)