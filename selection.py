import time 
import sys 

A = [64,25,11,34,56,87,57,23,45] 

start_time = time.time()

for i in range(len(A)): 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
    A[i], A[min_idx] = A[min_idx], A[i] 

end_time = time.time()

print("Sorted array:")
for i in range(len(A)): 
    print("%d" %A[i],end="  ")

print("\nExecution time:", end_time - start_time, "seconds")
