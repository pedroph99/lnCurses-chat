import curses


def insert(charKeeper, winObject, key):
    try:
        charKeeper.append(chr(key))
        winObject.addch(1, len(charKeeper)+ 20, chr(key) )
        
        winObject.refresh()
    except:
         pass

def delete(charKeeper, winObject):
    winObject.clear()
    counter = 1;
    if len(charKeeper)> 0:

        charKeeper.pop();
        for x in charKeeper:
            winObject.addch(1, counter+ 20, x )
            counter+=1
        print(charKeeper)
        winObject.refresh()
    
    
def writeCharKeeper(charKeeper, winObject):
    winObject.clear()
    winObject.box()
    counter = 0
    for x in charKeeper:
            winObject.addch(1, counter+ 20, x )
            counter+=1


def convertCharKeeper(charKeeper):
     returned = ''
     for x in charKeeper:
          returned = returned + x
     print(returned)
     return returned