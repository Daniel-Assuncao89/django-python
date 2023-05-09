"""
Primeira solucao foi usar o metodo reverse() e comparar a palavra normal com a inversa, primeira dificuldade foi que o metodo reverse so se usa em estrutura list, então fui atras de como transformar em lista, depois a comparação não funcionava pq a variavel q deveria armazenar a palavra inversa retornava None e foi ai que descobri que o metodo reverse ele não retorna valores, ele so altera o original. Depois disso pensei em soluções mais verbosas, de armazenar o char de cada indice para fazer a comparação, um iniciando no indice 0 e o outro no final da palavra e ai comparando se as extremidades eram iguais. Mas achei q deveria ter uma solucao mais simples, entao comecei a ver minhas anotações sobre manipulação de array e foi ai que consegui resolver o problema. Decidi deixar alguns passos q fiz no codigo pra vcs terem essa visualização do caminho percorrido.
"""
palavra = input()
# print(palavra[::-1])
# print(palavra[0:] == palavra[::-1])

def palindromo(palavra):
    if ( palavra[0:] == palavra[::-1]):
         print(f"{palavra} é um Palíndromo")
    else:
         print(f"A palavra : {palavra}")

palindromo(palavra)

"""
def converterStrParaList(palavra: str) -> list:
    converterPalavra = []
    converterPalavra[0:] = palavra
    return converterPalavra


def reverterLista(lista):

     listaReversa = []
     listaReversa = lista.reverse()
     print(listaReversa)
     return listaReversa

listaPalavra = converterStrParaList(palavra)
listaReversa = listaPalavra.reverse()
print(listaReversa) # retorna none pq reverse() não retorna valores para armazenamento
print(str(listaPalavra)) # tentativa de converter a lista de volta para string.
palindromo(listaPalavra)

reverterLista(listaPalavra)
"""