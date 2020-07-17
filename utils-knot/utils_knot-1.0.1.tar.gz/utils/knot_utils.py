def convercao_romana(numero):

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