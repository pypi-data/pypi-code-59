import re


def par(number: int) -> bool:
    """Função que valida se número é par"""
    try:
        return number % 2 == 0
    except (TypeError) as ex:
        print(str(ex))
    return False

# funcao para retirar caracteres nao numericos
def retira_formatacao(num_cpf):
    num_cpf_limpo= re.sub('[^0-9]', '', num_cpf)
    return num_cpf_limpo


def valida_cpf(num_cpf):
    num_cpf_limpo = retira_formatacao(num_cpf)
    num_cpf_limpo_validador = num_cpf_limpo[0:9]  # eliminando os digitos
    multiplicador = 10                            # multiplicador entra valendo 10
    retorno = 0                                   # retorno soma o resultado da multiplicação feita entre o numero do cpf e o multiplicador
    for numero in num_cpf_limpo_validador:
        resultado = int(numero) * int(multiplicador)
        retorno = retorno + resultado
        multiplicador -= 1
    retorno2 = (retorno * 10) % 11 % 10           # resto do algoritimo que deve ser igual ao primeiro digito do cpf para ser valido

    num_cpf_limpo_validador = num_cpf_limpo[0:10]
    multiplicador = 11
    retorno = 0
    for numero in num_cpf_limpo_validador:
        resultado = int(numero) * int(multiplicador)
        retorno = retorno + resultado
        multiplicador -= 1
    retorno3 = (retorno * 10) % 11 % 10     # resto do algoritimo que deve ser igual ao segundo digito do cpf para ser valido

    # verificando se o cpf é diferente de 11 numeros inteiros
    if len(num_cpf_limpo) != 11:
        return False

    # verificando se ambos os retornos (restos) da validação são iguais aos respectivos 2 digitos do cpf
    if int(num_cpf_limpo[9]) != int(retorno2) or int(num_cpf_limpo[10]) != int(retorno3):
        return False

    # verificando numero que passam como cpfs válidos, mas são inválidos
    lista_cpfs_invalidos = ['00000000000', '11111111111', '22222222222', '33333333333', '44444444444', '55555555555', '66666666666', '77777777777', '88888888888', '99999999999' ]
    if num_cpf_limpo in lista_cpfs_invalidos:
        return False

    return True


def conversao_romana(numero):

    inteiros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    romanos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    #exemplo:   numero = 20
    try:
        numero = int(numero)
        i = 0
        resultado = ""
        while numero > 0: #20 maior que 0              |   10 maior que 0
            if numero >= inteiros[i]: #20 >= 10        |   10 >= 10
                resultado += romanos[i]
                numero -= inteiros[i] #20 - 10         | 10 - 10
            else:
                i += 1
                
    except Exception as ex:
        print(f'Function expects an integer: {ex}')
        resultado = False

    return resultado