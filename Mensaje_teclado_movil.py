def movile_keyboard(message):

    #creo el diccionario
    keyboard = {
        ' ':'0',
        'a':'2',
        'b':'22',
        'c':'222',
        'd':'3',
        'e':'33',
        'f':'333',
        'g':'4',
        'h':'44',
        'i':'444',
        'j':'5',
        'k':'55',
        'l':'555',
        'm':'6',
        'n':'66',
        'o':'666',
        'p':'7',
        'q':'77',
        'r':'777',
        's':'7777',
        't':'8',
        'u':'88',
        'v':'888',
        'w':'9',
        'x':'99',
        'y':'999',
        'z':'9999',
    }

    #incializo las variables vacias
    response = ''
    last_number = ''

    #recorro el mensaje 
    for letter in message:
        #obtengo de cada letra su combinación numérica correspondiente
        key = keyboard.get(letter,'')

        #si la combinación numérica es igual a la anterior le pongo un espacio
        #sino la agrego al mensaje sin espacio
        if last_number==key:
            response += ' ' + key
        else:
            response += key 

        last_number = key
    
    #pinto el mensaje
    print(response)

if __name__ == '__main__':
    print("Ingrese el mensaje: ")
    message = input()
    movile_keyboard(message)