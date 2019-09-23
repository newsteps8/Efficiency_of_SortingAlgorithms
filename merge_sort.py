import time
start = time.time()
# Python program for implementation of MergeSort



count = 0
def mergeSort(arr):

    global count
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            count = count + 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            count = count + 1
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            count = count + 1
            arr[k] = R[j]
            j += 1
            k += 1





# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# driver code to test the above code
if __name__ == '__main__':

    fp = open("case")  # Open file on read mode
    arr = fp.read().split(" ")  # Create a list containing all lines
    fp.close()

    list2 = []
    for i in range(len(arr)):
        t = int(arr[i])
        list2.append(t)

    mergeSort(list2)
    print("Sorted array is: ", end="\n")
    printList(list2)
    print(count)

# This code is contributed by Mayank Khanna

end = time.time()
print(end - start)