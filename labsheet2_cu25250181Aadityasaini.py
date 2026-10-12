arr=list(map(int,input("Enter array elements: ").split()))
while True:
 print("1.Insert\n2.Delete\n3.Search\n4.Display\n5.Exit")
 ch=int(input("Enter choice: "))
 if ch==1:
  val=int(input("Enter element: "))
  idx=int(input("Enter index: "))
  if 0<=idx<=len(arr):
   arr.insert(idx,val)
   print(arr)
  else:
   print("Invalid index")
 elif ch==2:
  idx=int(input("Enter index: "))
  if 0<=idx<len(arr):
   arr.pop(idx)
   print(arr)
  else:
   print("Invalid index")
 elif ch==3:
  val=int(input("Enter value to search: "))
  idx=-1
  for i in range(len(arr)):
   if arr[i]==val:
    idx=i
    break
  print("Index:",idx)
 elif ch==4:
  print(arr)
 elif ch==5:
  break
 else:
  print("Invalid choice")
