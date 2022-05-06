def getMatrix():
    print("#"*10)
    print("INPUT MATRIX")
    row_count = int(input("ROW COUNT: "))
    col_count = int(input("COL COUNT: "))
    matrix = []
    for i in range(1, row_count+1):
        row = []
        for j in range(1, col_count+1):
            element = int(input(str(i)+" ROW, " + str(j) + " COL: "))
            row.append(element)
        matrix.append(row)
    return matrix
def printMatrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end="\t")
        print()
def orderOfMatrix(matrix):
    order = str(len(matrix[0]))+"x"+str(len(matrix))
    return order
def checkConfiguration(matrix):
    mean = len(matrix[0])
    badhiya = True
    for rows in matrix:
        if (len(rows) != mean):
            badhiya = False
            break
    return badhiya
def addMatrix(a, b):
    if (checkConfiguration(a) == True and checkConfiguration(b) == True and orderOfMatrix(a) == orderOfMatrix(b)):
        sum = []
        rw = 0
        cl = 0
        for rows in a:
            nwrw = []
            for col in rows:
                el = col + b[rw][cl]
                nwrw.append(el)
                cl+=1
            rw+=1
            cl = 0
            sum.append(nwrw)
        return sum
    else:
        return False
def printSign(sign):
    print("\t"+sign)
a = getMatrix()
b = getMatrix()
matrixSum = addMatrix(a, b)
if (matrixSum != False):
    print("""\n
PRINTING SUM\n
    """)
    printMatrix(a)
    printSign("+")
    printMatrix(b)
    printSign("=")
    printMatrix(matrixSum)
else:
    print("BEKAR MATRIX DI HAI, SHHE!")
