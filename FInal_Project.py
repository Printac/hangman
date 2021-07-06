def choose_word(file_path, index): 
    """ Choosing a word from a txt file
        :param file_path: file path value
        :index: the index of which word does the user want from the file
        :type file_path: str
        :type index: str
        :return: the word that the user want to be the secret_word
        :rtype: str"""
    input_from_file = open(file_path , 'r')
    place_in_the_file = input_from_file.read()
    input_list = place_in_the_file.split(" ")
    temp_list = []  
    count = 0
    for item in input_list:
        if item not in temp_list:
            count += 1
            temp_list.append(item)
    input_from_file.close()
    return input_list[(index-1) % len(input_list)]

def check_win(secret_word, old_letters_guessed):
    """ checks if secret_word in old words - if yes , you win 
        :param secret_word: the secret_word
        :param old_letters_guessed: list of all geussed letters
        :type secret_word: str
        :type old_letters_guessed: list
        :return: True if u win and false if not
        :rtype: bool"""
    ans = True
    for i in range(len(secret_word)):
        if secret_word[i] not in old_letters_guessed:
            ans = False
    return ans
    
def show_hidden_word(secret_word, old_letters_guessed):
    """ hides the ungeussed letters and reveal the others
        :param secret_word: the secret_word
        :param old_letters_guessed: list of all geussed letters
        :type secret_word: str
        :type old_letters_guessed: list
        :return: return the secret word with revealed letters 
        :rtype: str"""
    ans = list(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] not in old_letters_guessed:
            ans[i] = '_'
    final = ' '.join(ans)
    print(final)
    
def check_valid_input(letter_guessed, old_letters_guessed):
    """ checks if the letter that the user typed is legal(eng letter ,1 char , in the list already)
        :param letter_guessed: the geussed letter
        :param old_letters_guessed: list of all geussed letters
        :type letter_guessed: str
        :type old_letters_guessed: list
        :return: true if the letter is legal and false if not
        :rtype: bool"""
    if not(letter_guessed.isalpha()) or int(len(letter_guessed)) > 1 or letter_guessed.upper() in old_letters_guessed or letter_guessed.lower() in old_letters_guessed:
        return False
    else:
        return True
    
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """ checks if the letter that the user typed is legal(eng letter ,1 char , in the list already)
        :param letter_guessed: the geussed letter
        :param old_letters_guessed: list of all geussed letters
        :type letter_guessed: str
        :type old_letters_guessed: list
        :return: true if the letter is legal and false if not
        :rtype: bool"""
    if check_valid_input(letter_guessed, old_letters_guessed) == False:
        print(" -> ".join(sorted(old_letters_guessed)))
        return False
    else:
        old_letters_guessed.append(letter_guessed)
        return True


def print_hangman(place):
    """ dictionary of all the hangman positions from 1 to 6 and prints the position by place param
        :param place: which hangman to print
        :type place: int
        """
    HANGMAN_PHOTOS = {
    '1' : """x-------x""" 
    ,'2': """x-------x\n|\n|\n|\n|\n|\n"""
    ,'3': """x-------x\n|\t|\n|\t0\n|\n|\n|\n""" 
    ,'4': """x-------x\n|\t|\n|       0\n|      /|\\\n|\n|"""
    ,'5': """x-------x\n|\t|\n|       0\n|      /|\\\n|      /\n|\n"""
    ,'6': """x-------x\n|\t|\n|       0\n|      /|\\\n|      / \\\n|\n"""
    }
    print(HANGMAN_PHOTOS[str(place)]+"\n")


def print_opening_page():
    ## Print the Opening Screen
    HANGMAN_ASCII_ART = '''  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/ '''
    MAX_TRIES = 6
    print(HANGMAN_ASCII_ART+"\n\nYou Have "+str(MAX_TRIES)+" Attemps to Win!")

def main():
    print_opening_page()                
    path , index , old_letters_guessed , MAX_TRIES = input('\nEnter file path: ') , int(input('Enter index: ')), [] , 6   ##creating the new vars
    secret_word = choose_word(path , index)
    print("\nLets Play!\n\n\t")
    show_hidden_word(secret_word , old_letters_guessed)                                                             ## print the hidden word with _
    count_tries = 1
    while check_win(secret_word, old_letters_guessed) != True:                                                      ##while the user dont win or getting the max amount of attemps , the program will try this block over and over
        if count_tries>MAX_TRIES:                                                                                   ## if the user used all of his attemps he will LOSE
            break
        geussed_letter = input('\nGuess a letter: ')
        if check_valid_input(geussed_letter , old_letters_guessed):                                                 ##checking if the letter is legal by function
            if geussed_letter not in old_letters_guessed and geussed_letter.lower() not in secret_word :            ##checking if the user didnt geussed this letter before and didnt in secret word
                old_letters_guessed.append(geussed_letter.lower())                                                  ##if so , the letter will add to the old_letters_guessed list and the attempts counter will rise up
                print(':( \n***Youve Got ' + str(MAX_TRIES - count_tries) + ' More Tries***')
                print_hangman(count_tries)
                count_tries +=1
                show_hidden_word(secret_word , old_letters_guessed)
            elif try_update_letter_guessed(geussed_letter.lower(), old_letters_guessed):{                           ##checking if the letter is correct and not in the geussed list
            show_hidden_word(secret_word , old_letters_guessed)
        }
        else : 
            if geussed_letter in old_letters_guessed:
                print('You Already Guessed This Letter\n')
            else:
                print("not a vaild input!")
    if count_tries>MAX_TRIES:                                                                                       ##if the user tries are bigger then he lose
        print("\n\nYou lost")
    else:
        print("\n\nCongrats You Won!!")

if __name__ == "__main__":
    main()