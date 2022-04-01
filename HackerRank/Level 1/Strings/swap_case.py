def swap_case(s):

    text = list(s)
  
    result=[]   # Lista vacia
    for letter in text:

        # Comprobar si es minuscula
        flag = letter.islower()
        # Si esta en minuscula cambiar a mayuscula
        if flag == True:
            l = letter.capitalize()
            result.append(l)
        else:
            l = letter.casefold()
            result.append(l)
        
    #Unir
    result = ''.join(result)

    return result






if __name__ == '__main__':

    print("\nIntroduce la frase: ")
    s = input()

    mod = swap_case(s)

    print(mod)