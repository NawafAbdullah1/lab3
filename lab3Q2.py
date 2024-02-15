num_list = []

for i in range(10):
    num = float(input("Enter value {}: ".format(i + 1)))
    num_list.append(num)

largest = num_list[0]

for num in num_list:
    if num > largest:
        largest = num

print("The largest number in the list is:",largest)