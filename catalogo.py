import os
import json
from datetime import date

ARQUIVO_DADOS = "meus_filmes.json"
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def carregar_dados():
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8")as arquivo:
            return json.load(arquivo)
    except:
        print("arquivo não existe!!")
        return []
    


def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8")as arquivo:
        json.dump(dados,arquivo,indent=4, ensure_ascii=False)

def obter_ano_valido():
    while True:
        try:
            ano = int(input("ano de lançamento: "))

            if ano < 1888 or ano > date.today().year:
                print("por favor. digite um ano realista.")
                continue

            return ano
        except ValueError:
            print("ERRO. digite apenas números inteiros para o ano.")



def obter_nota_valida():
    while True:
        try:
            nota = float(input("nota(0.0 a 5.0): "))
            if nota < 0.0 or nota > 5.0:
                print("a nota deve está entre 0 a 5. ")
                continue

        except ValueError:
            print("ERRO. use ponto para números decimais")



def adicionar_filmes(catalogo):
    limpar_tela()
    print("--- REGISTRAR NOVO FILME ---")
    titulo = input("Titulo: ").strip()

    for filme in catalogo:
        if filme("Titulo").lower() == titulo.lower():
            print(f"\n Atenção: o filme {filme["Titulo"]} já está cadastrado no seu catalogo!")
            return
        
    genero = input("genero (ex: ação, comédia, drama): ").strip()
    ano = obter_ano_valido()
    nota = obter_nota_valida()
    critica = input("breve critica:").strip()

    filme = {
        "Titulo" : titulo,
        "genero" : genero,
        "ano" : ano,
        "nota" : nota,
        "critica" : critica
    }
    catalogo.append(filme)
    salvar_dados(catalogo)
    print(f" {titulo} adicionado com sucesso no seu catalogo")

if __name__ == "__main__":
   lista_filmes = carregar_dados()
   adicionar_filmes(lista_filmes)