import PySimpleGUI as sg

import back
import tela


DB = "diario_banco.db"

diario = tela.Janela((800, 600), 'Diário', back.FONTE, perguntar_saida=True)

def muda_tema(pagina, tema):
    """ Muda as cores do programa."""

    if pagina == 'primeira_tela':
        sg.theme(tema)
        t, w = diario.primeira_tela()
    elif pagina == 'cadastro':
        sg.theme(tema)
        t, w = diario.cadastro()
    elif pagina == 'login':
        sg.theme(tema)
        t, w = diario.login()
    return t, w


if not back.existe_banco(DB):
    back.criar_banco(DB)

sg.theme('tan')

wInicial, wCadastro, wLogin, wArea_usuario, wEscrever, wLer = diario.primeira_tela(), None, None, None, None, None

while True:
    window, event, values = sg.read_all_windows()

    # Fechar programa
    if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == "Sair" or event == sg.WIN_CLOSED) and back.saida():
        break

    # Sobre o programa
    elif event == 'Sobre':
        back.sobre()

    # Tela de cadastro
    elif event == 'Cadastro':
        if window == wInicial:
            wInicial.hide()
        elif window == wLogin:
            wLogin.hide()

        if not wCadastro:
            wCadastro = diario.cadastro()
        else:
            wCadastro.un_hide()

    # Tela de login
    elif event == 'Login':
        if window == wInicial:
            wInicial.hide()
        elif window == wCadastro:
            wCadastro.hide()

        if not wLogin:
            wLogin = diario.login()
        else:
            wLogin.un_hide()

    # Logar em uma conta
    elif event == 'Entrar':
        existe, id_user, nome = back.login(values, DB)
        if existe:
            wLogin.hide()
            wLogin.find_element('-LOG_NOME-').Update('')
            wLogin.find_element('-LOG_SENHA-').Update('')
            wArea_usuario = diario.area_usuario(nome)

    # Tela onde escreve mensagem
    elif event == 'Escrever':
        wArea_usuario.hide()
        wEscrever = diario.escrever()

    # Botão ler da área do usuário
    elif event == 'Ler':
        lista, titulos = back.ler(DB, id_user)
        wArea_usuario.hide()
        wLer = diario.ler(lista)

    # Cadastrar o usuário no banco de dados
    elif event == 'Cadastrar':
        back.cadastrar(values, DB)

    # Salvar mensagem no banco de dados
    elif event == 'Salvar':
        salvou = back.salvar_msg(values, DB, id_user)
        if salvou:
            window.find_element('-TITULO-').Update('')
            window.find_element('-TEXTO-').Update('')

    # Voltar pra área do usuário
    elif window == wEscrever and event == 'Voltar':
        wEscrever.hide()
        wArea_usuario.un_hide()

    elif window == wLer and event == "Voltar":
        wLer.hide()
        wArea_usuario.un_hide()

    # Voltar pra tela principal
    elif window == wArea_usuario and event == 'Voltar':
        if wLer:
            wLer.close()
        if wEscrever:
            wEscrever.close()
        wArea_usuario.close()
        wInicial.un_hide()
        id_user = nome = None

    # Botão visualizar da tela ler
    elif event == "Visualizar":
        back.visualizar(values, DB, titulos)
        window.find_element('-NUM-').Update('')

    # Trocar tema das janelas
    elif event == 'Dark':
        if sg.theme() == 'Dark':
            pass
        else:
            window.close()
            tela, window = muda_tema(tela, 'dark')
    elif event == 'Light':
        if sg.theme() == 'Tan':
            pass
        else:
            window.close()
            tela, window = muda_tema(tela, 'Tan')
    elif event == 'Lavanda':
        if sg.theme() == 'LightPurple':
            pass
        else:
            window.close()
            tela, window = muda_tema(tela, 'LightPurple')
    elif event == 'Azul':
        if sg.theme() == 'Python':
            pass
        else:
            window.close()
            tela, window = muda_tema(tela, 'Python')
