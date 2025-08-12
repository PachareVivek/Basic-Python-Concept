n = input("Enter the student name: ")
studens = {"vivek":90,"mohit":50,"balwant":80,"manoj":25}
if n in studens:
    print(studens[n])
else:
    print("student not found")