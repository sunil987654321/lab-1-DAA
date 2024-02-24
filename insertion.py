import time

# Function to do insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    # Define the array of 40 elements
    arr = [64, 45, 87, 98, 65, 34, 56, 78, 76, 86, 36, 23, 79, 66, 26, 33,
           67, 55, 21, 88, 44, 89, 99, 90, 100, 77, 80, 91, 92, 93, 94, 95,
           96, 97, 1, 2, 3, 4, 5, 6, 7, 8]
    
    start_time = time.time()
    insertionSort(arr)
    end_time = time.time()

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")

    # Convert the time difference from seconds to milliseconds
    execution_time_ms = (end_time - start_time) * 1000
    print("\nExecution time:", execution_time_ms, "milliseconds")
