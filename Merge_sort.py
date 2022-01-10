
### Use this space to try out ideas and free code ###
def merge(arr_1, arr_2):
  
  arr_len_1 = len(arr_1)
  arr_len_2 = len(arr_2)
  i = j = k = 0
  
  sorted_arr = [None] * (arr_len_1 + arr_len_2)
  
  while i < arr_len_1 and j < arr_len_2:
    if arr_1[i] < arr_2[j]:
      sorted_arr[k] = arr_1[i]
      i += 1
      k += 1
    else:
      sorted_arr[k] = arr_2[j]
      j += 1
      k += 1
      
  while i < arr_len_1:
    sorted_arr[k] = arr_1[i]
    i += 1
    k += 1
  
  while j < arr_len_2:
    sorted_arr[k] = arr_2[j]
    j += 1
    k += 1
  
  return sorted_arr
      
def merge_split(arr):
  if len(arr) == 1:
    return arr
  left_part = merge_split(arr[:len(arr)//2])
  right_part = merge_split(arr[len(arr)//2:])
  
  return merge(left_part, right_part)
  
  
# arr = [20, 19, 8, 6, 13, 0, 1, 26]
# print(merge_split(arr))
