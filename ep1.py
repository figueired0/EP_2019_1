# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Ana Clara Carneiro de Freitas, anaccf5@insper.edu.br
# - aluno B: Igor Figueiredo, sicranoa1@insper.edu.br

def carregar_cenarios():
    cenarios= {
            "fase1_recepcao": {
                    "titulo": "Saguao do Insper",
                    "descricao": "Voce está no saguao de entrada do insper",
                    "opcoes": {
                            "recepção": "bem vindo a recepção do insper em que posso ajudá-lo?",
                            "biblioteca": "a biblioteca está lotada, volte mais tarde",
                            "banheiro": "O banheiro está sendo limpado, volte mais tarde",
                            "sala dos professores": "A sala está em reuniao, volte mais tarde"
                            }
                    },
            "banheiro": {
                    "titulo": "banheiro",
                    "descricao": "voce chegou no banheiro, será que raul está aqui? Dê uma olhada",
                    "opcoes":{
                            "saguão": "voltar ao saguão",
                            "porta":"abrir a porta"
                            }
                    },
            "sala dos professores": {
                    "titulo": "Sala dos professores",
                    "descricao": "voce entrou na sala dos professores e se depara com o professor humberto",
                    "opcoes": {
                            "pergunta":"perguntar sobre raul",
                            "saguão":"voltar ao saguão"
                            }
                    },
            "biblioteca": {
                    "titulo": "biblioteca",
                    "descricao": "voce cehgou a biblioteca do insper, o que deseja fazer?",
                    "opcoes": {
                            "livros":"procurar livros", 
                            "saguão":"voltar ao sagão",
                            "sala":"ir para outra sala"
                            }
                    },
            "recepção":{
                    "titulo":"recepção",
                    "descricao":"bem vindo a recepção do insper em que posso ajuda-lo?",
                    "opcoes":{
                            "
                            }
                    
                    }
            }   
    nome_cenario_atual = "fase1_recepcao"
    return cenarios, nome_cenario_atual


def main():
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
        for k in (cenario_atual["opcoes"]).keys():
                print (k)

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

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
