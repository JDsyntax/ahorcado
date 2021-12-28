from os import system as sys
import random

# Funcion de escoger la palabra desde la base de datos
def choose_word(data):
    global word
    global word_len
    word = random.choice(data)
    word = ''.join(x for x in word if x != '\n')
    for i in word:
        if i == 'á':
            word = word.replace('á', 'a')
        elif i == 'é':
            word = word.replace('é', 'e')
        elif i == 'í':
            word = word.replace('í', 'i')
        elif i == 'ó':
            word = word.replace('ó', 'o')
        elif i == 'ú':
            word = word.replace('ú', 'u')
    word_len = len(word)
    return word
# Funcion de dibujas la linea de opciones
def draw_line(letters_num):
    global hidden_word
    hw = []
    for i in range(word_len):
        hw.append('_ ')

    hidden_word = ''.join(hw)

# La funcion de remplazar letras (tal vez la funcion mas importantes del juego)
def replace_letter(letter):
    hw = []
    global hidden_word
    for i in hidden_word:
       hw =  hidden_word.split()
    word_letters = dict(enumerate(word))
    letter_positions = [key for key, value in word_letters.items() if value == letter]
    for i in letter_positions:
        hw[i] = letter
    hidden_word = ' '.join(hw)

def draw_tittle():
    tittle = ''
    with open('./archivos/tittle_ahorcado.txt', 'r', encoding='utf-8') as f:
        tittle = f.read()

    print(tittle)

def draw_hangman(num):
    hangman_state = [
        open('./archivos/ahorcado.txt', 'r', encoding='utf-8').read(),
        open('./archivos/ahorcado1.txt','r', encoding='utf-8').read(),
        open('./archivos/ahorcado2.txt','r', encoding='utf-8').read(),
        open('./archivos/ahorcado3.txt','r', encoding='utf-8').read(),
        open('./archivos/ahorcado4.txt','r', encoding='utf-8').read(),
        open('./archivos/ahorcado5.txt','r', encoding='utf-8').read(),
        open('./archivos/ahorcado6.txt','r', encoding='utf-8').read(),]
    print(hangman_state[num])

def run():
    sys('clear')
    with open('./archivos/data.txt', 'r', encoding='utf-8') as f:
        data = [line for line in f]
    choose_word(data)

    draw_line(word_len)
    finished = False
    win = False
    losse = False
    count = 0
    #Bucle principal del juego
    while finished == False:

        draw_tittle()
        draw_hangman(count)
        print('')
        print(hidden_word)
        letter = input('Escribe una letra: ').lower()
        replace_letter(letter)
        if letter not in hidden_word:
            count += 1
        
        sys('clear')
        
        if '_' not in hidden_word and count <= 5:
            win = True
            losse = False
            draw_tittle()
            draw_hangman(count)
            print('')
            print(hidden_word)
            with open('./archivos/win.txt', 'r', encoding='utf-8') as f:
                win_message = f.read()
            print('')
            print(win_message)
        if '_' in hidden_word and count > 5:
            win = False
            losse = True
            draw_tittle()
            draw_hangman(6)
            with open('./archivos/losse.txt', 'r', encoding='utf-8') as f:
                losse_message = f.read()
            print(losse_message)
            print('')
            print('La palabra era: ' + word)
        if win or losse:
            finished = True
    
    anws = input('Quieres volver a jugar (S)i o (N)o: ')
    # Bucle de reinicio del juego
    while anws.lower() != 's' and anws.lower() != 'n':
        print('Inserta una respuesta valida')
        anws = input('Quieres volver a jugar (S)i o (N)o: ')

    if anws.lower() == 's':
        sys('python juego_del_ahorcado.py')
    else:
        with open('./archivos/final_message.txt', 'r', encoding='utf-8') as f:
            final_message = f.read()
        print('')
        print(final_message)

if __name__ == '__main__':
    run(  )