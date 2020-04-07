# Question 1
name_file = open("name.txt", "w")
name = input("Please enter your name")
print(name, file=name_file)
name_file.close()

# Question 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Your name is ,", name)

# Question 3
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)