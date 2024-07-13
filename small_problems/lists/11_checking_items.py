grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

grocery_list_copy = list(grocery_list)

for item in grocery_list_copy:
    print(item)
    grocery_list.remove(item)

print(grocery_list)