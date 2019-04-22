# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Ana Clara Carneiro de Freitas, anaccf5@insper.edu.br
# - aluno B: Igor Figueiredo, igorf1@insper.edu.br

import json

def carregar_cenarios():
    #Dicionário
    with open('cenarios_json.txt','r') as arquivo:
        texto = arquivo.read()
    cenarios = json.loads(texto)
    
    nome_cenario_atual = "saguão 1"
    return cenarios, nome_cenario_atual

def main():
    print("------------------")
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    inventario=[]
    game_over = False
    while not game_over:
        
        cenario_atual = cenarios[nome_cenario_atual]
        
        #Imprimindo o cenário
        print("-"*len(cenario_atual["titulo"]))
        print(cenario_atual["titulo"])
        print("-"*len(cenario_atual["titulo"]))
        print(cenario_atual["descricao"])
        print()
        
        #Imprimindo as opções
        print("essas são as opções que você possui:")
        opcoes = cenario_atual['opcoes']
        print("-------------------")
        for k,v in (cenario_atual["opcoes"]).items():
            print (k,":",v)
        print("-------------------")
                        
        if len(opcoes) == 0:
            print("Acabaram-se suas opções!")
            game_over = True
        else:
            escolha = input("para onde deseja ir ? ")
            if escolha in opcoes:
                cenario_atual = escolha
                nome_cenario_atual= cenario_atual
                    
            tentativa=0
            while escolha not in opcoes:
                print("-------------------")
                print("reveja suas opções")
                escolha = input("Escolha novamente, para onde deseja ir?   ")  
                print("-------------------")
                tentativa+=1
                #Garantindo as opções ao jogar    
                if tentativa == 1:
                    print("essa opção não existe")
                    print()
                    print("-------------------")
                    print("Essas são suas opcões:")
                    print()
                    for k,v in (cenario_atual["opcoes"]).items():
                        print (k,":",v)
                    tentativa=-1
                    #Dica
                    print()
                    print("Dica: digite apenas o nome da sala")
                    print("Exemplo: 'nome da sala 1'")
                    
        if escolha in opcoes:
            cenario_atual = escolha
            nome_cenario_atual = cenario_atual
            
            #charada
            tries=1
            if escolha == "charada":
                print("----------------")
                print("A grande charada")
                print("----------------")
                print("Ai vai a charada: ")
                print("Qual é o animal que caminha sobre quatro pernas de ")
                print("manhã, duas pernas durante a tarde e três pernas a noite?")
                resposta = input("digite a resposta da charada:  ")
                print("tentativas = {}".format(tries))
                while escolha == "charada":
                    if resposta == "homem" or resposta == "ser humano":
                        cenario_atual = "bilhete"
                        print()
                        print('-------------------')
                        print("parabéns! Você acertou a charada feita por Humberto em {} tentativas"
                              " e, com isso, você recebe um prêmio... ".format(tries))
                        print()
                        print("Um bilhete!")
                        print("Será essa a próxima pista para encontrar Raul?")
                        print('-------------------')
                            
                        #Inventario
                        print('você deseja adcionar o bilhete ao inventario?')
                        bilhete=input("sim ou não?")
                            
                        if bilhete == "sim":
                            inventario.append('bilhete')
                            print('voce adcionou o bilhete ao seu inventario')
                            print("agora possui os seguintes items em seu inventario:{}".format(inventario))
                        else:
                            print('você decidiu apenas ler o bilhete rapidamente para'
                                  'salvar Raul o mais rápido possivel')
                                    
                        print()
                        print("-"*len(cenarios[cenario_atual]["titulo"]))
                        print(cenarios[cenario_atual]["titulo"])
                        print("-"*len(cenarios[cenario_atual]["titulo"]))
                        print(cenarios[cenario_atual]["descricao"])
                        print()
                        
                        print("essas são as opções que voçê possui: ")
                        opcoes = cenarios[cenario_atual]['opcoes']
                        print("-------------------")
                        for k,v in (cenarios[cenario_atual]["opcoes"]).items():
                            print (k,":",v)
                        print("-------------------")
                            
                        if len(opcoes) == 0:
                            print("Acabaram-se suas opções!")
                            game_over = True
                        else:
                            escolha = input("para onde deseja ir ?")
                            if escolha in opcoes:
                                cenario_atual = escolha
                                nome_cenario_atual= cenario_atual
                                
                            tentativa=0
                            while escolha not in opcoes:
                                print("-------------------")
                                print("reveja suas opções")
                                escolha = input("Escolha novamente, para onde deseja ir?   ")  
                                print("-------------------")
                                tentativa+=1
                                #Garantindo as opções ao jogar    
                                if tentativa == 1:
                                    print("essa opção não existe")
                                    print()
                                    print("-------------------")
                                    print("Essas são suas opcões:")
                                    print()
                                    for k,v in (cenario_atual["opcoes"]).items():
                                        print (k,":",v)
                                    tentativa=-1
                                    #Dica
                                    print()
                                    print("Dica: digite apenas o nome da sala")
                                    print("Exemplo: 'nome da sala 1'")
                                    
                        if escolha in opcoes:
                            cenario_atual = escolha
                            nome_cenario_atual = cenario_atual
                        
                    if resposta != "homem" or resposta != "ser humano":
                        print("essa não é a resposta correta!")
                        print("tente novamente")
                        print()
                        resposta = input("qual a resposta da charada? ")
                        tries+=1
                        print("tentativas = {}".format(tries))
                    
            #Chave
            if escolha == "livro 3":
                    print()
                    print("-"*len(cenarios[cenario_atual]["titulo"]))
                    print(cenarios[cenario_atual]["titulo"])
                    print("-"*len(cenarios[cenario_atual]["titulo"]))
                    print(cenarios[cenario_atual]["descricao"])
                    print()
                    
                    inventario.append('chave')
                    print('voce decidiu adcionar a chave ao seu inventario')
                    print("agora possui os seguintes items em seu inventario:{}".format(inventario))
                    
                    print("essas são as opções que voçê possui: ")
                    opcoes = cenarios[cenario_atual]['opcoes']
                    print("-------------------")
                    for k,v in (cenarios[cenario_atual]["opcoes"]).items():
                        print (k,":",v)
                    print("-------------------")
                        
                    if len(opcoes) == 0:
                        print("Acabaram-se suas opções!")
                        game_over = True
                    else:
                        escolha = input("para onde deseja ir ?")
                        if escolha in opcoes:
                            cenario_atual = escolha
                            nome_cenario_atual= cenario_atual
                            
                        tentativa=0
                        while escolha not in opcoes:
                            print("-------------------")
                            print("reveja suas opções")
                            escolha = input("Escolha novamente, para onde deseja ir?   ")  
                            print("-------------------")
                            tentativa+=1
                            #Garantindo as opções ao jogar    
                            if tentativa == 1:
                                print("essa opção não existe")
                                print()
                                print("-------------------")
                                print("Essas são suas opcões:")
                                print()
                                for k,v in (cenario_atual["opcoes"]).items():
                                    print (k,":",v)
                                tentativa=-1
                                #Dica
                                print()
                                print("Dica: digite apenas o nome da sala")
                                print("Exemplo: 'nome da sala 1'")
                    if escolha in opcoes:
                        cenario_atual = escolha
                        nome_cenario_atual = cenario_atual
            
            #Teletrasporte
            if escolha == "sala":
                print()
                print("----------------------------------")
                print("Bem vindo a sala de teletransporte")
                print("----------------------------------")
                print()
                print("você por ir diretamente para outro sala. Basta apenas "
                      "digitar o nome da sala desejada ")
                print()
                print("DICA: digite apenas o nome da sala sem numeros")
                sala = input("Digite para onde você quer ir: ")
                if sala == "banheiro":
                    cenario_atual = sala
                    nome_cenario_atual = cenario_atual
                elif sala == "saguao":
                    cenario_atual = sala
                    nome_cenario_atual = cenario_atual
                elif sala == "sala dos professores":
                    cenario_atual = "sala dos professores"
                    print("-"*len(cenarios[cenario_atual]["titulo"]))
                    print(cenarios[cenario_atual]["titulo"])
                    print("-"*len(cenarios[cenario_atual]["titulo"]))
                    print(cenarios[cenario_atual]["descricao"])
                    game_over = True
                elif sala == "ir embora":
                    cenario_atual = "ir embora"
                    print("-"*len(cenarios[cenario_atual]["titulo"]))
                    print(cenarios[cenario_atual]["titulo"])
                    print("-"*len(cenarios[cenario_atual]["titulo"]))
                    print(cenarios[cenario_atual]["descricao"])
                    game_over = True
                else:
                    print("sala inválida")
                    escolha = input("tente novamente: ")
                    
            # IF Abrir
            if escolha == "abrir":
                cenario_atual = "abrir"
                print("-"*len(cenarios[cenario_atual]["titulo"]))
                print(cenarios[cenario_atual]["titulo"])
                print("-"*len(cenarios[cenario_atual]["titulo"]))
                print(cenarios[cenario_atual]["descricao"])
                game_over = True
                
            #IF ir embora
            if escolha == "ir embora":
                cenario_atual = "ir embora"
                print("-"*len(cenarios[cenario_atual]["titulo"]))
                print(cenarios[cenario_atual]["titulo"])
                print("-"*len(cenarios[cenario_atual]["titulo"]))
                print(cenarios[cenario_atual]["descricao"])
                game_over = True
                
                
    if game_over == True:
        print("você concluiu o jogo!")
        print ("FIM")
# Programa principal.
if __name__ == "__main__":
    main()
