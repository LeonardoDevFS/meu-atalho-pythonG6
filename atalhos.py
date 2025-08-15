import time
import threading
from pynput.keyboard import Key, Controller, Listener
from PIL import Image
import pystray

# --- AQUI VOCÊ CADASTRA SEUS ATALHOS ---
shortcuts = {
    ";detectar": """Você poderia me explicar melhor esse problema e informar em quais equipamentos ele aconteceu? (como celulares, computadores, TVs ou outros) Assim vou conseguir entender melhor a situação e encontrar a solução mais adequada para você.""",
    ";autenticado": """Notei que o seu roteador está ligado há bastante tempo sem desligar.Com o uso contínuo, ele acumula memória cache, o que pode causar lentidão ou até a desconexão de alguns aparelhos. Recomendo desligar o roteador da tomada por cerca de 1 minuto e depois ligá-lo novamente. Isso ajuda a limpar a memória e melhorar o desempenho da conexão.""",
    ";velocidade": """De acordo com a Resolução nº 574/2011 da ANATEL, as operadoras devem garantir ao consumidor: Velocidade instantânea mínima: pelo menos 20% da velocidade contratada em qualquer momento da medição. Velocidade média mínima: pelo menos 60% da velocidade contratada ao longo do mês. Esses parâmetros são definidos para assegurar a qualidade mínima da sua conexão de internet.""",
    ";24g5g": """O seu roteador transmite duas redes Wi-Fi diferentes: 2.4 GHz e 5 GHz. A rede 2.4 GHz é uma tecnologia mais antiga, com velocidade limitada geralmente entre 20 Mb e 50 Mb. Ela é compatível com praticamente todos os dispositivos, antigos e novos, e possui maior alcance, sendo ideal para locais mais distantes do roteador. A rede 5 GHz é mais moderna e rápida, podendo alcançar a velocidade máxima suportada pelo roteador e pelo dispositivo conectado. No entanto, possui alcance menor e alguns aparelhos mais antigos não conseguem detectá-la. Para testes de velocidade mais precisos, o ideal é conectar o computador ou notebook via cabo de rede e verificar se ele suporta velocidades acima de 100 Mb.""",
    ";tvbox": """Em relação à TV Box, na maioria dos casos você está recebendo um sinal não homologado pela Anatel, ou seja, um terceiro está repassando o conteúdo de forma irregular. Esse tipo de sinal costuma apresentar travamentos e instabilidade. Para verificar se o problema é realmente na sua conexão, faça um teste abrindo um vídeo no YouTube ou na Netflix. Caso o vídeo não trave nenhuma vez, possivelmente o problema está no TV Box ou no sinal que está sendo repassado.""",
    ";tardefinal": "Tudo certo então! Estarei encerrando seu atendimento por aqui, tudo bem? Desejo que tenha uma excelente tarde!",
    ";manhafinal": "Tudo certo então! Estarei encerrando seu atendimento por aqui, tudo bem? Desejo que tenha uma excelente manhã!",
    ";ordem": "Sua ordem de serviço foi aberta com os dias e horários indicados como prazos, ok? Por enquanto, basta apenas aguardar a equipe técnica no local."
}
# -----------------------------------------

# --- LÓGICA DO MONITOR DE TECLADO (A MESMA DE ANTES) ---
current_string = []
keyboard = Controller()
listener = None # Vamos controlar o listener globalmente

def on_press(key):
    global current_string
    try:
        current_string.append(key.char)
    except AttributeError:
        pass
    if len(current_string) > 50:
        current_string.pop(0)
    for trigger, replacement in shortcuts.items():
        typed_str = "".join(current_string)
        if typed_str.endswith(trigger):
            for _ in range(len(trigger)):
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
                time.sleep(0.005)
            for char in replacement:
                keyboard.press(char)
                keyboard.release(char)
                time.sleep(0.005)
            current_string = []
            break

# Função que inicia o monitoramento do teclado
def start_keyboard_listener():
    global listener
    # A tecla ESC não fecha mais o programa, o menu do ícone fará isso
    listener = Listener(on_press=on_press)
    listener.start()
    print("Monitor de teclado iniciado.")

# --- LÓGICA DO ÍCONE DA BANDEJA DO SISTEMA ---

# Função para ser chamada quando o botão "Sair" do menu for clicado
def exit_action(icon, item):
    print("Saindo...")
    if listener and listener.is_alive():
        listener.stop() # Para o monitor de teclado
    icon.stop()       # Para o ícone da bandeja

# Função principal que configura e roda tudo
def main():
    # Carrega a imagem do ícone
    try:
        image = Image.open("icone.png")
    except FileNotFoundError:
        print("Erro: Arquivo 'icone.png' não encontrado. Certifique-se de que ele está na mesma pasta do script.")
        return

    # Cria o menu que aparecerá ao clicar com o botão direito
    menu = (pystray.MenuItem('Sair', exit_action),)

    # Cria o objeto do ícone
    icon = pystray.Icon("Atalhos", image, "Meu Software de Atalhos", menu)

    # Inicia o monitor de teclado em uma thread separada
    keyboard_thread = threading.Thread(target=start_keyboard_listener)
    keyboard_thread.daemon = True # Permite que o programa feche mesmo que a thread esteja rodando
    keyboard_thread.start()
    
    print("Ícone da bandeja iniciado. Clique com o botão direito para sair.")
    # Mostra o ícone. Esta linha vai "travar" o programa aqui, mantendo o ícone visível.
    icon.run()

# Roda a função principal quando o script é executado
if __name__ == '__main__':
    main()