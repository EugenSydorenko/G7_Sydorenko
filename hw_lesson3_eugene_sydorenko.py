elements: list = [1, 2, 3, 4, 5, 5, 8, 7]
print('elements = ', elements)

dictionary: dict = {'salary': 100, 'bonus': 25, 'reward': 50}
print('dictionary = ', dictionary)

sum_elements = sum(elements)
print('sum_elements = ', sum_elements)

unique_elements_sum = sum(set(elements))
print('unique_elements_sum = ', unique_elements_sum)

sum_third_element_and_salary_value = elements[2] + dictionary['salary']
print('sum_third_element_and_salary_value = ', sum_third_element_and_salary_value)

sum_values = sum(dictionary.values())
print('dictionary sum = ', sum_values)

dictionary['salary'] += dictionary['reward']
print('new dictionary ', dictionary)

value = dictionary.get('key')
print(value)
