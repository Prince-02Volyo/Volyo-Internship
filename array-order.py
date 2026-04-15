#output should be  ["","a","zz","abc","aaa"]


def solution(inputArray):
    return sorted(inputArray, key = len)

inputArray = ["abc", "", "aaa", "a", "zz"]
print(solution(inputArray))


#def inputArray(arr1):

'''arr1 = ["abc","", "aaa", "a", "zz"]
new = sorted(arr1) 
print(new)'''