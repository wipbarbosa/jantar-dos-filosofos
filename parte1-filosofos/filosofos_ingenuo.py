import threading
import time
import random

numero_filosofos = 5
garfos = [threading.Lock() for _ in range(numero_filosofos)]

def filosofo(id):
    esquerda = id
    direita = (id + 1) % numero_filosofos

    while True:
        print(f"Filósofo {id} está pensando")
        time.sleep(random.uniform(0.5, 1.5))

        print(f"Filósofo {id} está com fome")

        garfos[esquerda].acquire()
        print(f"Filósofo {id} pegou o garfo esquerdo")

        time.sleep(0.1)

        garfos[direita].acquire()
        print(f"Filósofo {id} pegou o garfo direito")

        print(f"Filósofo {id} está COMENDO")
        time.sleep(random.uniform(0.5, 1.0))

        garfos[direita].release()
        garfos[esquerda].release()
        print(f"Filósofo {id} liberou os garfos")

for i in range(numero_filosofos):
    threading.Thread(target=filosofo, args=(i,), daemon=True).start()

time.sleep(20)# Mantém o programa rodando
print("Fim.")