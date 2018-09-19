# in a string.. find the largest substring with atmost K characters

def run_length(input: str) -> [(str, int)] :
    if not input: return []

    result = []
    currentChar = input[0]
    count = 0
    for char in input:
        if char == currentChar:
            count+=1
        else:
            result.append((currentChar, count))
            currentChar = char
            count=1
    result.append((currentChar, count))
    return result

#incorrect implementation
# def longest_with_max2(input: str) -> str:
#     rl_encode = run_length(input)
#     if len(rl_encode) <= 2: return  input
#     maxLen = -1
#     result_rl = []
#     for i in range(0, len(input)-2):
#         window = rl_encode[i:i+2]
#         lenWindow = sum([pair[1] for pair in window])
#         if lenWindow > maxLen:
#             maxLen = lenWindow
#             result_rl = window
#     return stringify(result_rl)

def longestMaxK(input : str, K : int) -> str:
    rl_encode = run_length(input)
    if len(rl_encode) <= K: return  input

    maxLen = -1
    maxRes = []
    result_rl = []
    uniqueChars = set()
    while rl_encode:
        if len(uniqueChars) < K:
            top = rl_encode.pop(0)
            result_rl.append(top)
            uniqueChars.add(top[0])
        elif len(uniqueChars) == K:
            if rl_encode[0][0] in uniqueChars:
                top = rl_encode.pop(0)
                result_rl.append(top)
                currentLen = sum([count for char, count in result_rl])
                if currentLen > maxLen:
                    maxLen = currentLen
                    maxRes = result_rl.copy()
            else:
                currentLen = sum([count for char, count in result_rl])
                if currentLen > maxLen:
                    maxLen = currentLen
                    maxRes = result_rl.copy()
                result_rl.pop(0)
                uniqueChars= set([char for char, idx in result_rl])


        else: # result has more than K unique
            result_rl.pop(0)
            uniqueChars = set([char for char , idx in result_rl])

    currentLen = sum([count for char, count in result_rl])
    if currentLen > maxLen:
        maxLen = currentLen
        maxRes = result_rl.copy()
    return stringify(maxRes)






def stringify(runLength: [(str, int)])-> str :
    return "".join([char*count for char , count in runLength])

#
# print(run_length("adaabacccc"))
#
# print(stringify(run_length("adaabacccc")))

# print(longest_with_max2("aabbcccdddeeeee"))
# print(longest_with_max2("aa"))
input = "aaacaadddeee"
# print(longest_with_max2(input))
print(longestMaxK(input, 3))


