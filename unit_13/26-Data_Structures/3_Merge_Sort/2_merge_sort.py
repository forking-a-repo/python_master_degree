#
#  Data Structures: Merge Sort: Splitting into sublists
#  Python Techdegree
#
#  Created by Dulio Denis on 3/24/19.
#  Copyright (c) 2019 ddApps. All rights reserved.
# ------------------------------------------------
def merge_sort(list):
    '''
    Sorts a list in ascending order.
    Returns a new sorted list.

    Divide:  Find the midpoint of the list and divide into sublists.
    Conquer: Recursively sort the sublists created in previous step.
    Combine: Merge the sorted sublists created in the previous step.
    '''
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    '''
    Divide the unsorted list at midpoint into sublists.
    Returns two sublists - left and right.
    '''
    midpoint = len(list) // 2
    left = list[:midpoint]
    right = list[midpoint:]
    
    return left, right


