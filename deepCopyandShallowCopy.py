import copy   #  copy module

import unittest

class testCopy(unittest.TestCase):
    def test_equalOperator():

        # In Python, we use = operator to create a copy of an object.
        # You may think that this creates a new object; 
        # it doesn't. It only creates a new variable that shares the reference of the original object.
        print('---------------------- copy object with equal oprator------------')
        old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
        new_list = old_list

        new_list[2][2] = 9

        print('Old List:', old_list)
        print('ID of Old List:', id(old_list))

        print('New List:', new_list)
        print('ID of New List:', id(new_list))

    def test_shallowCopy():

        # Essentially, sometimes you may want to have the original values unchanged 
        # and only modify the new values or vice versa. 
        # In Python, there are two ways to create copies:
                # Shallow Copy
                # Deep Copy
        # To make these copy work, we use the copy module.
        # shallow copy
        # A shallow copy creates a new object which stores the reference of the original elements.
        # So, a shallow copy doesn't create a copy of nested objects,
        # instead it just copies the reference of nested objects. 
        # This means, a copy process does not recurse or create copies of nested objects itself.

        #--------------------------------shallow copy   is defferent and independent with the old object---------------------------

        # To confirm that new_list is different from old_list,
        # we try to add new nested object to original and check it.
        print('--------------------shallow copy with copy method----------------')
        old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]         
        new_list = copy.copy(old_list)

        old_list.append([4, 4, 4])

        print("Old list:", old_list)
        print("New list:", new_list)


    def test_deepCopy():

        #-------------------------------shallow copy  copy the reference of the original elements-----------------
        print('--------------deep copy ---------------------')
        old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        new_list = copy.copy(old_list)

        old_list[1][1] = 'AA'

        print("Old list:", old_list)
        print("New list:", new_list)



    def test_deepCopy2():
        
        #---------------------deep copy------------------ creates independent copy of original object and all its nested objects.
        # A deep copy creates a new object 
        # and recursively adds the copies of nested objects present in the original elements.
        old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        new_list = copy.deepcopy(old_list)

        old_list[1][0] = 'BB'

        print("Old list:", old_list)
        print("New list:", new_list)


