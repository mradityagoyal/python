"""
reverse alternate K elements in a list
"""

def reverseAlternateK(input: [str], K : int) -> None:
    starts = list(range(0,len(input)-1, 2*K))
    for start in starts:
        end = -1
        if len(input) < start + K: end = len(input)-1
        else: end = start + K -1
        reverse(input, start, end)

def reverse(input: [str], start: int, end: int)-> None:
    for i in range(0, max(1,int((end-start)/2))):swap(input, start+i, end -i)

def swap(input: [], i: int, j: int)-> None: input[i] , input[j] = input[j] , input[i]

#
# input = [1,2,3]
# reverse(input,0,2)
# print(input)

input = list(range(0,14))
print(input)
reverseAlternateK(input, 3)
print(input)