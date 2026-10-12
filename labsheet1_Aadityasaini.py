#1
import time
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
sizes=[10000,50000,100000]
for n in sizes:
    arr=list(range(n))
    target=n-1
    start=time.perf_counter_ns()
    result=linear_search(arr,target)
    end=time.perf_counter_ns()
    execution_time=(end-start)/1000
    print("Array size:",n)
    print("Target found at index:",result)
    print("Execution time:",round(execution_time,2),"microseconds")
    print()

#2
import time
def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
sizes=[10000,50000,100000]
for n in sizes:
    arr=list(range(n))
    target=n-1
    start=time.perf_counter_ns()
    result=binary_search(arr,target)
    end=time.perf_counter_ns()
    execution_time=(end-start)/1000
    print("Array size:",n)
    print("Target found at index:",result)
    print("Execution time:",round(execution_time,2),"microseconds")
    print()
 
#3
import time
for n in [100,500,1000,2000,4000]:
 start=time.perf_counter()
 count=0
 for i in range(n):
  for j in range(n):
   count+=1
 end=time.perf_counter()
 print(f"n={n},Time={(end-start)*1000000:.2f} microseconds")
  
