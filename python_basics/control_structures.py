num = int(input("Enter Number: "))

def even_or_odd(num):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

even_or_odd(num)

# For loop creating list of even numbers
lst = list()
def even(num):
    if num % 2 == 0:
        lst.append(num)

for i in range(1, 51):
    even(i)

print(lst)

# while loop that prints numbers from 10 to 1 
curr = 10
while curr > 0:
    print(curr)
    curr -= 1   

