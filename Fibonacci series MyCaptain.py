
n = int(input("Enter the number of terms: "))


a, b = 0, 1

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci series: ", a)
else:
    print("Fibonacci series:")
    print(a, b, end=" ")

    for i in range(2, n):
        next_number = a + b
        print(next_number, end=" ")
        a, b = b, next_number
