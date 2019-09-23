import time
start = time.time()


# Python program for implementation of Insertion Sort
# Function to do insertion sort


def insertionSort(arr):
    count = 0
    for i in range(1, len(arr)):
        count = count + 1
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            count = count + 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    print(count)



# Driver code to test above

fp = open("case")  # Open file on read mode
arr = fp.read().split(" ")  # Create a list containing all lines
fp.close()

list2 = []
for i in range(len(arr)):
    t = int(arr[i])
    list2.append(t)

insertionSort(list2)
for i in range(len(list2)):
	print ("% d" % list2[i])


end = time.time()
print(end - start)

