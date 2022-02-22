import random
import math

# Constraint / limit
global rb_x
rb_x = -1 # upper limit of x
global ra_x
ra_x = 2 # lower limit of x

global rb_y
rb_y = -1 # upper limit of y
global ra_y
ra_y = 1 # lower limit of y


# Abbrevation
# sizep -> population size
# sizeg -> genotype size
# arrp -> array of population
# arrc -> array of chromosome
# x -> formula of x for decoding
# y -> formula of y for decoding
# d_x -> value decode x
# d_y -> value decode y
# lstd_x -> list of x decoded
# lstd_y -> list of y decoded
# lst_fit -> list of fitness
# fitx -> list of fitness x
# fixy -> list of fitness y



# Initialization function
def initialize(sizep, sizeg):
    arrp = []
    for i in range(sizep): 
        arrc = []
        for j in range(sizeg):
            arrc.append(random.randint(0,1))
        arrp.append(arrc)
    return arrp, arrc


# Decode function
def decodex(sizeg, arrc):
    temp_a = 0
    temp_b = 0
    for i in range(int(sizeg/2)):
        temp_a = temp_a + 2**(-(i+1))
        temp_b = temp_b + arrc[i]*(2**(-(i+1)))
    x = rb_x + ((ra_x - rb_x) / (temp_a)) * (temp_b)
    return x


def decodey(sizeg, arrc):
    temp_a = 0
    temp_b = 0
    for i in range(int(sizeg/2)):
        temp_a = temp_a + 2**(-(i+1))
        temp_b = temp_b + arrc[i+(int(sizeg/2))]*(2**(-(i+1)))
    y = rb_y + ((ra_y - rb_y) / (temp_a)) * (temp_b)
    return y


# Fitness
def fitness(lx, ld):
    fit = (math.cos(lx**2))*(math.sin(ld**2)) + lx + ld
    return fit


if __name__ == "__main__":
    # Pick size
    print("Input the size for it population : ", end = "")
    sizep = int(input())
    while(sizep == 0):
        print("Incorrect, input the correct size for it population (can't be null) : ", end = "")
        sizep= int(input())
    print("Input the size for it genotype (must be odd numbers) : ", end = "")
    sizeg = int(input())
    while(sizeg % 2 == 1 or sizeg == 0):
        print("Incorrect, input the correct size for it genotype (must be odd numbers and cant be null) : ", end = "")
        sizeg = int(input())

    # Initialitating
    print("")
    arrp, arrc = [], [] 
    arrp, arrc = initialize(sizep, sizeg)
    for i in range(sizep):
        print("Parent {} :,".format(i+1), arrp[i])

    # Decoding
    print("")
    lstd_x = []
    lstd_y = []
    for i in range(sizep):
        d_x = decodex(sizeg, arrp[i])
        lstd_x.append(d_x)
        d_y = decodey(sizeg, arrp[i])
        lstd_y.append(d_y)
        print("For chromosome {}, decode value x :".format(i+1), d_x)
        print("For chromosome {}, decode value y :".format(i+1), d_y)
        print("")


    # Fitnessing
    lst_fit = []
    for i in range(sizep):
        lst_fit.append(fitness(lstd_x[i], lstd_y[i]))
        print("For population {} value of it fitness :".format(i+1), lst_fit[i])


    # Selectioning

