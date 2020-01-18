import pygame
import sys
from tictacsprites import Marks

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')

sprites = pygame.sprite.Group()

def draw_board(board):
    x = 0
    y = 0
    for i in range(len(board)):
        for n in range(len(board)):
            if board[i][n] == '#':
                pygame.draw.rect(screen,(255, 255, 255), ((x, y),(200,200))) 
            
            if board[i][n] == 'O':
                circle = Marks('O')
                sprites.add(circle)
                circle.rect.x = x
                circle.rect.y = y

            if board[i][n] == 'X':
                cross = Marks('X')
                sprites.add(cross)
                cross.rect.x = x
                cross.rect.y = y

            x += 200 + 1
        
        y += 200 + 1
        x = 0

def check_win(board):
    for i in range(len(board)): 
        if board[i][0] == board[i][1] == board[i][2] == 'O':
            return 1

        if board[0][i] == board[1][i] == board[2][i] == 'O':
            return 1

        if board[0][0] == board[1][1] == board[2][2] == 'O':
            return 1

        if board[0][2] == board[1][1] == board[2][0] == 'O':
            return 1
        
        if board[i][0] == board[i][1] == board[i][2] == 'X':
            return 2

        if board[0][i] == board[1][i] == board[2][i] == 'X':
            return 2

        if board[0][0] == board[1][1] == board[2][2] == 'X':
            return 2

        if board[0][2] == board[1][1] == board[2][0] == 'X':
            return 2
        
        for n in range(len(board)):
            if board[i][n] == '#':
                return -1


    if '#' not in board:
        return 0
class GameApp:

    def __init__(self):
        pygame.init()
        
        self.board = [['#','#','#'],
                      ['#','#','#'], 
                      ['#','#','#'] ]

        self.turn = 1

    def execute(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    posx, posy = pygame.mouse.get_pos()
                    posx = posx // 200
                    posy = posy // 200
                    
                    if self.turn % 2 == 1 and self.board[posy][posx] == '#':
                        self.board[posy][posx] = 'O'
                        self.turn += 1

                    elif self.turn % 2 == 0 and self.board[posy][posx] == '#':
                        self.board[posy][posx] = 'X'
                        self.turn += 1
                    
                                       

            screen.fill((0, 0, 0))
            
            draw_board(self.board)
            sprites.draw(screen)

            pygame.display.flip()


            if check_win(self.board) == 1:
                print('O wins')
                break
            
            if check_win(self.board) == 2:
                print('X wins')
                break
            
            if check_win(self.board) == 0:
                print('TIE!')
                break

if __name__=='__main__':

    game = GameApp()
    game.execute()
