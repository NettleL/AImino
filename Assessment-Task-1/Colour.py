from colorama import  Fore, Back, Style

def colr(text):
    return(Style.DIM + Fore.CYAN + text + Style.RESET_ALL) #colours/dims the selected text only

def bold(text):
    return(Style.BRIGHT + text + Style.RESET_ALL)