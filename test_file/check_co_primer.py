# Python program to check Co-Prime Number
# https://www.codesansar.com/python-programming-examples/check-co-prime-numbers.htm#:~:text=This%20python%20program%20checks%20whether,1%20are%20co%2Dprime%20numbers.
# Function to check Co-prime

# Record : 6558.0M cal.

def get_num_from_txt():
    f = open("coprime_record.txt", "r")
    return int(f.read())

def set_num_from_txt(num):
    f = open("coprime_record.txt", "w")
    f.write(str(num))

# Python program to check Co-Prime Number

# Function to check Co-prime
def are_coprime(a,b):
    
    hcf = 1

    #for i in range(get_num_from_txt(), a+1):
    for i in range(1, a+1):
        if a%i==0 and b%i==0:
            hcf = i

        # Add 
        """if i % 1000000 == 0 :
            print(i)
            set_num_from_txt(i)"""
            
    return hcf == 1

# Reading two numbers
# 53644 737765 488792 839237 440000
first = 11 #6377153 
second = 53644737765488792839237440000

if are_coprime(first, second):
    print('%d and %d are CO-PRIME' %(first, second))
else:
    print('%d and %d are NOT CO-PRIME' %(first, second))



