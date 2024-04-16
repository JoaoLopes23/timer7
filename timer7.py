import logging
import threading
import time

# Configuração do logger
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Função a ser chamada pelo timer
def timer7():
    logging.info('timer7 foi acionado')

# Função para acionar o timer a cada 30 segundos
def start_timer():
    while True:
        timer7()
        time.sleep(30)

# Iniciando o timer em uma thread separada
timer_thread = threading.Thread(target=start_timer)
timer_thread.daemon = True  # A thread será encerrada quando o programa principal terminar
timer_thread.start()

# Mantém o programa principal em execução para que o timer continue sendo acionado
while True:
    pass
