filename = "" #"coprime_record.txt"

def get_num_from_txt():
    f = open(filename, "r")
    return int(f.read())

def set_num_from_txt(num):
    f = open(filename, "w")
    f.write(str(num))

def cycle_one_step(seed: int, sample_size: int, increment: int):
    nb = seed
    nb = (nb + increment) % sample_size
    return nb


while(1):
    number = cycle_one_step(seed = get_num_from_txt() ,sample_size = 53644737765488792839237440000 ,increment = 11)
    print(number)
    #set_num_from_txt(number)