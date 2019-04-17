# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Ana Clara Carneiro de Freitas, anaccf5@insper.edu.br
# - aluno B: Igor Figueiredo, igorf1@insper.edu.br

def carregar_cenarios():
    cenarios= {
            "saguão1": {
                    "titulo": "Saguão do Insper",
                    "descricao": "Voce está no saguão de entrada do insper",
                    "opcoes": {
                            "recepção1": "Ir á recepção",
                            "biblioteca1": "Ir á biblioteca",
                            "banheiro1": "Ir ao banheiro",
                            "sala dos professores1": "Ir á sala dos professores"
                            }
                    },
                    
            "biblioteca1": {
                    "titulo": "Biblioteca",
                    "descricao": "A biblioteca está lotada, volte mais tarde",
                    "opcoes": {
                            "saguão1": "voltar ao saguão"
                            }
                    },
                    
            "banheiro1": {
                    "titulo": "Banheiro",
                    "descricao": "O banheiro está sendo limpado, volte mais tarde",
                    "opcoes": {
                            "saguão1": "voltar ao saguão"
                            }
                    },
                    
            "sala dos professores1": {
                    "titulo": "Sala dos professores",
                    "descricao": "A sala está em reuniao, volte mais tarde",
                    "opcoes": {
                            "saguão1": "voltar ao saguão"
                            }
                    },
                    
            "recepção1":{
                    "titulo":"recepção",
                    "descricao":"bem vindo a recepção do insper em que posso ajuda-lo?",
                    "opcoes":{
                            "perguntar":"Pergunte onde raul está?",
                            "saguão1":"voltar ao saguão"
                            }
                    
                    },
                    
            "perguntar": {
                    "titulo": "A grande pista",
                    "descricao": "após perguntar sobre Raul, a recepcionista diz que o"
                                 "viu indo para o banheiro a pouco tempo",
                    "opcoes": {
                            "saguão2": "voltar ao saguão"
                            }
                    },
                    
            "saguão2": {
                    "titulo": "Saguão do Insper",
                    "descricao": "Voce está no saguão de entrada do insper",
                    "opcoes": {
                            "recepção1": "Ir á recepção",
                            "biblioteca1": "Ir á biblioteca",
                            "banheiro2": "Ir ao banheiro",
                            "sala dos professores1": "Ir á sala dos professores"
                            }
                    },
                    
            "Banheiro2": {
                    "titulo": "banheiro",
                    "descricao": "voce chegou no banheiro, será que raul está aqui?"
                                 "Dê uma olhada!"
                                 "Você escuta gritos, será que deve investigar?",
                    "opcoes":{
                            "saguão2": "voltar ao saguão",
                            "porta1":"abrir a porta"
                            }
                    },
                    
            "porta1": {
                    "titulo": "Porta trancada",
                    "descrição": "Apos tentar abrir a porta do banheiro"
                                 "voce percebe que ela esta trancada"
                                 "voce precisa de uma chave",
                    "opcoes": {
                            "saguão3": "voltar ao saguão"
                            }
                    },                            
                    
            "saguão3": {
                    "titulo": "Saguão do Insper",
                    "descricao": "Voce está no saguão de entrada do insper",
                    "opcoes": {
                            "recepção1": "Ir á recepção",
                            "biblioteca1": "Ir á biblioteca",
                            "banheiro2": "Ir ao banheiro",
                            "sala dos professores2": "Ir á sala dos professores"
                            }
                    },
                    
            "Sala dos professores2": {
                    "titulo": "Sala dos professores",
                    "descricao": "voce entrou na sala dos professores e se depara com"
                                 "o professor Humberto",
                    "opcoes": {
                            "questionar": "perguntar sobre Raul",
                            "saguão3": "voltar ao saguão"
                            }
                    },
                    
            "quenstionar": {
                    "titulo": "O grande desafio",
                    "decricao": " ",
                    "opcoes": {
                            "charada": " ",
                            "saguão3": "voltar ao saguão"
                            }
                    },
                    
            "charada": {
                    "titulo": "O grande desafio",
                    "descricão": " ",
                    "opcoes": {
                            "saguão4": "voltar ao saguão"
                            }
                    },
            
            "saguão4": {
                    "titulo": "Saguão do Insper",
                    "descricao": "Voce está no saguão de entrada do insper",
                    "opcoes": {
                            "recepção1": "Ir á recepção",
                            "biblioteca2": "Ir á biblioteca",
                            "banheiro2": "Ir ao banheiro",
                            "sala dos professores2": "Ir á sala dos professores"
                            }
                    },

            "Biblioteca2": {
                    "titulo": "biblioteca",
                    "descricao": "voce cehgou a biblioteca do insper, o que deseja fazer?",
                    "opcoes": {
                            "livros":"procurar livros", 
                            "saguão4":"voltar ao sagão",
                            "sala":"ir para outra sala"
                            }
                    },
               
            "livros": {
                    "titulo": " ",
                    "descricao": " ",
                    "opcoes": {
                            "livro 1": "Investigar livro 1",
                            "livro 2": "Investigar livro 2",
                            "livro 3": "Investigar livro 3"
                            }
                    },
                    
            "livro 1": {
                    "titulo": " ",
                    "descricao": " ",
                    "opcoes": {
                            "livro 2": "Investigar livro 2",
                            "livro 3": "Investigar livro 3"
                            }
                    },
                    
            "livro 2": {
                    "titulo": " ",
                    "descricao": " ",
                    "opcoes": {
                            "livro 1": "Investigar livro 1",
                            "livro 3": "Investigar livro 3"
                            }
                    },
                    
            "livro 3": {
                    "titulo": " ",
                    "descricao": " ",
                    "opcoes": {
                            "saguão5": "voltar ao saguão"
                            }
                    },
            
            "saguão5": {
                    "titulo": "Saguão do Insper",
                    "descricao": "Voce está no saguão de entrada do insper",
                    "opcoes": {
                            "recepção1": "Ir á recepção",
                            "biblioteca2": "Ir á biblioteca",
                            "banheiro3": "Ir ao banheiro",
                            "sala dos professores2": "Ir á sala dos professores"
                            }
                    },
                    
            "banheiro3": {
                    "titulo": " ",
                    "descricao": " ",
                    "opcoes": {
                            "porta2": "Abrir a porta 2"
                            }
                    },
            
            "porta2": {
                    "titulo": "Porta do banheiro",
                    "descricao": "Voce chegou ao baheiro e agora possui a chave para abrir a porta",
                    "opcoes": {
                            "abrir":"abrir a porta",
                            "saguão6": "voltar ao saguão"
                            }
                    },
            
            "abrir": {
                    "titulo": "O grande final",
                    "descricao": " "
                    },
            
            "saguão6": {
                    "titulo": "Saguão do Insper",
                    "descricao": "Voce está no saguão de entrada do insper",
                    "opcoes": {
                            "ir embora"
                            }
                    },
            
            "ir embora": {
                    "titulo": " ",
                    "descricao": " "
                    }
            }   
    nome_cenario_atual = "saguão"
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
        cenario_atual = cenarios[nome_cenario_atual]
        print("-"*len(cenario_atual["titulo"]))
        print(cenario_atual["titulo"])
        print("-"*len(cenario_atual["titulo"]))
        print(cenario_atual["descricao"])
        print()
        print("essas sao as opçoes que voce possui:")
        print()
        for k,v in (cenario_atual["opcoes"]).items():
                print (k,":",v)

        opcoes = cenario_atual['opcoes']
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
