def verifica_senha(password):
    count_caracter = len(password)
    count_num = 0
    count_letter = 0
    count_pontuacao = 0
    num_condicionais = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    pontuacao_condicionais = ['!', '?', ',', '.', ':', ';']
    for i in password:
        if i in num_condicionais:
            count_num += 1
        if i.isalpha():
            count_letter += 1
        if i in pontuacao_condicionais:
            count_pontuacao += 1
            
    if count_caracter <= 5:
        return 'Senha fraca'
    elif count_num > 0 and count_letter > 0 and count_pontuacao > 0:
        return 'Senha Muito Forte'       
    elif count_num > 0 and count_letter > 0:
        return 'Senha forte'         
            
    #return count_caracter, count_num, count_letter, count_pontuacao

password = input('Digite uma senha: ')

resultado = verifica_senha(password)
print(resultado)
            