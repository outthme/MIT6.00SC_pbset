def recur_insertSort(l):
#Empty list test
    if not len(l):
        return print('Imput is a empty list')
    
#Main body of this function
    elif len(l) > 1:
        remain = l[-1] #store the last unsorted number of the list
#pass the sequence-assumed list: l[:-1]
#into the next recursion and get the sorted list as a return
        sorted_list = recur_insertSort(l[:-1]) 
        insert_to_list(sorted_list, remain) #insert the remain into the sorted_list
        return sorted_list
#If the length of l is 1, it did not pass l into the futher recursion
#and return the 1-sized list as a sequenced list.
    elif len(l) == 1:
        return l

def insert_to_list(l, i):
#set lower and upper bounds for binary sort.
    low = 0
    high = len(l)-1 
    flag = 0 #in case for len(l)=1 input.
#do binary search.
    test = 1
    while low <= high:
        flag = int((low + high) / 2)
        if l[flag] == i:
            break
        elif l[flag] > i:
            high = flag - 1
        elif l[flag] < i:
            low = flag + 1
#do insertion( insert i before flag if l[flag] >= i otherwise after flag)
    if l[flag] >= i:
        l.insert(flag, i)
    else:
        l.insert(flag+1, i)
    return l
