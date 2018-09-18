# write a program to find all words in a given matrix.
# words can be in up / down/ left / right / diagnols in the matrix.
# input list of valid words and a matrix of characters.

def findAllWords(matrix: [[int]], validWords: [str]) -> [] :
    """

    :param matrix: a 2 d char array.
    :param validWords: a seq of strings.
    :return: a seq of strings found in the matrix.
    """
    result = []

    rows = len(matrix)
    cols = len(matrix[0])

    def is_valid_coord(coord: (int, int)) -> bool:
        return coord[0] <= rows -1 and coord[0] >= 0 and coord[1] >= 0 and coord[1] <= cols -1

    def char_at(coord: (int, int)) -> str:
        if is_valid_coord(coord):
            return matrix[coord[0]][coord[1]]
        else: return ''

    def nextCoordInDir(coord: (int, int), dir: (int, int)) -> (int, int):
        return coord[0] + dir[0], coord[1]+ dir[1]

    for col in range(0, cols):
        for row in range(0, rows):
            start = (row, col)
            startWord = char_at(start)
            if startWord in valid_words: result.append(startWord)
            for dir in getDirections():
                sw = startWord
                nextCoord = nextCoordInDir(start, dir)
                while (is_valid_coord(nextCoord)and contains_prefix(sw + char_at(nextCoord), valid_words)):
                    sw += char_at(nextCoord)
                    if sw in validWords : result.append(sw)
                    nextCoord = nextCoordInDir(nextCoord, dir)
    return result

def getDirections() -> []:
    """
    return all 8 directions as tuples.
    :return:
    """
    result = []
    for i in range(-1, 2):
        for j in range (-1, 2):
            if not (i == 0 and j==0):
                result.append((i,j))
    return result


def contains_prefix(prefix, ls) -> bool:
    return len(list(filter(lambda x: x.startswith(prefix), ls))) > 0


#

matrix = []
matrix.append([c for c in 'andy'])
matrix.append([c for c in 'dade'])
matrix.append([c for c in 'done'])

for row in matrix:
    print(row)

valid_words = ['and', 'add', 'done', 'on', 'ned', 'x' , 'ndd']

found = findAllWords(matrix, valid_words)
print(found)
