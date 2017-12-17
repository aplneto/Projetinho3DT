'''
Joguinho em 3D&T Alpha para praticar o uso de dicionários de Python.

12-15-2017
00:06

Bem-vindo a masmorra de treinos do Protetorado do Reino, um RPG no cenário de Tormenta onde você enfrenta hordas de inimigos em um calabouço, em busca do Desbravador, a arma mágica da Deusa.

Opções:
CONTINUAR --> O personagem segue para enfrentar o próximo inimigo, escolhido aleatoriamente dentre um determinado número de inimigos.
SALVAR --> Salva o estado do jogador e o número de inimigos derrotados.
DESISTIR --> Salva um arquivo de Score contendo a pontuação do jogador.

Personagens:
GUERREIRO --> Força 3, Habilidade 2, Resistência 3, Armadura 2, Poder de Fogo 0, Pontos de Vida 20, Pontos de Magia 10
MAGO --> Força 1, Habilidade 3, Resistência 2, Armadura 1, Poder de Fogo 0, Pontos de Vida 10, Pontos de Magia 30
PALADINO --> Força 2, Habilidade 2, Resistência 3, Armadura 2, Poder de Fogo 0, Pontos de Vida 15, Pontos de Magia 15
ARQUEIRO --> Força 1, Habilidade 2, Resistência 2, Armadura 1, Poder de Fogo 3, Pontos de Vida 10, Pontos de Magia 10

Os personagens podem usar as seguintes ações.
GUERREIRO --> Machado; Ataque especial perigoso e poderoso (3 PMs)
MAGO --> Cajado; Arpão (15 PMs), Bola de Fogo (5 PMs), O Crânio Voador de Vladislav (3 PMs)
PALADINO --> Espada; Ataque Vorpal (3 PMs), Cura Mágica (2 PMs), Esconjuro (5 PMs)
ARQUEIRO --> Faca, Arco; Tiro Preciso, Perigoso e Poderoso (4 PMs)

Já os inimigos são:
'''
from random import randint
from masmorra import *
from dummies import *

def Main():
    '''
    Função principal do jogo.
    '''
    global score
    global fim_de_jogo
    PLAYER = {'Nome': 'jogador', 'F':0, 'H':0, 'R':0, 'A':0, 'PdF':0, 'PV':1, 'PM':1, 'ATK':{}, 'Status':'Normal', 'dano': '', 'Ação':ActPlayer, 'Tipo': 'Humano', 'score':0}
    rolar = lambda: randint(1,6)
    testar = (lambda x: rolar() <= x)
    
    def MenuClasse():
        nonlocal PLAYER
        while True:
            print('...')
            comando = input('Arqueiro(a/arqueiro), Guerreiro(g/guerreiro), Mago(m/mago), Paladino(p/paladino).\n...\n').lower()
            print('...')
            if comando.startswith('a'):
                print ('<Arkam Braço Metálico> -- Um antigo ditado diz que um arqueiro carrega um número de vidas em sua aljava, tamanha é a sua precisão.\n'
                       '<Arkam Braço Metálico> Conhecidos por serem silenciosos e mortais, um bom arqueiro só é notado depois que sua fleche atinge seu alvo.')
                print ('<!> Você terá Força 0, Habilidade 2, Resistência 2, Armadura 1, Poder de Fogo 3\n'
                       '<!> 10 PVs, 10 PMs e pode atacar com seu arco.\n'
                       '<!> Além disso, você pode realizar um poderoso disparo que tem mais chances de causar dano crítico e que, quando o faz, causa mais dano que os ataques normais ao custo de 4 PMs.')
                print ('...')
                comando = input('Confirmar (c/confirmar), voltar(v/voltar)').lower()
                if comando.startswith('c'):
                    PLAYER['F'] = 1
                    PLAYER['H'] = 2
                    PLAYER['R'] = 2
                    PLAYER['A'] = 1
                    PLAYER['PdF'] = 3
                    PLAYER['PV'] = 10
                    PLAYER['PM'] = 10
                    PLAYER['MAX'] = (10, 10)
                    PLAYER['dano'] = 'seu arco'
                    PLAYER['ATK'] = {'Arco':{'ATK':Disparar, 'PM':0}, 'Faca':{'ATK':Atacar, 'PM':0},'Golpe Fatal':{'ATK':TiroCerteiro, 'PM':4}}
                    break
                elif comando.startswith('v'):
                    continue
                else:
                    print('...')
                    print('<Arkam Braço Metálico> -- Não entendi. Pode repetir?')
            elif comando.startswith('g'):
                print('<Arkam Braço Metálico> -- Os guerreiros costumam ser a alma de um grupo de aventureiros.\n'
                      '<Arkam Braço Metálico> A força e bravura de um guerreiro pode ser a diferença entre encontrar um tesouro ou ir para ao encontro dos deuses.')
                print('<!> Você terá Força 3, Habilidade 2, Resistência 3, Armadura 2, Poder de Fogo 0\n'
                      '<!> 20 PVs, 10 PMs e usará um machado.\n'
                      '<!> Além disso, você poderá também usar um poderoso golpe que causa muito mais dano por 3 PMs.')
                print('...')
                comando = input('Confirmar (c/confirmar), voltar(v/voltar)').lower()
                if comando.startswith('c'):
                    PLAYER['F'] = 3
                    PLAYER['H'] = 2
                    PLAYER['R'] = 3
                    PLAYER['A'] = 2
                    PLAYER['PV'] = 20
                    PLAYER['PM'] = 10
                    PLAYER['MAX'] = (20, 10)
                    PLAYER['dano'] = 'seu machado'
                    PLAYER['ATK'] = {'Machado':{'ATK':Atacar, 'PM': 0}, 'Golpe Demolidor':{}}
                    break
                elif comando.startswith('v'):
                    continue
                else:
                    print('...')
                    print('<Arkam Braço Metálico> -- Não entendi. Pode repetir?')
            elif comando.startswith('m'):
                print('<Arkam Braço Metálico> -- Em todo lugar de Arton, grandes histórias são contadas sobre magos e seus poderes.'
                      '<Arkam Braço Metálico> -- Com certeza ser um mago requer inteligencia e é uma tarefa difícil... mas nao sei se a masmorra é um bom lugar pra você.')
                print('<!> Você terá Força 1, Habilidade 3, Resistência 2, Armadura 0  e Poder de Fogo 0\n'
                      '<!> 10 PVs, 30 PMs e será capaz de atacar com seu cajado, além das seguintes magias:\n'
                      '<!> Arpão (15 PMs): uma poderosa onda sônica de energia mágica capaz de obliterar um inimigo:\n'
                      '<!> Bola de fogo (6 PMs): uma bola de fogo que explode em uma área, atingindo até três inimigos;\n'
                      '<!> O Crânio Voador de Vladislav (3 PMs): um crânio mágico que explode contra um alvo, ignorando sua Armadura.')
                print('...')
                comando = input('Confirmar (c/confirmar), voltar(v/voltar)').lower()
                if comando.startswith('c'):
                    PLAYER['F'] = 1
                    PLAYER['H'] = 3
                    PLAYER['R'] = 2
                    PLAYER['A'] = 1
                    PLAYER['PV'] = 10
                    PLAYER['PM'] = 30
                    PLAYER['MAX'] = (10, 30)
                    PLAYER['dano'] = 'seu cajado'
                    PLAYER['ATK'] = {'Arpão':{'ATK':Arpao, 'PM':15},'Cajado': {'ATK':Atacar, 'PM': 0}, 'Bola de Fogo': {'ATK': BolaDeFogo, 'PM': 5}}
                    break
                elif comando.startswith('v'):
                    continue
                else:
                    print('...')
                    print('<Arkam Braço Metálico> -- Não entendi. Pode repetir?')
            elif comando.startswith('p'):
                print('<Arkam Braço Metálico> -- Os deuses escolheram você para cumprir uma missão divina em Arton.\n'
                      '<Arkam Braço Metálico> -- Mas será que suas orações serão suficientes para fazê-lo vencer esse desafio? É o que vamos descobrir.')
                print('<!> Você terá Força 2, Habilidade 2, Resistência 3, Armadura 2, Poder de Fogo 0\n'
                      '<!> 15 PVs, 15 PMs e poderá usar sua Espada para ataques simples. Além disso, terá a sua disposição as seguintes magias:\n'
                      '<!> Ataque Vorpal (3 PMs): um poderoso ataque que, em caso de acerto crítico, pode decapitar um inimigo.\n'
                      '<!> Cura mágica (2 PMs): você recupera entre 1 e 6 PVs próprios.\n'
                      '<!> Esconjuro (5 PMs): pode ser usada apenas contra mortos-vivos. Caso tenha sucesso, sua magia bane o alvo, destruindo de uma so vez.')
                print('...')
                comando = input('Confirmar (c/confirmar), voltar(v/voltar)').lower()
                if comando.startswith('c'):
                    PLAYER['F'] = 2
                    PLAYER['H'] = 2
                    PLAYER['R'] = 3
                    PLAYER['A'] = 2
                    PLAYER['PV'] = 15
                    PLAYER['PM'] = 15
                    PLAYER['MAX'] = (15, 15)
                    PLAYER['dano'] = 'sua espada'
                    PLAYER['ATK'] = {'Espada':{'ATK':Atacar, 'PM':0}, 'Cura Mágica':{'ATK':CuraMagica, 'PM':2}, 'Esconjuro':{'ATK': Esconjuro, 'PM': 5}, 'Ataque Vorpal':{'ATK':AtaqueVorpal, 'PM': 3}}
                    break
                elif comando.startswith('v'):
                    continue
                else:
                    print('...')
                    print('<Arkam Braço Metálico> -- Não entendi. Pode repetir?')
                    
    def Atacar(atacante, vitima):
        '''
        Função definida para os ataques fisicos simples, feitos com F.
        '''
        nonlocal rolar
        msg = '{} ataca {} com {}'.format(atacante['Nome'], vitima['Nome'], atacante['dano'])
        dado = rolar()
        ataque = atacante['F']+atacante['H']+dado
        if dado == 6 and (atacante['F'] > 0):
            ataque+=atacante['F']
        dado = rolar()
        defesa = vitima['A'] + vitima['H']+dado
        if dado == 6 and (vitima['A'] > 0):
            defesa +=vitima['A']
        dano = ataque-defesa
        if dano<=0:
            msg += ', mas seu ataque falha.'
        elif dado == 1:
            msg += 'que é atingido em cheio, recebendo {} pontos de dano.'.format(dano)
            vitima['PV'] -= dano
        else:
            msg += ' e causa {} pontos de dano.'.format(dano)
            vitima['PV'] -= dano
        print(msg)
        
    def AtaqueVorpal (atacante, vitima):
        '''
        Função definida para o uso da magia "Ataque Vorpal" do Paladino.
        '''
        nonlocal rolar
        nonlocal testar
        atacante['PM'] -= 3
        print ('Você ora para que os deuses abençoem a lâmina de sua espada e investe contra {}.'.format(vitima['Nome']))
        critico = False
        dadoAtaque = rolar()
        ataque = atacante['F']+atacante['H']+dadoAtaque+1
        if dadoAtaque == 6:
            critico = True
            ataque += atacante['F']+1
        dadoDefesa = rolar()
        defesa = vitima['A']+vitima['H']+dadoDefesa
        if dadoDefesa == 6:
            defesa += vitima['A']
        dano = ataque-defesa
        dano = max(0, dano)
        if (dano != 0) and critico:
            if testar(vitima['R']):
                print('A espada corta o ar em direção a cabeça de {}, que consegue esquivar da lâmina, mas acaba atingido pelo corte que viaja através do vento,\n\
sofrendo {} pontos de dano.'.format(vitima['Nome'], dano))
            else:
                print('Girando seu corpo rapidamente, você consegue separar a cabeça de {} do corpo, que cai inerte no chão.'.format(vitima['Nome']))
                vitima['PV'] = 0
        elif dano!= 0:
            print ('Você brande a espada ferozmente em um giro que corta o ar a sua volta, atingindo {} e causando {} pontos de dano.'.format(vitima['Nome'], dano))
        else:
            print('{} consegue desviar do seu golpe no último instante, dando um salto para trás e saindo ileso do ataque.'.format(vitima['Nome']))
        vitima['PV'] -= dano
        
    def CuraMagica (usuario):
        '''
        Função definida para a magia cura mágica
        '''
        nonlocal rolar
        dado = rolar()
        usuario['PM'] -= 2
        usuario['PV'] = min(usuario['MAX'][0], usuario['PV'] + dado)
        print ('{0} concentra energias mágicas em suas mãos, levando-as ao corpo para amenizar seus ferimentos.'.format(usuario))
        print ('{} recupera {} pontos de vida.'.format(usuario, dado))
        
    def Disparar(atacante, vitima):
        '''
        Função definida para os ataques físicos a distância, feitos com PdF.
        '''
        nonlocal rolar
        msg = '{} dispara {} contra {}'.format(atacante['Nome'], atacante['dano'], vitima['Nome'])
        dado = rolar()
        ataque = atacante['PdF']+atacante['H']+dado
        if dado == 6 and (atacante['F'] > 0):
            ataque+=atacante['PdF']
        dado = rolar()
        defesa = vitima['A'] + vitima['H']+dado
        if dado == 6 and (vitima['A'] > 0):
            defesa +=vitima['A']
        dano = ataque-defesa
        if dano<=0:
            msg += ', mas erra o disparo.'
        elif dado == 1:
            msg += 'que é atingido em cheio, recebendo {} pontos de dano.'.format(dano)
            vitima['PV'] -= dano
        else:
            msg += ' e causa {} pontos de dano.'.format(dano)
            vitima['PV'] -= dano
        print(msg)

    def Esconjuro(atacante, vitima):
        '''
        Função definida para a magia esconjuro, efetiva apenas contra mortos vivos.
        '''
        nonlocal testar
        atacante['PM'] -= 5
        msg ='Depois de uma oração, {} estende as mãos na direção de {}'.format(atacante['Nome'], vitima['Nome'])
        if (testar(vitima['R'])) or (vitima['Tipo'] != 'morto-vivo'):
            msg+=', mas nada acontece.'
        else:
            msg+=', liberando uma grande quantidade de luz que atinge seu alvo em cheio, destruindo-o.'
            vitima['PV'] = 0

    def GolpeDemolidor(atacante, vitima):
        '''
        Função definida para o ataque especial do guerreiro.
        '''
        nonlocal rolar
        atacante['PM'] -= 3
        dado = rolar()
        ataque = dado+atacante['F']+atacante['H']+2
        critico = False
        if dado == 6 or dado == 5:
            critico = True
            ataque += 2*atacante['F']
        dado = rolar()
        defesa = vitima['A']+vitima['H']+dado
        if dado == 6:
            defesa += vitima['A']
        dano = ataque-defesa
        dano = max(0, dano)
        if dano != 0 and critico:
            print('{} gira seu machado com violência, descendo-o rapidamente em um golpe vertical.\n {} É atingido em cheio, sofrendo {} pontos de dano.'.format(atacante['Nome'],vitima['Nome'], dano))
        elif dano!= 0:
            print('() brande seu machado furiosamente contra {}, atingido-o e causando {} pontos de dano.'.format(atacante['Nome'],vitima['Nome'],dano))
        else:
            print('{} avança com o machado em mãos, brandindo-o em um movimento rápido, mas acaba por errar {}, que se esquiva sem dificuldades.'.format(atacante['Nome'], vitima['Nome']))
        vitima['PV'] -= dano
        
    def TiroCerteiro(atacante, vitima):
        '''
        Função definida para o tiro certeiro da classe arqueiro.
        '''
        nonlocal rolar
        dado = rolar()
        atacante['PM'] -= 4
        ataque = atacante['H'] + atacante['PdF'] + dado
        if dado >= 5:
            ataque += 2*atacante['PdF']
        msg = '{} concentra suas energias em {} antes de realizar o disparo fatal.'.format(atacante['Nome'], atacante['dano'])
        print(msg)
        dado = rolar()
        defesa = vitima['H'] + vitima['PdF'] + dado
        dano = ataque - defesa
        if dano <= 0:
            msg = 'No entanto, {} consegue proteger-se do disparo, fazendo {} errar seu alvo.'.format(vitima['Nome'], atacante['Nome'])
        elif dado == 1:
            msg = '{} é atingido em cheio pelo disparo que atravessa seu corpo, causando {} pontos de dano.'.format(vitima['Nome'], dano)
        else:
            msg = '{} é atingo pelo disparo sofrento {} pontos de dano.'.format(vitima['Nome'], dano)
        dano = max(dano, 0)
        vitima['PV'] -= dano
        print(msg)

    def Arpao (atacante, vitima):
        '''
        Função definida para o uso da magia Arpão
        '''
        nonlocal rolar
        atacante['PM'] -= 15
        msg = '{} junta uma grande quantidade de energia mágica em suas mãos e, com o sussurrar\n\
                de algumas palavras mágicas, disparando de suas mãos uma onda roxa na forma de um arpão.'.format(atacante['Nome'])
        print(msg)
        ataque = atacante['H']
        for i in range (6):
            ataque += rolar()
        dado = rolar()
        defesa = vitima['H']+vitima['A']+dado
        dano = ataque-defesa
        if dano <= 0:
            msg = 'Milagrosamente, {} consegue desviar do arpão mágico, saindo ileso do golpe.'.format(vitima['Nome'])
        elif dado == 1:
            msg = '{} é atingido em cheio pelo ataque, sendo arremessado para longe pelo impacto e sofrento {} pontos de dano.'.format(vitima['Nome'], dano)
        else:
            msg = '{} é atingo pelo disparo, sofrendo queimaduras mágicas por todo o corpo e recebendo {} pontos de dano.'.format(vitima['Nome'], dano)
        dano = max(dano, 0)
        vitima['PV'] -= dano
        
    def BolaDeFogo(atacante, vitimas):
        '''
        Função definida para o uso da magia Bola de Fogo.
        '''
        nonlocal rolar
        ataque = atacante['H']+5+rolar()
        atacante['PM'] -= 5
        msg1 = '{} sussurra algumas palavras mágicas e extende as mãos em direção'.format(atacante['Nome'])
        if len(vitimas) == 1:
            msg1 += ' ao inimigo e de suas mãos uma grande bola de fogo é disparada.'
        else:
            msg1 += 'aos inimigos e de suas mãos uma grande bola de fogo é disparada.'
        print(msg1)
        for alvo in vitimas:
            dado = rolar()
            defesa = vitima['H']+vitima['A']+dado
            if (dado == 6) and (vitima['A']>0):
                defesa += vitima['A']
            dano = ataque-defesa
            if dano<=0:
                msg2 = '{} consegue defender-se da bola de fogo, saindo ileso do ataque.'.format(vitima['Nome'])
                print(msg2)
            elif dado == 1:
                msg2 = 'A bola de fogo atinge {} em cheio, causando {} ponto de dano.'.format(vitima['Nome'], dano)
                print(msg2)
                vitima['PV'] -= dano
            else:
                msg2 = 'A bola de fogo explode próxima a {}, causando-lhe {} pontos de dano.'.format(vitima['Nome'], dano)
                print(msg2)
                vitima['PV'] -= dano

    def CranioVoador(atacante, vitima):
        '''
        Função definida para a magia O Crânio Voador de Vladislav.
        '''
        nonlocal rolar
        ataque = atacante['H']+rolar()+rolar()
        atacante['PM'] -= 3
        msg = '{} dispara de suas mãos um horrendo crânio de energia mágica, que voa na direção de seu alvo.'.format(atacante['Nome'])
        print(msg)
        defesa = vitima['H']+rolar()
        dano = ataque-defesa
        if dano <= 0:
            msg = 'O crânio erra o alvo e {} sai ileso do ataque.'.format(vitima['Nome'])
        else:
            msg = '{} é atingido pelo crânio voador, que causa queimaduras mágicas pelo seu corpo.'.format(vitima['Nome'])
            vitima['PV'] -= dano
        print(msg)

    def EncontrarInimigo():  #IA de controle de inimigos
        print('...')
        print('<!>')

    def Jogar():
        '''
        Função definida para o Menu entre as batalhas.
        '''
        global fim_de_jogo
        while True:
            print('...')
            comando = input('Continuar(c/continuar), Salvar(s/salvar), Ajuda(a/ajuda), Gastar Experiência (e/exp), Desistir(d/desistir)\n')
            if comando.startswith('c'):
                break
            elif comando.startswith ('s'):  # Menu de Salvar, lembrar de configurar
                pass
            elif comando.startswith ('a'):  # Instruções da masmorra
                pass
            elif comando.startswith('e'):  # Menu de Experiência
                pass
            elif comando.startswith('d'):
                fim_de_jogo = True
                break
            else:
                print('...')
                print('Escolha um comando válido.')
            
    #  Fichas dos inimigos abaixo:
    ZUMBI = {'Nome': 'Zumbi', 'F':1, 'H':2, 'R':2, 'A':0, 'PdF':0, 'PV':10, 'PM':10, 'Status':'Normal', 'dano': 'suas garras', 'Ação':Grunt, 'Tipo': 'morto-vivo', 'score':5}
    ZUMBI['ATK'] = {'ataque': {'ATK': Atacar, 'PM': 0}}
    ZUMBI['Morte'] = ''

    # Inicio do Jogo
    while True:
        escolha = input('Novo Jogo(n/novo), Continuar(c/continuar), Sair(s/sair)\n').lower()
        if escolha.startswith('c'):
            pass
        elif escolha.startswith('s'):
            break
        elif escolha.startswith('n'):
            print('<!> Bem-vindo, aventureiro, ao desafio da masmorra do protetorado do reino.\n\n\n')
            PLAYER['Nome'] = input('<Arkam Braço Metálico> -- Então você acha que é capaz de vencer o desafio? Bom, isso é o que vamos ver.\n'
                                   '<Arkam Braço Metálico> -- Antes de entrar, diga-me, qual seu nome?\n...\n').capitalize()
            print('...')
            print('<Arkam Braço Metálico>: -- Bem-vindo, {}. A masmorra está pronta para recebê-lo, mas pelo visto você ainda não está pronto para prosseguir.\n'
                  '*Arkam lhe aponta uma mesa com armas e equipamentos de diversos tipos.*'
                  '\n<Arkam Braço Metálico> -- Na masmorra você precisa usar equipamentos especiais, feitos para as mais diversas classes de aventureiros. Escolha com sabedoria.'.format(PLAYER['Nome']))
            MenuClasse()
            print('...')
            print('<!>Arkam permite que você pegue seus equipamentos e o guia através de um corredor escuro até uma porta de madeira velha.\n'
                  '<!> A porta está protegida por uma barra de metal brilhante, provavelmente mágico, que emite uma fraca luz azul.')
            print('<Arkam Braço Metálico> -- É aqui que nos separamos, {}. Espero encontrá-lo do outro lado da masmorra. Hahaha'
                  '<Arkam Braço Metálico> -- Boa sorte.'.format(PLAYER['Nome']))
            print('<!> A porta se abre e você a entra, ouvindo o rangido e a batida da porta fechando-se logo atrás de você.')
            while not fim_de_jogo:
                Jogar()
                if not fim_de_jogo:
                    inimigos = EncontrarInimigo()
                    print('...')
                    Combate(PLAYER, inimigos)
        else:
            print('<!> Comando inválido. Tente novamente.')

Main()
