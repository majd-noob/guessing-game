my_list=[2, 4, 6,12, 14, 16,1,3,99]

def even():
    for x in my_list:
        if x % 2 ==0:
            print(x)
        else:
            return my_list
even()
