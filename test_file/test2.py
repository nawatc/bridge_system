import re



def storescores(num):

   hs = open("prime_save.txt","a")
   hs.write(str(num) + "\n")
   hs.close() 

def get_prime_num(line):
    f = open("P-1-10000001.txt", "r")
    input_text = f.readlines()[line-1]


    input_text.strip('\n')

    output = re.findall('\d+', input_text)

    output = output[1]
    return int(output)



def check_prime_indivi(prime):

    a = 53644737765488792839237440000.0/prime


    if a.is_integer() == True:
        print(f'{a:.20f}' + " is Integer.")
        txt = f'{a:.20f}' + " is Integer."

        storescores(txt)
    elif a.is_integer() == False:
        print(f'{a:.20f}' + " is not Integer.")
        print("and it what we looking for ...")

        txt = f'{a:.20f}' + " is not Integer." + " and it what we looking for ... is " + str(prime)
        storescores(txt)

#print(get_prime_num(2))

for i in range(1,10000001):
    prime = get_prime_num(i)
    check_prime_indivi(prime)
print("not found")

"""f = open("P-1-10000001.txt", "r")
input_text = f.readlines()[1]
print(input_text)"""