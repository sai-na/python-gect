# def my_function() : 
#     print ("hello")

# my_function()


def linearSearch (list1 , input_val) : 
    flag = 0

    for x in list1 : 
        if input_val== x :
            flag = 1
    if flag == 1 :
        print(input_val , "contains")
    else : 
            print(input_val , "not contains")


list1 = [1,3,4,5,2,0,88]
input_val = int(input("search value : "))
linearSearch(list1=list1 , input_val=input_val)