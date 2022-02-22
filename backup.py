
# Chromosome: Binary, 32-bit
# Populasi: 8 Chromosome
# dengan Batasan −1 ≤ 𝑥 ≤ 2 dan −1 ≤ 𝑦 ≤ 1.

import random
import math

# Tasks

# Inisialisasi (check)

def initialization(population): 
    for i in range (8):
        chromosome = []
        for j in range (32):
            chromosome.append(random.randint(0, 1)) # 1,0,1,0
        population.append(chromosome)

# Dekode Kromosom 

def decodeX(chromosome):
    temp_sum = 0
    temp_2i = 0
    for i in range(16):
        temp_sum = temp_sum + chromosome[i]*(2**(-(i+1)))
        temp_2i = temp_2i + 2**(-(i+1))
    x = -1 + (3/temp_2i)*(temp_sum)
    return x

def decodeY(chromosome):
    temp_sum = 0
    temp_2i = 0
    for i in range(16):
        temp_sum = temp_sum + chromosome[i+16]*(2**(-(i+1)))
        temp_2i = temp_2i + 2**(-(i+1))
    y = -1 + (2/temp_2i)*(temp_sum)
    return y

# Perhitungan Fitness

def calculateFitness(x1, y1): # (cos𝑥2∗sin𝑦2)+(𝑥+𝑦)
    fitness = (math.cos(x1**2))*(math.sin(y1**2)) + x1 + y1
    return fitness

# Seleksi dengan turnamen

def tournamentSelection(fitness1_tmp, population_tmp, parent):
    Max = fitness1_tmp.index(max(fitness1_tmp))
    elite = population_tmp[Max]
    parent.append(population_tmp[Max])
    fitness1_tmp.pop(Max)
    population_tmp.pop(Max)
    return fitness1_tmp, population_tmp, parent, elite

# Cross-over

def crossOver(parent1, parent2):
    # temp1 = []
    # temp2 = []
    # temp1 = parent1
    chromosome_tmp1 = parent1.copy()
    chromosome_tmp2 = parent2.copy()
    for i in range(16):
        # temp1[i] = chromosome_tmp1[i]
        # temp1[i+3]
        temp = chromosome_tmp1[i+16]
        chromosome_tmp1[i+16] = chromosome_tmp2[i+16]
        chromosome_tmp2[i+16] = temp
    return chromosome_tmp1, chromosome_tmp2

# Mutate

def mutate(chromosome):
    mutationIndex = []
    for i in range(32):
        x = random.randint(0, 9)
        mutationIndex.append(x)
    y = random.randint(0, 19)
    if y == 9:
        if(chromosome[mutationIndex.index(max(mutationIndex))] == 0):
            chromosome[mutationIndex.index(max(mutationIndex))] = 1
        elif (chromosome[mutationIndex.index(max(mutationIndex))] == 1):
            chromosome[mutationIndex.index(max(mutationIndex))] = 0
        # print("Mutation occured\n")
    # else:
        # print("Mutation doesnt occur\n")

# Main

if __name__ == "__main__": 
    population = [] # 11011, ...
    chromosome = [] # 1,1,0,..
    x1 = []
    y1 = []
    fitness1 = []
    parent = []
    child = []
    elites = []
    
    # print("\nInisialisasi\n")
    initialization(population)
    #disini gan
    for u in range(2000):
        x1 = []
        y1 = []
        fitness1 = []
        parent = []
        child = []
        elites = []
        elite = []
        for i in range(8):
            x1.append(decodeX(population[i]))
            y1.append(decodeY(population[i]))
            fitness1.append(calculateFitness(x1[i], y1[i]))
            # print("Populasi ke {} : {}\n".format(i+1,population[i]))
            # print("Nilai Dekode x : {}, Nilai Dekode y : {}\n".format(x1[i], y1[i]))
            # print("Fitness : {}\n".format(fitness1[i]))

        print("\nMax Fitness: {}\n".format(max(fitness1)))
        # print("\nGenotipe Max: {}\n".format(population[fitness1.index(max(fitness1))]))
        print("\nX: {}".format(x1[fitness1.index(max(fitness1))]))
        print("\nY: {}".format(y1[fitness1.index(max(fitness1))]))
        print("\nGenerasi: {}\n".format(u+1))
        
        fitness1_tmp = fitness1.copy()
        population_tmp = population.copy()

        # print("\nSeleksi Parent\n")
        for i in range(8):
            fitness1_tmp, population_tmp, parent, elite = tournamentSelection(fitness1_tmp, population_tmp, parent)
            if i <= 1:
                elites.append(elite)
            # if i <= 5:
                # print("Parent ke {} : {}\n".format(i+1,parent[i]))

        # print("\nMating Pool\n")
        tmp_1 = []
        tmp_2 = []
        for i in range(3):
            x = random.randint(0, 5-(2*i))
            y = random.randint(0, 5-(2*i))
            while(x == y):
                x = random.randint(0, 5-(2*i))
                y = random.randint(0, 5-(2*i))
            # print("Parent yang akan dicrossover berupa \n{} \ndan \n{}\n".format(parent[x],parent[y]))
            child1, child2 = crossOver(parent[x], parent[y])
            child.append(child1)
            child.append(child2)
            parent.pop(x)
            if y > x:
                parent.pop(y-1)
            else:
                parent.pop(y)
            tmp_1 = []
            tmp_2 = []

        # print("Hasil mating pool:\n")
        # for i in range(6):
            # print("Child ke-{}: {}\n".format(i+1, child[i]))

        # print("\nMutasi\n")
        for i in range(6):
            mutate(child[i])

        # print("Hasil mutasi:\n")
        #for i in range(6):
            # print("Child ke-{}: {}\n".format(i+1, child[i]))

        # print("\nElitisme: \n{} dan \n{}\n".format(elites[0], elites[1]))

        population[0] = elites[0]
        population[1] = elites[1]
        for i in range(6):
            population[i+2] = child[i]

        # print("\nGenerasi baru:\n")
        # for i in range(8):
            # print("Kromosom {}: {}\n".format(i+1, population[i]))

        
        for i in range(8):
            fitness1[i] = calculateFitness(decodeX(population[i]), decodeY(population[i]))
        # print(fitness1)