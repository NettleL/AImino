from colorama import  Fore, Back, Style

def colr(text):
    return(Style.DIM + Fore.CYAN + text + Style.RESET_ALL)

def bold(text):
    return(Style.BRIGHT + text + Style.NORMAL)

def back(text):
    return(Back.WHITE + text + Back.RESET)