import time
start = time.time()
# Python program for implementation of heap Sort
count = 0
# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
	global count
	count += 1
	largest = i # Initialize largest as root
	l = 2 * i + 1	 # left = 2*i + 1
	r = 2 * i + 2	 # right = 2*i + 2

	# See if left child of root exists and is
	# greater than root
	if l < n and arr[i] < arr[l]:
		largest = l

	# See if right child of root exists and is
	# greater than root
	if r < n and arr[largest] < arr[r]:
		largest = r

	# Change root, if needed
	if largest != i:
		arr[i],arr[largest] = arr[largest],arr[i] # swap

		# Heapify the root.
		heapify(arr, n, largest)

# The main function to sort an array of given size
def heapSort(arr):
	global count
	n = len(arr)
	# Build a maxheap.
	for i in range(n, -1, -1):
		heapify(arr, n, i)
	count += 1
	# One by one extract elements
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap
		heapify(arr, i, 0)
count += 1
# Driver code to test above

fp = open("case")  # Open file on read mode
arr = fp.read().split(" ")  # Create a list containing all lines
fp.close()

list2 = []
for i in range(len(arr)):
    t = int(arr[i])
    list2.append(t)

heapSort(list2)
for i in range(len(list2)):
	print ("% d" % list2[i])

# This code is contributed by Mohit Kumra
end = time.time()
print(end - start)
print(count)