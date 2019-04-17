# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Ana Clara Carneiro de Freitas, anaccf5@insper.edu.br
# - aluno B: Igor Figueiredo, igorf1@insper.edu.br

def carregar_cenarios():
    cenarios= {
            "saguão 1": {
                    "titulo": "Saguão do Insper",
                    "descricao": "Voce está no saguão de entrada do insper",
                    "opcoes": {
                            "recepção 1": "Ir á recepção",
                            "biblioteca 1": "Ir á biblioteca",
                            "banheiro 1": "Ir ao banheiro",
                            "sala dos professores 1": "Ir á sala dos professores"
                            }
                    },
                    
            "biblioteca 1": {
                    "titulo": "Biblioteca",
                    "descricao": "A biblioteca está lotada, volte mais tarde",
                    "opcoes": {
                            "saguão 1": "voltar ao saguão"
                            }
                    },
                    
            "banheiro 1": {
                    "titulo": "Banheiro",
                    "descricao": "O banheiro está sendo limpado, volte mais tarde",
                    "opcoes": {
                            "saguão 1": "voltar ao saguão"
                            }
                    },
                    
            "sala dos professores 1": {
                    "titulo": "Sala dos professores",
                    "descricao": "A sala está em reuniao, volte mais tarde",
                    "opcoes": {
                            "saguão 1": "voltar ao saguão"
                            }
                    },
                    
            "recepção 1":{
                    "titulo":"recepção",
                    "descricao":"bem vindo a recepção do insper em que posso ajuda-lo?",
                    "opcoes":{
                            "perguntar":"Pergunte onde raul está?",
                            "saguão 1":"voltar ao saguão"
                            }
                    
                    },
                    
            "perguntar": {
                    "titulo": "A grande pista",
                    "descricao": "após perguntar sobre Raul, a recepcionista diz que o "
                                 "viu indo para o banheiro a pouco tempo",
                    "opcoes": {
                            "saguão 2": "voltar ao saguão"
                            }
                    },
                    
            "saguão 2": {
                    "titulo": "Saguão do Insper",
                    "descricao": "Voce está no saguão de entrada do insper",
                    "opcoes": {
                            "recepção 2": "Ir á recepção",
                            "biblioteca 2": "Ir á biblioteca",
                            "banheiro 2": "Ir ao banheiro",
                            "sala dos professores 2": "Ir á sala dos professores"
                            }
                    },
             "biblioteca 2": {
                    "titulo": "Biblioteca",
                    "descricao": "A biblioteca está lotada, volte mais tarde",
                    "opcoes": {
                            "saguão 2": "voltar ao saguão"
                            }
                    },
                    
            "sala dos professores 2": {
                    "titulo": "Sala dos professores",
                    "descricao": "A sala está em reuniao, volte mais tarde",
                    "opcoes": {
                            "saguão 2": "voltar ao saguão"
                            }
                    },
                    
            "recepção 2":{
                    "titulo":"recepção",
                    "descricao":"A recepcionista foi almoçar, volte mais tarde",
                    "opcoes":{
                            "saguão 2":"voltar ao saguão"
                            }
                    },
                    
            "banheiro 2": {
                    "titulo": "banheiro",
                    "descricao": "voce chegou no banheiro, será que raul está aqui? "
                                 "Dê uma olhada! "
                                 "Você escuta gritos, será que deve investigar?",
                    "opcoes":{
                            "saguão 2": "voltar ao saguão",
                            "porta 1":"abrir a porta"
                            }
                    },
                    
            "porta 1": {
                    "titulo": "Porta trancada",
                    "descricao": "Apos tentar abrir a porta do banheiro "
                                 "voce percebe que ela esta trancada. "
                                 "Voce precisa encontrar uma chave",
                    "opcoes": {
                            "saguão 3": "voltar ao saguão"
                            }
                    },                            
                    
            "saguão 3": {
                    "titulo": "Saguão do Insper",
                    "descricao": "Voce está no saguão de entrada do insper",
                    "opcoes": {
                            "biblioteca 3": "Ir á biblioteca",
                            "sala dos professores 3": "Ir á sala dos professores"
                            }
                    },
                    
             "biblioteca 3": {
                    "titulo": "Biblioteca",
                    "descricao": "A biblioteca está lotada, volte mais tarde",
                    "opcoes": {
                            "saguão 3": "voltar ao saguão"
                            }
                    },
                    
            "sala dos professores 3": {
                    "titulo": "Sala dos professores",
                    "descricao": "voce entrou na sala dos professores e se depara com "
                                 "o professor Humberto",
                    "opcoes": {
                            "questionar": "perguntar sobre Raul",
                            "saguão 3": "voltar ao saguão"
                            }
                    },
                    
            "questionar": {
                    "titulo": "O grande desafio",
                    "descricao": "Humberto acordou engraçado hoje e decidiu que só te contará"
                                 " onde Raul está se você advinhar uma charada",
                    "opcoes": {
                            "charada": "perguntar sobre a charada",
                            "saguão 3": "voltar ao saguão"
                            }
                    },
                    
            "charada": {
                    "titulo": "O grande desafio",
                    "descricao": "Ai vai a charada: Qual é o animal que caminha sobre quatro pernas de "
                                 "manhã, duas pernas durante a tarde e três pernas a noite?",
                    "opcoes": {
                            "saguão 4": "voltar ao saguão"
                            }
                    },
            
            "saguão 4": {
                    "titulo": "Saguão do Insper",
                    "descricao": "Voce está no saguão de entrada do insper",
                    "opcoes": {
                            "biblioteca 4": "Ir á biblioteca",
                            "banheiro 4": "Ir ao banheiro",
                            }
                    },

            "biblioteca 4": {
                    "titulo": "biblioteca",
                    "descricao": "voce chegou á biblioteca do insper, o que deseja fazer?",
                    "opcoes": {
                            "livros":"procurar livros", 
                            "saguão 4":"voltar ao sagão"
                            }
                    },
               
            "livros": {
                    "titulo": "A procura da chave",
                    "descricao": "Dentre todos as descrições que havia no bilhete de "
                                 "Humberto, você encontrou três livros onde a chave "
                                 "pode estar",
                    "opcoes": {
                            "livro 1": "Investigar livro 1",
                            "livro 2": "Investigar livro 2",
                            "livro 3": "Investigar livro 3"
                            }
                    },
                    
            "livro 1": {
                    "titulo": "Livro 1: Mãos a obra, construindo um banheiro",
                    "descricao": "Ao pegar o livro na mão, você decide folea-lo "
                                 "e não encontra nada. Sendo assim, você decide "
                                 "olhar o próximo",
                    "opcoes": {
                            "livro 2": "Investigar livro 2",
                            "livro 3": "Investigar livro 3"
                            }
                    },
                    
            "livro 2": {
                    "titulo": "Livro 2: O enigma do banheiro ",
                    "descricao": "Ao pegar o livro na mão, você decide folea-lo "
                                 "e não encontra nada. Sendo assim, você decide "
                                 "olhar o próximo",
                    "opcoes": {
                            "livro 1": "Investigar livro 1",
                            "livro 3": "Investigar livro 3"
                            }
                    },
                    
            "livro 3": {
                    "titulo": "Livro 3: Pythopolis, em busca da chave perdida",
                    "descricao": "Ao pegar o livro na mão, você decide folea-lo "
                                 "e encontra algo misterioso no meio. "
                                 "(...) "
                                 "Após investigar profundamente, você perebe que "
                                 "esta é a chave desejada para abrir o banheiro "
                                 "e salvar Raul. "
                                 "Será que você conseguirá adiar o EP1?",
                    "opcoes": {
                            "saguão 5": "voltar ao saguão",
                            "sala":"ir para outra sala"
                            }
                    },
            
            "sala": {
                    "titulo": "teletransporte",
                    "descricao": "você por ir diretamente para outro sala. Basta apenas "
                                 "digitar o nome da sala desejada "
                                 "DICA: digite apenas o nome da sala (Sem numeros)",
                                 },
                    
            "banheiro 4": {
                    "titulo": "Banheiro",
                    "descricao": "Você ainda não possui a chave, volte mais tarde",
                    "opcoes": {
                            "saguão 4": "voltar ao saguão"
                            }
                    },
            
            "saguão 5": {
                    "titulo": "Saguão do Insper",
                    "descricao": "Voce está no saguão de entrada do insper",
                    "opcoes": {
                            "banheiro": "Ir ao banheiro",
                            }
                    },
                    
            "banheiro": {
                    "titulo": "O grande fiinal",
                    "descricao": "Você chegou ao banheiro e agora possui a chave para "
                                 "abrir a tão estimada porta. "
                                 "O que você irá fazer?",
                    "opcoes": {
                            "porta 2": "Abrir a porta"
                            }
                    },
            
            "porta 2": {
                    "titulo": "Porta do banheiro",
                    "descricao": "Você coloca a chave na maceneta e...",
                    "opcoes": {
                            "abrir":"abrir a porta",
                            "saguão 6": " tirar a chave e voltar ao saguão"
                            }
                    },
            
            "abrir": {
                    "titulo": "Adiantamento do EP",
                    "descricao": "Vôce cola a chave na maceneta e, ao abri-la "
                                 "(...)  "
                                 "Voce se depara com Raul, desolado e perdido no canto "
                                 "do banheiro. "
                                 "Porém, no momento em que há troca de olhares, a felicidade "
                                 "é estampada em seu rosto e IMEDIATAMENTE, Raul pula em você "
                                 "e te agradece ferverosamente. "
                                 "Você aproveita a ocasiao para perguntar sobre o EP1 e se seria "
                                 "possivel o adiantamento desse. "
                                 "Devido a extrema gratidão de Raul, ele te concede mais 1h a mais "
                                 "para entrega."
                    },
            
            "saguão 6": {
                    "titulo": "Saguão do Insper",
                    "descricao": "Voce está no saguão de entrada do insper",
                    "opcoes": {
                            "ir embora": "Deixar o Insper"
                            }
                    },
            
            "ir embora": {
                    "titulo": " ",
                    "descricao": "Você não gosta de Raul e, portanto, decide mante-lo trancado "
                                 "no banheiro para sempre. "
                                 "Raul morre de fome e solidão e você não precisa entregar o EP",
                    }
            }   
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

    game_over = False
    while not game_over:
        nome_cenario_atual = cenarios[nome_cenario_atual]
        print("-"*len(nome_cenario_atual["titulo"]))
        print(nome_cenario_atual["titulo"])
        print("-"*len(nome_cenario_atual["titulo"]))
        print(nome_cenario_atual["descricao"])
        print()
        print("essas são as opções que você possui:")
        print()
        
        for k,v in (nome_cenario_atual["opcoes"]).items():
                print (k,":",v)

        opcoes = nome_cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            escolha = ""
            escolha = input("para onde deseja ir?")
            
            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("essa opção não existe")
                game_over = True
                
# Programa principal.
if __name__ == "__main__":
    main()
