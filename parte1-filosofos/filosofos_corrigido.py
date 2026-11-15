import threading
import time
import random

numero_filosofos = 5
garfos = [threading.Lock() for _ in range(numero_filosofos)]

def filosofo(id):
    esquerda = id
    direita = (id + 1) % numero_filosofos

    primeiro = min(esquerda, direita)
    segundo = max(esquerda, direita)

    while True:
        print(f"Filósofo {id} está pensando")
        time.sleep(random.uniform(0.5, 1.5))

        print(f"Filósofo {id} está com fome")

        garfos[primeiro].acquire()
        print(f"Filósofo {id} pegou o primeiro garfo ({primeiro})")

        garfos[segundo].acquire()
        print(f"Filósofo {id} pegou o segundo garfo ({segundo})")

        print(f"Filósofo {id} está comendo")
        time.sleep(random.uniform(0.5, 1.0))

        garfos[segundo].release()
        garfos[primeiro].release()
        print(f"Filósofo {id} liberou os garfos")

for i in range(numero_filosofos):
    threading.Thread(target=filosofo, args=(i,), daemon=True).start()

time.sleep(20)
print("fim.")