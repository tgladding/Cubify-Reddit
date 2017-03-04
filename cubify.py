filler = '/'


def cubify(word, diagonalWord=None):
    if not((word.__len__() >= 1) & (word.isalpha()) & (word.endswith(word[0])) & (word.__len__() % 2 == 1)):
        print("[cubify] This word (%s) can't be cubified." %word)
        return False

    word = word.upper()
    if diagonalWord != None:
        diagonalWord = diagonalWord.upper()
        if not (diagonalWord.isalpha() & (diagonalWord.startswith(word[0])) & diagonalWord.endswith(word[0]) & (len(diagonalWord) == int(len(word) / 2 + 1))):
            #print("[cubify] Diagonalword is not suited.")
            diagonalWord = None



    #create matrix filled with placeholder .
    size = int(word.__len__() / 2 + word.__len__())
    matrix = [[' ' for x in range(size)] for y in range(size)]


    gap = int(len(word) / 2)

    for i in range(len(word)):
        #write horizontal words
        matrix[0][gap + i] = word[i]
        matrix[gap][i] = word[i]
        matrix[2*gap][gap + i] = word[i]
        matrix[3*gap][i] = word[i]

        #write vertical words
        matrix[gap + i][0] = word[i]
        matrix[i][gap] = word[i]
        matrix[i][3*gap] = word[i]
        matrix[gap + i][2*gap] = word[i]

    #write diagonal
    for i in range(1,gap):
        if diagonalWord == None:
            matrix[gap - i][i] = filler
            matrix[gap - i][2 * gap + i] = filler
            matrix[3 * gap - i][i] = filler
            matrix[3 * gap - i][2 * gap + i] = filler
        else:
            matrix[gap - i][i] = diagonalWord[i]
            matrix[gap - i][2 * gap + i] = diagonalWord[i]
            matrix[3 * gap - i][i] = diagonalWord[i]
            matrix[3 * gap - i][2 * gap + i] = diagonalWord[i]


    #making matrix pretty
    # matrix = [[x if x != ' ' else ' ' for x in row] for row in matrix]     #replace background with another character
    matrix = [' '.join(row) for row in matrix]

    matrix = ['    ' + row for row in matrix]

    return displayMatrix(matrix)


def displayMatrix(matrix):
    string = ''
    for x in matrix:
        for y in x:
            string += y
        string += '\n'
    return string