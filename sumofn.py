num = int(input("Enter a number: "))

sum = 0
for i in range(1, num+1):
    sum = sum + i 
print(f"Sum of first {num} numbers: {sum}")