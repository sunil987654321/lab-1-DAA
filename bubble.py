import time

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

if __name__ == "__main__":
    arr = [64,45,87,98,65,34,56,78,76,86,36]
    
    start_time = time.time()
    bubbleSort(arr)
    end_time = time.time()

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")

    print("\nExecution time:", end_time - start_time, "seconds")
