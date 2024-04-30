def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 #get the idx for middle element
        left_array = arr[:mid]
        right_array = arr[mid:]

        mergesort(left_array)
        mergesort(right_array)

        i = 0 #idx for left_array
        j = 0 #idx for right_array
        k = 0 #idx for sorted array

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                arr[k] = left_array[i]
                i+=1
            else:
                arr[k] = right_array[j]
                j+=1
            #move to next slot
            k+=1
        while i < len(left_array): #to check if any elements is remaining in the left array
            arr[k] = left_array[i]
            i+=1
            k+=1
        while j < len(right_array): #to check if any elements is remaining in the right array
            arr[k] = right_array[j]
            j+=1
            k+=1
