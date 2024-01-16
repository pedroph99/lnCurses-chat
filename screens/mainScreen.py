import curses
from insrtFunctions.insertUser import convertCharKeeper, insert, delete
from screens.roomScreen import createRoomScreen
from user.User import Usuario
def auxScreenUser(width, height):
    begin_x = 5
    auxScreenwidth = width-10
    begin_y = height-5
    auxScreenHeight = 4
    win = curses.newwin(auxScreenHeight, auxScreenwidth, begin_y, begin_x)
    win.addstr(0, 0, "Digite o usuário: ",
              curses.A_REVERSE)
    return win


def refreshMainWin(winObject):
    winObject.clear()
    winObject.box()
    winObject.refresh()



def refreshauxWin(winObject):
    
    winObject.box()
    winObject.addstr(1, 2, "Digite o usuário: ")
    winObject.refresh()
    

def mainScreen(stdscr):
    # Configurações iniciais
    curses.curs_set(0)  # Esconde o cursor
    stdscr.clear()      # Limpa a tela

    # Obtém as dimensões da tela
    height, width = stdscr.getmaxyx()

    # Calcula as coordenadas para o centro da tela
    center_y = height // 2
    center_x = width // 2

    # Define o texto a ser exibido no centro
    title = "CHAT ECOMP"

    # Calcula as coordenadas para exibir o texto no centro da tela
    start_y = center_y - 1
    start_x = center_x - len(title) // 2
    auxWin = auxScreenUser(width, height)
    
    
    # Exibe o texto no centro da tela

    charKeeper = []
    Usuario  = ''
    while True:
        stdscr.addstr(start_y, start_x, title)
        stdscr.box()
        # Atualiza a tela

        stdscr.refresh()
        refreshauxWin(auxWin)

        # Aguarda a entrada do usuário
        key =  stdscr.getch()
        if key == 8:

            delete(charKeeper, auxWin)
            refreshauxWin(auxWin)
        elif key == 10:

            refreshMainWin(stdscr)
            break;
        else:

            insert(charKeeper, auxWin, key)
        print(key)
    Usuario = convertCharKeeper(charKeeper)
    createRoomScreen(stdscr, width, height, User=Usuario)



# Inicializa o curses e chama a função principal
curses.wrapper(mainScreen)