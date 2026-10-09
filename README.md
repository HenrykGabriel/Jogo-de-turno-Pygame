# The Last Vanguard

## Objetivo

O **The Last Vanguard** é um jogo desenvolvido em Python com a biblioteca Pygame, baseado em combates por turnos. O jogador enfrenta diferentes inimigos, escolhe suas ações durante os combates e aprimora os atributos de seu personagem ao longo da progressão.

O projeto utiliza elementos visuais em pixel art, incluindo cenários, personagens, inimigos e cartas de atributos.

## Funcionalidades

* **Seleção de personagem:** escolha da classe do jogador.
* **Combate por turnos:** o jogador realiza suas ações e, em seguida, os inimigos atacam.
* **Sistema de ataque:** permite escolher um inimigo como alvo.
* **Sistema de defesa:** permite utilizar escudo para reduzir o impacto dos ataques recebidos.
* **Atributos do personagem:** gerenciamento de vida, dano, dano crítico, chance de dano crítico, esquiva e escudo.
* **Cartas de atributos:** permitem melhorar as características do personagem durante a progressão.
* **Diferentes cenários:** ambientes com identidades visuais próprias.
* **Inimigos e chefes:** enfrentamento de diferentes adversários ao longo das fases.
* **Interface de combate:** exibição de informações como barras de vida, escudo e resultados das ações.
* **Sistema de vitória e derrota:** identificação do resultado dos combates.

## Controles

O jogo utiliza o ponteiro para interagir com os elementos da interface.

**Requisito:** é necessário ter um dispositivo apontador, como um mouse ou o touchpad de um notebook, para interagir com a interface do jogo.

## Tecnologias utilizadas

* **Python 3.13.14:** linguagem de programação utilizada no desenvolvimento.
* **Pygame:** biblioteca utilizada para criar a interface gráfica e as mecânicas do jogo.
* **Visual Studio Code (VS Code):** editor utilizado para escrever, executar e depurar o código.
* **Git e GitHub:** ferramentas utilizadas para controle de versão e armazenamento do projeto.

## Como executar o projeto

### 1. Instalar uma IDE

Instale uma IDE ou editor de código compatível com Python. Durante o desenvolvimento deste projeto, foi utilizado o Visual Studio Code.

Site oficial: https://code.visualstudio.com/

### 2. Instalar o Python

Instale o **Python 3.13.14**, versão utilizada durante o desenvolvimento do projeto.

Site oficial: https://www.python.org/downloads/

Após a instalação, abra o terminal e verifique se o Python está disponível:

```bash
python --version
```

### 3. Instalar as extensões do VS Code

Caso utilize o Visual Studio Code, instale as seguintes extensões:

* **Python:** fornece suporte à linguagem Python no editor.
* **Python Debugger:** permite executar e depurar o código, facilitando a identificação de erros.

As extensões podem ser encontradas na seção **Extensions** do VS Code.

### 4. Baixar e extrair o projeto

Acesse o repositório do projeto no GitHub e baixe os arquivos no formato ZIP.

Em seguida:

1. Localize o arquivo ZIP baixado.
2. Extraia todos os arquivos para uma pasta de sua preferência.
3. Abra o Visual Studio Code.
4. Selecione **File → Open Folder** e abra a pasta extraída do projeto.

A estrutura principal deverá ser semelhante a esta:

```text
The-Last-Vanguard/
├── assets/
├── src/
│   └── main.py
├── .gitignore
├── README.md
└── requirements.txt
```

A pasta `assets` contém os recursos utilizados pelo jogo, enquanto a pasta `src` contém o código-fonte.

**Importante:** mantenha a estrutura original de pastas e arquivos para evitar problemas com os caminhos das imagens e dos demais recursos do jogo.

### 5. Instalar o Pygame

No Visual Studio Code, abra o terminal integrado em **Terminal → New Terminal**.

Execute o seguinte comando:

```bash
pip install pygame
```

Aguarde até que a instalação seja concluída.

Como alternativa, para instalar as dependências listadas no arquivo `requirements.txt`, execute:

```bash
python -m pip install -r requirements.txt
```

### 6. Executar o jogo

Depois de instalar as dependências:

1. No explorador de arquivos do VS Code, abra a pasta `src`.
2. Abra o arquivo `main.py`.
3. Selecione o interpretador Python 3.13.14, caso seja solicitado.
4. Para iniciar o jogo, utilize a opção de execução do Python.
5. Para executar em modo de depuração, abra **Run and Debug** ou pressione `F5`, conforme a configuração do VS Code.

O arquivo `main.py` é o ponto de entrada do jogo.

## Organização do projeto

* **`assets/`**: armazena imagens e outros recursos utilizados pelo jogo.
* **`src/`**: contém o código-fonte Python, incluindo o arquivo principal `main.py`.
* **`.gitignore`**: define os arquivos e diretórios que não devem ser enviados ao Git.
* **`README.md`**: apresenta informações sobre o projeto e instruções de execução.
* **`requirements.txt`**: lista as bibliotecas externas necessárias para executar o projeto.

## Integrantes

* Henryk Gabriel Lara Fabiano
* David Fernando Ferreira Moura

## Observações

Este projeto foi desenvolvido com finalidade acadêmica, utilizando Python e Pygame. Para executar o jogo corretamente, é necessário instalar as dependências e manter os arquivos e diretórios na estrutura original do projeto.
