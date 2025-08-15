import time
from pynput.keyboard import Key, Controller, Listener

# --- AQUI VOCÊ CADASTRA SEUS ATALHOS ---
# Versão com atalhos curtos e correção para acentos. Gatilho ";"
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

current_string = []
keyboard = Controller()

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
            # Apaga o atalho
            for _ in range(len(trigger)):
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
                time.sleep(0.005)

            # Digita o texto letra por letra (MÉTODO CORRIGIDO)
            for char in replacement:
                keyboard.press(char)
                keyboard.release(char)
                time.sleep(0.005)

            current_string = []
            break

def on_release(key):
    if key == Key.esc:
        return False

# Inicia o listener para monitorar o teclado
with Listener(on_press=on_press, on_release=on_release) as listener:
    print("Software de atalhos iniciado (v1.2). Pressione 'Esc' para sair.")
    listener.join()