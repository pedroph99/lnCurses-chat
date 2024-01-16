import threading
import time

def funcao1():
    for _ in range(5):
        print("Função 1")
        time.sleep(1)

def funcao2():
    for _ in range(5):
        print("Função 2")
        time.sleep(1)

# Criação das threads
thread1 = threading.Thread(target=funcao1)
thread2 = threading.Thread(target=funcao2)

# Inicia as threads
thread1.start()
print('INICIANDO THREAD2')
thread2.start()

# Aguarda o término das threads
thread1.join()
thread2.join()

print("Programa principal finalizado.")