

import random

def fitness_calc(list):
    # arr = [[0]*len(list)]*len(list)
    arr =[ [ 0 for i in range(len(list)) ] for j in range(len(list)) ]
    # for x in range(len(list)):
    #     # if x==list[x]-1:
    #         # arr[list[x]-1][len(list)-x-1] = list[x]
    #     for y in range(len(list)):
    print(arr)
    # for x in range(8):
    # arr[1][1]=5

    for i, k in enumerate(list):
        arr[k-1][i] = k
        # print('arr'+'['+str(i)+']'+'['+str(k)+']'+str(arr[k-1][i]))
    print(arr)

    value = 0

    for x in range(len(list)):
        for y in range(len(list)):
            if(arr[x][y]>0):
                v = 0
                for i in range(len(list)):
                    if(arr[x][i]>0):
                        v+=1
                    if(arr[i][y]>0):
                        v+=1
                    

                #     if len(list)-(i+1)>=0:
                #         # print(len(list)-(i+1))

                #         if arr[len(list)-(i+1)][i]>0:
                #             v+=1
                #     if len(list)-(i+1)>=0 and arr[i][len(list)-(i+1)]>0:
                #         v+=1
                # v-=4
                # print(v)
                
                        




    

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