import numpy as np

#we declare three empty numpy arrays which we will be modifying to store the values of the three lfsr's
reg_1 = np.empty
reg_2 = np.empty
reg_3 = np.empty

def user_input():
    usrinput = np.array(list(map(int,(input("Enter the 64 bit key with space between the elements").strip().split()))), dtype=bool)
    print(usrinput)
    print(type(usrinput))
    if len(usrinput) == 64:
        return usrinput
    else:
        while len(usrinput) != 64:
            if len(usrinput) == 64:
                return usrinput
            usrinput = np.array(list(map(int,(input("Enter the 64 bit key with space between the elements").strip().split()))), dtype=bool)
        return usrinput

def load_key(key):

    global reg_1
    global reg_2
    global reg_3

#   print(key,type(key))
    reg_1 = key[0:19]
    reg_2 = key[19:41]
    reg_3 = key[41:64]
    # print(reg_1,reg_2,reg_3)
    print("registers loaded succesfully")


def get_majority(a,b,c):
    if int(a) + int(b) + int(c) > 1:
        return True
    else:
        return False



def clock_a5(clocking):
    c = clocking

    global reg_1
    global reg_2
    global reg_3

    # print(reg_1[7], reg_2[9], reg_3[9])

    while c != 0:
        majority = get_majority(reg_1[8], reg_2[10], reg_3[10])
        # print(majority)
        if reg_1[8] == majority:
            first_bit = int(reg_1[18]) ^ int(reg_1[17]) ^ int(reg_1[16]) ^ int(reg_1[13])
            temp_arr1 = np.empty_like(reg_1)
            temp_arr1[0] = first_bit
            # copying all except last bit
            temp_arr1[1:] = reg_1[:18]
            #swapping reg_1
            reg_1 = temp_arr1


        if reg_2[10] == majority:
            first_bit = int(reg_2[20]) ^ int(reg_2[21])
            temp_arr2 = np.empty_like(reg_2)
            temp_arr2[0] = first_bit
            # copying all except last bit
            temp_arr2[1:] = reg_2[:21]
            # swapping reg_2
            reg_2 = temp_arr2

        if reg_3[10] == majority:
            first_bit = int(reg_3[20]) ^ int(reg_3[21]) ^ int(reg_3[22])
            temp_arr3 = np.empty_like(reg_3)
            temp_arr3[0] = first_bit
            #copying all except last bit
            temp_arr3[1:] = reg_3[:22]
            # swapping reg_3
            reg_3 = temp_arr3

        #calculating final output bit
        output = int(reg_1[18]) ^ int(reg_2[21]) ^ int(reg_3[22])
        print(int(output), end= '')

        c -= 1




def main():
    key = user_input()
#    replacing user input by test values for now
#    testlist = list(map(int, "0 1 0 1 0 0 1 0 0 0 0 1 1 0 1 0 1 1 0 0 0 1 1 1 0 0 0 1 1 0 0 1 0 0 1 0 1 0 0 1 0 0 0 0 0 0 1 1 0 1 1 1 1 1 1 0 1 0 1 1 0 1 0 1".strip().split()))
#    key = np.array(testlist, dtype=bool)
    # print(key, type(key))
    load_key(key)
    clocking = int(input("Please enter the number of times to clock the Stream Generator"))
    clock_a5(clocking)


main()