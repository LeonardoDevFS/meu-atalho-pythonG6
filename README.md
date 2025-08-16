# ⚡ Meu Software de Atalhos (Text Expander)

Um simples e eficiente **software de expansão de texto** que roda em segundo plano no Windows.  
Crie atalhos curtos para expandir em frases ou parágrafos completos, economizando tempo e aumentando a produtividade.

Este projeto foi desenvolvido em **Python** e empacotado em um executável (`.exe`) para portabilidade e facilidade de uso.

---

## ✨ Funcionalidades
- **Roda em Segundo Plano**: Inicie o programa e esqueça. Ele funciona em qualquer janela ou campo de texto.  
- **Ícone na Bandeja do Sistema**: O programa fica discretamente na bandeja (perto do relógio). Clique com o botão direito para sair.  
- **Portátil**: Não requer instalação. Basta executar o arquivo `.exe`.  
- **Customizável**: Adicione ou edite seus próprios atalhos diretamente no código-fonte em Python.  

---

## 🚀 Como Usar
1. Baixe o arquivo **atalhos.exe** na seção de [Releases](#) *(link de exemplo)*.  
2. Execute o `atalhos.exe`. O programa iniciará em segundo plano e um ícone aparecerá na bandeja do sistema.  
3. Abra qualquer editor de texto (Bloco de Notas, navegador, etc.) e digite um dos gatilhos da lista abaixo para ver a mágica acontecer.  

⚠️ **Aviso:** Softwares antivírus podem sinalizar o programa como suspeito, pois ele monitora a digitação (comportamento semelhante a um *keylogger*).  
Isso é um **falso positivo**. Adicione uma exceção no seu antivírus para permitir a execução do programa.  

---

## 📋 Lista de Atalhos

| **Gatilho**   | **Texto de Substituição** |
|---------------|----------------------------|
| `;detectar`   | Você poderia me explicar melhor esse problema e informar em quais equipamentos ele aconteceu? (como celulares, computadores, TVs ou outros) Assim vou conseguir entender melhor a situação e encontrar a solução mais adequada para você. |
| `;autenticado`| Notei que o seu roteador está ligado há bastante tempo sem desligar. Com o uso contínuo, ele acumula memória cache, o que pode causar lentidão ou até a desconexão de alguns aparelhos. Recomendo desligar o roteador da tomada por cerca de 1 minuto e depois ligá-lo novamente. Isso ajuda a limpar a memória e melhorar o desempenho da conexão. |
| `;velocidade` | De acordo com a Resolução nº 574/2011 da ANATEL, as operadoras devem garantir ao consumidor: Velocidade instantânea mínima: pelo menos 20% da velocidade contratada em qualquer momento da medição. Velocidade média mínima: pelo menos 60% da velocidade contratada ao longo do mês. Esses parâmetros são definidos para assegurar a qualidade mínima da sua conexão de internet. |
| `;24g5g`      | O seu roteador transmite duas redes Wi-Fi diferentes: 2.4 GHz e 5 GHz. A rede 2.4 GHz é uma tecnologia mais antiga, com velocidade limitada geralmente entre 20 Mb e 50 Mb... |
| `;tvbox`      | Em relação à TV Box, na maioria dos casos você está recebendo um sinal não homologado pela Anatel, ou seja, um terceiro está repassando o conteúdo de forma irregular... |
| `;tardefinal` | Tudo certo então! Estarei encerrando seu atendimento por aqui, tudo bem? Desejo que tenha uma excelente tarde! |
| `;manhafinal` | Tudo certo então! Estarei encerrando seu atendimento por aqui, tudo bem? Desejo que tenha uma excelente manhã! |
| `;ordem`      | Sua ordem de serviço foi aberta com os dias e horários indicados como prazos, ok? Por enquanto, basta apenas aguardar a equipe técnica no local. |

---

## 🔧 Como Compilar a Partir do Código-Fonte (Para Desenvolvedores)

### 📌 Pré-requisitos
- Python 3.x instalado  

## 📋 Instale as dependências para criar sua versão:
py -m pip install pynput pillow pystray pyinstaller

##🏗️ Compile o Executável
py -m PyInstaller --onefile --windowed --add-data "icone.png;." atalhos.py

### 📥 Clone o Repositório
```bash
git clone https://github.com/LeonardoDevFS/meu-atalho-pythonG6
cd seu-repositorio
