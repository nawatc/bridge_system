def generate_desk():
    num = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
    suit = ["s","h","d","c"]
    desk = []

    for i in suit:
        for j in num:
            desk.append(j+i)
    
    return desk
            


def comb(sofar, rest, n):
    global seed
    global output

    if n == 0:
        #print (sofar)
        
        seed = seed - 1
        if seed == 0 :
            print("yes " + sofar)
            #output = sofar
            #return sofar
            

    else:
        for i in range(len(rest)):
            comb(sofar + rest[i], rest[i+1:], n-1)
            if seed == 0 :
                break
            



#comb("", "abcdef", 3)
global seed
global output
seed = 7096896423093986807593535793
output = ""

comb("", generate_desk(), 13)