#class - ADA
#date 24/03/2025
'''In Insertion sort 
step1:take a first element as sorted array
step2:take second element as key
step3:comapare the key with left elments of sorted array 
step4:place the key at its right position
'''
def Insertion_sort(arr):
    n=len(arr)
    if n>2:
        key_in=2
        key=arr[key_in]
        for i in range(n):
            if key>=0 & key<n:
                if arr[key_in]>arr[key_in-1]:
                    arr[key_in],arr[key_in-1]=arr[key_in-1],arr[key_in]
            key_in =key_in+1
        print(arr) 
if '__name__'=="__main__":
    a=int(input("enter the size of array: "))
    
   


