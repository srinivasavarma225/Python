m = int(input("Marks in Math: "))
s = int(input("Marks in Science: "))
e = int(input("Marks in English: "))

total = m + s + e
average = total / 3

percentage = (total / 300) * 100
grade = ""
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
else:
    grade = "P"

print(f"Total Marks: {total} \n Average Marks: {average} \n Grade: {grade}")
