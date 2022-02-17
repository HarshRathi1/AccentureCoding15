'''Write a function to validate if the provided two strings are anagrams or not. If the two strings are anagrams, then return ‘yes’. Otherwise, return ‘no’.
Input:
Input 1: 1st string
Input 2: 2nd string
Output:
(If they are anagrams, the function will return ‘yes’. Otherwise, it will return ‘no’.)'''
def fun(a,b):
    l1 = sorted(list(a))
    l2 = sorted(list(b))
    if l1 == l2:
        return "Yes"
    else:
        return "No"
a = 'listen'
b = 'silent'
print(fun(a,b))