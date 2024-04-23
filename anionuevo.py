import colorama
import time
import random

colorama.init()

def print_colored(text, color):
    print(color + text + colorama.Style.RESET_ALL, end='')

feliz_ano_nuevo = [
    "##### #### #    ### #####    ####  ###### #####   #   # #   # #### #   #  #####",
    "#     #    #     #     #    #    # #    # #   #   ##  # #   # #    #   #  #   #",
    "####  #### #     #    #     ###### # #  # #   #   # # # #   # ####  # #   #   #",
    "#     #    #     #   #      #    # #  # # #   #   #  ## #   # #     # #   #   #",
    "#     #### #### ### #####   #    # #    # #####   #   # ##### ####   #    #####"
]



colors = [
    colorama.Fore.RED, colorama.Fore.GREEN, colorama.Fore.YELLOW,
    colorama.Fore.BLUE, colorama.Fore.MAGENTA, colorama.Fore.CYAN
]

while True:
    for line in range(len(feliz_ano_nuevo)):
        for char_index in range(len(feliz_ano_nuevo[line])):
            if feliz_ano_nuevo[line][char_index] == '#':
                random_color = random.choice(colors)
                print_colored('#', random_color)
            else:
                print(feliz_ano_nuevo[line][char_index], end='')
        print()
    time.sleep(0.2)
    print("\033[H\033[J")
