def extsort(list):
    new_list=[]
    for x in list:
        '''split each element to list append that element list to new_list'''
        new_list.append(x.split('.'))
    new_list.sort(key = lambda x: x[1])#this new_list is sorted
    '''next step combine members in list by '.'.join'''
    list=[]
    for x in new_list:
        list.append('.'. join(x))
    return list
