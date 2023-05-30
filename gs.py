

import random

def fitness_calc(list):
    length = len(list)
    arr =[ [ 0 for i in range(length) ] for j in range(length) ]
    # for x in range(length):
    #     # if x==list[x]-1:
    #         # arr[list[x]-1][length-x-1] = list[x]
    #     for y in range(length):
    print(arr)
    # for x in range(8):
    # arr[1][1]=5

    for i, k in enumerate(list):
        arr[k-1][i] = k
        # print('arr'+'['+str(i)+']'+'['+str(k)+']'+str(arr[k-1][i]))
    print(arr)

    value = 0

    for x in range(length):
        for y in range(length):
            if(arr[x][y]>0):
                v = 0
                for i in range(length):
                    if arr[x][i]>0 and i!=y:
                        v+=1
                    if(arr[i][y]>0 and i!=x):
                        v+=1
                    if x-(i+1)>0 and y-(i+1)>0:
                        if arr[x-(i+1)][y-(i+1)] > 0:
                            v+=1 
                    if x+(i+1)<length and y+(i+1)<length:
                        if arr[x+(i+1)][y+(i+1)] > 0:
                            v+=1 

                    if x+(i+1)<length and y-(i+1)>0:
                        if arr[x+(i+1)][y-(i+1)] > 0:
                            v+=1 
                    if x-(i+1)>0 and y+(i+1)<length:
                        if arr[x-(i+1)][y+(i+1)] > 0:
                            v+=1 
                    

                #     if length-(i+1)>=0:
                #         # print(length-(i+1))

                #         if arr[length-(i+1)][i]>0:
                #             v+=1
                #     if length-(i+1)>=0 and arr[i][length-(i+1)]>0:
                #         v+=1
                # v-=2
                print(v)
                
                        




    

def main():

    print("N Queen Problem")

    inp = int(input('Enter N value: '))

    p =[[0]*inp]*2

    for x in range(2):
        p[x].clear()
        for y in range(inp):
            p[x].append(random.randint(1,inp))

    print(p)
    fitness_calc(p[0])


if __name__ == "__main__":
    main()