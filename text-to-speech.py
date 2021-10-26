from gtts import gTTS
from playsound import playsound
from os import mkdir
from os.path import isdir
from colorama import Fore,Style

class Text_to_speech(object):
    
    def __init__(self):
        while True:
            choice = input(Fore.GREEN + '''  
            _________ Welcome to the text to the speech _________
            Choose your type of text please.
            1: File 
            2: text 
            q: quit
            choose > ''' + Style.RESET_ALL)

            if choice == '1':
                self.file_to_speech()
            elif choice == '2':
                self.text_to_speech()
            elif choice == 'q':
                break
            else:
                print(Fore.RED + 'Please choose between the choices !!' + Style.RESET_ALL)
                continue
    
    def file_to_speech(self):
        
        file_add = input(Fore.BLUE + 'The file address please > ' + Style.RESET_ALL)
        name = input('The mp3 file name you want to save (without .mp3) > ')
        with open(file_add , 'r') as file:
            text = file.read()
        tts = gTTS(text)
        self.__createdir()
        print( Fore.BLUE + 'please wait...' + Style.RESET_ALL)
        tts.save(f'audio/{name}.mp3')
        print(Fore.GREEN + f'The {name}.mp3 file has been saved !!' + Style.RESET_ALL)
        self.play(name)
        
    def play(self , name):
        play = input('Do you want to play it ?(yes or no) > ')
        if play == 'yes':
            playsound(f'audio/{name}.mp3')
        elif play == 'no':
            self.__init__()
        else :
            print(Fore.RED + 'Please choose between the choices !!' + Style.RESET_ALL)
    
    def text_to_speech(self):
        
        text = input('Give me your text please > ')
        name = input('The mp3 file name you want to save (without .mp3) > ')
        
        tts = gTTS(text)
        self.__createdir()
        print( Fore.BLUE + 'please wait...' + Style.RESET_ALL)
        tts.save(f'audio/{name}.mp3')
        print(Fore.GREEN + f'The {name}.mp3 file has been saved !!' + Style.RESET_ALL)

        self.play(name)
        
    def __createdir(self):
        #check if dir not exists create it
        if isdir('audio') == False:
            mkdir('audio')
            
tts = Text_to_speech()