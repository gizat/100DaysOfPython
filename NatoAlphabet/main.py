# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# 
# print(new_list)


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name.upper() for name in names if len(name) > 4]
print(short_names)

