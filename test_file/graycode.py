def Deci_to_GrayCode(n):
 
    # Right Shift the number
    # by 1 taking xor with
    # original number
    return n ^ (n >> 1)
 
def GrayCode_to_Deci(n):
    inv = 0
     
    # Taking xor until
    # n becomes zero
    while(n):
        inv = inv ^ n
        n = n >> 1
    return inv

def Deci_to_Bin(n):
    return bin(n)
"""
def Bin_to_Deci(n):
    return "{0:b}".format(int(n))"""

#print(Deci_to_GrayCode(53644737765488792839237440000))

print(Deci_to_Bin(77989101499986644278505822976))

#print(b'ob101')


# Driver Code
#n = 10
#print(Deci_to_GrayCode(n))


"""n = 3

a = Deci_to_Bin(n)
print(Deci_to_Bin(n))

print(Bin_to_Deci(a))
b = a"""


