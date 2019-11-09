import pprint
def Board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('_____')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('_____')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


    
theBoard={'top-L': ' ', 'top-M': 'o', 'top-R': ' ',
         'mid-L': 'x', 'mid-M': 'x', 'mid-R': ' ',
         'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


Board(theBoard)

