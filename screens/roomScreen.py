import asyncio
import curses
import threading
import time
from webSockets.client import connect_to_websocket
from webSockets.client import escutar_mensagens_do_servidor
from webSockets.client import wrapper_escutar_mensagens_do_servidor

from  insrtFunctions.insertUser import *
def createRoomScreen(stdscr, width, height, User):

    charKeeper = ['a']
    counter_messages = [0]
    title = 'Room Chat'
    center_y = 2
    center_x = width // 2
    winType = curses.newwin(3, width-15, height-5, 8)
    winType.addstr(1,1,'mensagem: ')
    winType.box()
    winRoom = curses.newwin(height-8, width-10, 5, 5)
    
    winRoom.box()
    
    stdscr.addstr(center_y, center_x, title)

    stdscr.refresh()
    
    
    threadType = threading.Thread(target=FuncThreadType, args=(charKeeper, winRoom, winType), daemon=True)
    threadCh = threading.Thread(target=FuncThreadgetch, args=(charKeeper, winRoom, winType, User), daemon=True)
    threadWebSocketListener = threading.Thread(target=wrapper_escutar_mensagens_do_servidor, args=(counter_messages, winRoom), daemon=True)
    threadType.start()
    threadCh.start()
    threadWebSocketListener.start()

    # Aguarda o término das threads
    threadType.join()

    threadCh.join()
    
    

    print(charKeeper)




def FuncThreadgetch(charKeeper, winObject, winObject2, User):
    while True:
        key = winObject.getch()
        print(key)
        
        if key == 8:
            delete(charKeeper, winObject2)
            print(charKeeper)
        elif key == 10:
            
            asyncio.run(connect_to_websocket(convertCharKeeper(charKeeper), User))

            writeCharKeeper(charKeeper, winObject2)
            print('okpedro')

            
        else:
            charKeeper.append(chr(key))
            insert(charKeeper, winObject2, chr(key))
        winObject2.refresh()
        
        

def FuncThreadType(charKeeper, winObject, winObject2):
    counter = 0
    while True:

     
        winObject2.clear()
        winObject2.box()
        winObject2.addstr(1, 2, "Mensagem: ")
        counter+=1
        writeCharKeeper(charKeeper, winObject2)
        winObject2.refresh()



        

