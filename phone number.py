names = []
phone_numbers = []
num = 10

for i in range(num):
	name = input("name : ")
	phone_number = input("phone number : ")
	names.append(name)
	phone_numbers.append(phone_number)
	
print("\nName\t\t\tphone number\n")
for i in range(num):
	print(f"{names[i]}\t\t\t{phone_numbers[i]}")
	
search_term = input("\nEnter search term : ")

print("search result : ")
if search_term in names:
	index = names.index(search_term)
	phone_number = phone_numbers[index]
	print(f"Name : {search_term}, phone number : {phone_number} ")
	
else:
	print("Name not found")
