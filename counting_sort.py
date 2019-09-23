#!/usr/bin/env python
import time
start = time.time()
def counting_sort(array, maxval):
    global count_1
    count_1 = 0
    """in-place counting sort"""
    n = len(array)
    m = maxval + 1
    count = [0] * m
    print("length of count" , len(count))# init with zeros
    for a in array:
        count_1 += 1
        count[a] += 1   # count occurences
    i = 0
    for a in range(m):            # emit
        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
            count_1 += 1
            array[i] = a
            i += 1
    return array


fp = open("case")  # Open file on read mode
arr = fp.read().split(" ")  # Create a list containing all lines
fp.close()

list2 = []
for i in range(len(arr)):
    t = int(arr[i])
    list2.append(t)

print(counting_sort(list2 , 20 ))# 20 k değerine eşit input size ı 20 yi geçmiyecek ancak değiştirilebilir
print(count_1)

end = time.time()
print(end - start)


#################################
####   complexity analysis   ####
#################################


#
# time
#

#worst: O(n)
#average: O(n)
#best: O(n)

#
# space
#

#total: O(n + k)
#auxiliary: O(k)

#other
#than
#the
#input
#array, we
#need
#extra
#array[k]
#for storing the counting result.as stated at the beginning, the assumption is k is much smaller than n for this algo to be efficient.but if not, space inefficiency becomes apparent, which leads us to other non-comparision-based algo such as radix sort and bucket(bin) sort.

#if your only knowledge about the input data range is, for example, just an unsigned integer.then k = 2 ^ 32 = approx 4GB size, which is ridiculously huge.and N can be just 10, etc.in such a case, counting sort is not suitable.(who allocates 4GB auxiliary space for sorting 10 integers?)

#space:

#total

#o(n + k)

#auxiliary:

#o(k)

#worst
#case
#space
#complexity:

#o(n + k)


