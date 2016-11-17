from textPreprocess import Documents
from Distances import docdistance

FILEPATH1 = 'E:\PythonWorkspace\Distance of two documents\document1.txt'
FILEPATH2 = 'E:\PythonWorkspace\Distance of two documents\document2.txt'

if __name__ == '__main__':
    document1 = Documents(FILEPATH1)
    document2 = Documents(FILEPATH2)
    document1.showallwords()
    document2.showallwords()
    distance = docdistance(document1, document2)
    print('The distance between document1 & document2 is:' + str(distance))




