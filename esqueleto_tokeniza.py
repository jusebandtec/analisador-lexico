
# Constantes
from http.client import LENGTH_REQUIRED
from operator import le
import re

from numpy import array_str, indices, var


TESTE   = False

# caracteres usados em operadores
OPERADORES = "%*/+-!^="

# caracteres usados em números inteiros
DIGITOS = "0123456789"

# ponto decimal
PONTO = "."

# todos os caracteres usados em um números float
FLOATS = DIGITOS + PONTO

# caracteres usados em nomes de variáveis
LETRAS  = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# abre e fecha parenteses
ABRE_FECHA_PARENTESES = "()"

# categorias
OPERADOR   = 1 # para operadores aritméticos e atribuição
NUMERO     = 2 # para números: todos são considerados float
VARIAVEL   = 3 # para variáveis
PARENTESES = 4 # para '(' e ')

# Whitespace characters: space, newline, horizontal tab,
# vertical tab, form feed, carriage return
BRANCOS    = [' ', '\n', '\t', '\v', '\f', '\r']

# caractere que indica comentário
COMENTARIO = "#"


#------------------------------------------------------------
def tokeniza(exp):
    """(str) -> list

    Recebe uma string exp representando uma expressão e cria 
    e retorna uma lista com os itens léxicos que formam a
    expressão.

    Cada item léxico (= token) é da forma
       
        [item, tipo]

    O componente item de um token é 

        - um float: no caso do item ser um número; ou 
        - um string no caso do item ser um operador ou 
             uma variável ou um abre/fecha parenteses.

    O componente tipo de um token indica a sua categoria
    (ver definição de constantes acima). 

        - OPERADOR;
        - NUMERO; 
        - VARIAVEL; ou 
        - PARENTESES

    A funçao ignora tuo que esta na exp apos o caractere
    COMENTARIO (= "#").
    """
    # escreva o seu código abaixo

    def split_str(string):
        return [ch for ch in string]

    def validar_variavel(array, indice):
        variavel = ''   
        if array[0] in LETRAS:
            variavel = recorte_variavel(array)
            indice += len(variavel)-1

        return [variavel.strip(), indice]

    def recorte_variavel(array) -> str:
        variavel = ''
        for i in array:
            if not i in BRANCOS and not i in OPERADORES and not i in ABRE_FECHA_PARENTESES:
                variavel += i
            else:
                break

        return variavel

    def validar_ponto_flutuante(array, indice):
        variavel = ''
        if array[0] in FLOATS:
            variavel = recortar_ponto_flutuante(array)
            indice += len(variavel)-1

        return [variavel.strip(), indice]
        
    def recortar_ponto_flutuante(array) -> float:
        ponto_flutuante = ''
        for i in array:
            if not i in BRANCOS and not i in OPERADORES and not i in ABRE_FECHA_PARENTESES:
                ponto_flutuante += i    
            else:
                break
        
        return ponto_flutuante

    array_lexico = []
    array_string = split_str(exp)
    i = 0

    for _ in range(len(array_string)):

        if i >= len(array_string):
            break

        if not array_string[i] in BRANCOS:
            
            if array_string[i] == COMENTARIO:
                return array_lexico
            
            if array_string[i] in OPERADORES:
                array_lexico.append([array_string[i], OPERADOR])

            if array_string[i] in ABRE_FECHA_PARENTESES:
                array_lexico.append([array_string[i], PARENTESES])

            if array_string[i] in FLOATS:
                ponto_flutuante, i = validar_ponto_flutuante(array_string[i:], i)
                array_lexico.append([float(ponto_flutuante), NUMERO])

            if array_string[i] in LETRAS:
                variavel, i = validar_variavel(array_string[i:], i)
                array_lexico.append([variavel, VARIAVEL])
                
        i += 1

    return array_lexico
    

