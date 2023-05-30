

import random

def fitness_calc(list):
    length = len(list)
    arr =[ [ 0 for i in range(length) ] for j in range(length) ]
    # for x in range(length):
    #     # if x==list[x]-1:
    #         # arr[list[x]-1][length-x-1] = list[x]
    #     for y in range(length):
    #print(arr)
    # for x in range(8):
    # arr[1][1]=5

    for i, k in enumerate(list):
        arr[k-1][i] = k
        # #print('arr'+'['+str(i)+']'+'['+str(k)+']'+str(arr[k-1][i]))
    #print(arr)
    trackArr = {}
    value = 0
    dArr = arr
    for x in range(length):
        for y in range(length):
            if(dArr[x][y]>0):
                v = 0
                trackArr['['+str(x)+']['+str(y)+']'] = ''
                for i in range(length):
                    if dArr[x][i]>0 and i!=y:
                        v+=1
                        trackArr['['+str(x)+']['+str(y)+']'] =trackArr['['+str(x)+']['+str(y)+']'] +' '+'['+str(x)+']['+str(i)+']'
                    if(dArr[i][y]>0 and i!=x):
                        v+=1
                        trackArr['['+str(x)+']['+str(y)+']'] =trackArr['['+str(x)+']['+str(y)+']'] +' '+'['+str(i)+']['+str(y)+']'
                    if x-(i+1)>0 and y-(i+1)>0:
                        if dArr[x-(i+1)][y-(i+1)] > 0:
                            v+=1 
                            trackArr['['+str(x)+']['+str(y)+']'] =trackArr['['+str(x)+']['+str(y)+']'] +' '+'['+str(x-(i+1))+']['+str(y-(i+1))+']'
                    if x+(i+1)<length and y+(i+1)<length:
                        if dArr[x+(i+1)][y+(i+1)] > 0:
                            v+=1 
                            trackArr['['+str(x)+']['+str(y)+']'] =trackArr['['+str(x)+']['+str(y)+']'] +' '+'['+str(x+(i+1))+']['+str(y+(i+1))+']'


                    if x+(i+1)<length and y-(i+1)>0:
                        if dArr[x+(i+1)][y-(i+1)] > 0:
                            v+=1 
                            trackArr['['+str(x)+']['+str(y)+']'] =trackArr['['+str(x)+']['+str(y)+']'] +' '+'['+str(x+(i+1))+']['+str(y-(i+1))+']'

                    if x-(i+1)>0 and y+(i+1)<length:
                        if dArr[x-(i+1)][y+(i+1)] > 0:
                            v+=1 
                            trackArr['['+str(x)+']['+str(y)+']'] =trackArr['['+str(x)+']['+str(y)+']'] +' '+'['+str(x-(i+1))+']['+str(y+(i+1))+']'

                dArr[x][y] = -1
                value+=v
    #             #print("v: "+str(v))
    # for x in range(length):
    #     #print(dArr[x])
    #print("value: "+str(value)+'\n')
    # #print("Tracking: \n"+str(trackArr))
    return value
                
                        

def single_crossover(list, length):
    # #print(list)
    arr = [ [ 0 for i in range(length) ] for j in range(len(list)*2) ]
    arr[0]=list[0]
    arr[1]=list[1]
    #print(arr)

    rand = random.randint(1,length)
    #print(rand)

    for x in range(len(list)):
        for y in range(length):
            if y <= rand-1:
                if x==0:
                    arr[2][y]=arr[x][y]
                elif x==1:
                    arr[3][y]=arr[x][y]
            elif y > rand-1:
                if x==0:
                    arr[3][y]=arr[x][y]
                elif x==1:
                    arr[2][y]=arr[x][y]
    return arr
    


def mutation_fuc(list, length):
    #print(list)
    for x in range(len(list)):
        posRand = random.randint(1, length)
        valueRand = random.randint(1, length)
        # #print(posRand)
        # #print(valueRand)
        list[x][posRand-1] = valueRand
    # #print(list)
    return list
    
def single_crossover_after_unfit_replace(list, length):
    # #print(list)
    arr = [ [ 0 for i in range(length) ] for j in range(len(list)) ]
    # #print(arr)

    rand = random.randint(1,length)
    #print(rand)

    for x in range(len(list)):
        for y in range(length):
            if y > rand-1:
                if x==0:
                    arr[1][y]=list[x][y]
                elif x==1:
                    arr[0][y]=list[x][y]
                elif x==2:
                    arr[3][y]=list[x][y]
                elif x==3:
                    arr[2][y]=list[x][y]
            else:
                arr[x][y]=list[x][y]
    return arr
    


    

def main():

    #print("N Queen Problem")

    inp = int(input('Enter N value: '))

    p =[ [ 0 for i in range(inp) ] for j in range(2) ]#[[0]*inp]*2

    pFitness = [ 0 for i in range(len(p)) ]
    maxFitness = inp *(inp-1)/2

    for x in range(2):
        p[x].clear()
        for y in range(inp):
            p[x].append(random.randint(1,inp))
        #print(p[x])
        pFitness[x] = int(maxFitness) - fitness_calc(p[x])

    #print(maxFitness)
    #print(pFitness)

    newCrosssPopulation = single_crossover(p, inp)

    continueLoop = True
    count = 1
    while(continueLoop):
        newMutationPopulation = mutation_fuc(newCrosssPopulation, inp)
        #print(newMutationPopulation)

        newPopulationFitness = [ 0 for i in range(len(newMutationPopulation)) ]

        for x in range(len(newMutationPopulation)):
            newPopulationFitness[x] = int(maxFitness) - fitness_calc(newMutationPopulation[x])
        #print(newPopulationFitness)
        unfitIndex = newPopulationFitness.index(min(newPopulationFitness))
        maxPopulationFitness = max(newPopulationFitness)
        if(maxPopulationFitness == maxFitness):
            fitestIndex = newPopulationFitness.index(maxPopulationFitness)
            print('Interval: '+str(count))
            print('Parents: ')
            print(p)
            print('Parents Fitness Value: ')
            print(pFitness)

            print('\nLast Children: ')
            print(newMutationPopulation)
            print('Last Children Fitness Value: ')
            print(newPopulationFitness)





            print('\n'+str(fitestIndex+1)+" number of children get the solution")
            print('Fittest Child: ')
            print(newMutationPopulation[fitestIndex])
            break

        count+=1
        #print(unfitIndex)
        #print(newMutationPopulation)

        if unfitIndex<2:
            newMutationPopulation[unfitIndex] = newMutationPopulation[3]
        else:
            newMutationPopulation[unfitIndex] = newMutationPopulation[1]
        #print(newMutationPopulation)

        newCrosssPopulation = single_crossover_after_unfit_replace(newMutationPopulation, inp)
        #print(newCrosssPopulation)


    # fitness_calc(p[0])


if __name__ == "__main__":
    main()