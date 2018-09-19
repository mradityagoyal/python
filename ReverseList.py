"""
reverse alternate K elements in a list
"""

def reverseAlternateK(input: [], K : int) -> None:
    starts = list(range(0,len(input)-1, 2*K))
    for start in starts:
        end = -1
        if len(input) < start + K: end = len(input)-1
        else: end = start + K -1
        reverse(input, start, end)

def reverse(input: [], start: int, end: int)-> None:
    x = start
    y = end
    while x < y:
        swap(input, x , y)
        x+=1
        y-=1

def swap(input: [], i: int, j: int)-> None: input[i] , input[j] = input[j] , input[i]

#
# input = [1,2,3]
# reverse(input,0,2)
# print(input)

input = list(range(0,14))
print(input)
reverseAlternateK(input, 4)
print(input)