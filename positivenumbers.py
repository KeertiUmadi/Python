#Write a Python program to print all positive numbers in a range.
n = int(input("Enter number of elements : ")) 
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
print("\nList is - ", a)
print("Positive numbers are:")
for num in a:
      
    # checking condition
    if num >= 0:
        
        print(num, end = " ")
