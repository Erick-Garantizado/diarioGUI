# Diário

Um diário para anotar e relembrar os acontecimentos do dia a dia.
* Biblioteca: _PySimpleGUI_
* Banco de dados: _sqlite_

## Tela principal
![image](https://user-images.githubusercontent.com/66915867/160296264-c22befd6-2f55-4813-9814-0159af2ec20d.png)
\
Na tela principal o usuário é recebido com uma mensagem de boas vindas. \
Em cima tem um menu [Opções e Ajuda]. \
Ao clicar no menu [Opções] tem as opções de cadastro e login.
![image](https://user-images.githubusercontent.com/66915867/160296442-975815c6-41cd-435c-a360-c53c4705ee49.png)

## Tela de cadastro
![image](https://user-images.githubusercontent.com/66915867/160296639-31765598-e342-49da-84ad-09f17b53d288.png)
\
Clicando em [Cadastro] abre-se a janela de cadastro pedindo nome, senha e confirmação da senha. \
Após o preenchimento correto dos campos e clicar no botão [Cadastrar] é confirmado o cadastro. \
![image](https://user-images.githubusercontent.com/66915867/160296655-3958df9f-c9f9-4e1c-b9b9-19571c8fa719.png)

## Tela de login
![image](https://user-images.githubusercontent.com/66915867/160297051-467d56fe-ba22-41c4-8133-eff878cdff16.png)
\
Clicando em [Login] abre-se a janela de login pedindo nome e senha. \
Após o preenchimento correto dos campos e clicar no botão [Entrar] o usuário poderá entrar no campo de usuário. \
OBS.: é importante colocar os campos nome e senha exatamente como foi cadastrado. \
Ex.: Gabriel != gabriel ('G' maiúsculo é diferente de 'g' minúsculo)

## Área do usuário
![image](https://user-images.githubusercontent.com/66915867/160297153-0ecf97ce-2e1a-4b09-8835-2a38d747d6d7.png)
\
Na janela de área do usuário tem o nome do usuário logado no canto superior esquerdo, no meio da tela uma mensagem motivacional gerada a cada login e os botões [Escrever], [Ler] e [Voltar]. \
O botão [Escrever] abre a janela para o usuário escrever suas mensagens. \
O botão [Ler] abre a janela para o usuário ler suas mensagens. \
O botão [Voltar] desloga o usuário atual voltando para a tela principal.

## Tela para escrever
![image](https://user-images.githubusercontent.com/66915867/160297457-0bdc3a76-28a6-4e10-ba2a-c6f194aa77b0.png)
\
Na janela para escrever as mensagens tem o campo titulo, que é obrigatório, o campo onde será inserido a mensagem e os botões [Salvar] e [Voltar]. \
Ao clicar no botão [Salvar] aparecerá um aviso de que a mensagem foi salva. 
![image](https://user-images.githubusercontent.com/66915867/160297566-a2e96e37-4e70-43f2-bd60-9a2b22cb1203.png)
\
Ao clicar no botão [Voltar] volta para a área do usuário.

## Tela de leitura
![image](https://user-images.githubusercontent.com/66915867/160297880-902f912b-8775-42fa-8f5f-001a790481fe.png)
\
Na tela de leitura aparece a listagem de mensagens salvas pelo usuário com número, titulo e data, o campo para por o numero da mensagem a ser lida e os botões [Visualizar] e [Voltar]. \
Ao colocar o número da mensagem e clicar no botão [Visualizar] aparecerá a mensagem por completo em outra janela. \
![image](https://user-images.githubusercontent.com/66915867/160298034-4bb10340-3f28-4767-a30a-35025513549b.png)
