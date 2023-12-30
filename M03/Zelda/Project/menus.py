from funciones import *
import os

def clear_terminal():
    if os.name == 'nt':  # Para sistemas Windows
        _ = os.system('cls')
    else:  # Para sistemas Unix/Linux/MacOS
        _ = os.system('clear')

###################################   MENU PRINCIPAL    ############################################
def menu1():
    print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
        "\n *                                                             ##              * "
        "\n *                                                             ##              * "
        "\n *                                                          ##~~~              * "
        "\n *                                                          ##~~~O             * "
        "\n *    Zelda, Breath of the Wild                            ###~~~ \            * "
        "\n *                                                           |@@@| \           * "
        "\n *                                                           |   |  \          * "
        "\n *                                                           =   ==            * "
        "\n *                                                       %%%%%%%%%%%%          * "
        "\n *                                                    %%%%%%%%%%%%%%%          * "
        "\n * Continue, New Game, Help, About, Exit * * * * * * * * * * * * * * * * * * * * "
    )

def menu2():
     print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
        "\n *                                                             &&              * "
        "\n *                                                            oo &             * "
        "\n *                                                    $       -- &##           * "
        "\n *                                                    $$    <<OO####           * "
        "\n *    Zelda, Breath of the Wild                        $$  //OOO####           * "
        "\n *                                                      $$// OO#####           * "
        "\n *                                                       **  OOO###            * "
        "\n *                                                        &  @@@@\             * "
        "\n *                                                            Q  Q             * "
        "\n *                                                            Q  Q             * "
        "\n * Continue, New Game, Help, About, Exit * * * * * * * * * * * * * * * * * * * * "
    )

def menu3():
    print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
        "\n *                                                             &&              * "
        "\n *                                                            ####             * "
        "\n *                                                           ||                * "
        "\n *                                                        @@@@@@@@@@@@         * "
        "\n *    Zelda, Breath of the Wild                          @     ||@@@           * "
        "\n *                                                             |@@@            * "
        "\n *                                                            @@@              * "
        "\n *                                                         @@@@||     @        * "
        "\n *                                                      @@@@@@@@@@@@@          * "
        "\n *                                                             ||              * "
        "\n * Continue, New Game, Help, About, Exit * * * * * * * * * * * * * * * * * * * * "
    )



#############################################################################################################


#########################################   HELP, MAIN MENU    ##############################################


def helpMainMenu():
     print("* Help, main menu * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
        "\n *                                                                             * "
        "\n *                                                                             * "
        "\n *                 Type 'continue' to continue a saved game                    * "
        "\n *                 Type 'new game' to start a new game                         * "
        "\n *                 Type 'about' to see information about the game              * "
        "\n *                 Type 'exit' to exit the game                                * "
        "\n *                                                                             * "
        "\n *                 Type 'back' now to go back to the 'Main menu'               * "
        "\n *                                                                             * "
        "\n *                                                                             * "
        "\n * Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * "
    )



#########################################   SAVED GAMES, MENU    ##############################################
                                                                                                              #
def savedGamesMenu():                                                                                         #
     print("* Saved games * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"                  #
        "\n *                                                                             * "                 #
        "\n *                                                                             * "                 #
        "\n *                                                                             * "                 #
        "\n *                                                                             * "                 #
        "\n *                                                                             * "                 #
        "\n *                                                                             * "                 #
        "\n *                                                                             * "                 #
        "\n *                                                                             * "                 #
        "\n *                                                                             * "                 #
        "\n *                                                                             * "                 #
        "\n * Play X, Erase X, Help, Back * * * * * * * * * * * * * * * * * * * * * * * * *"                  #
    )                                                                                                         #
                                                                                                              #
                                                                                                              #
#########################################   HELP SAVED GAMES, MENU    #########################################
                                                                                                              #
def helpSavedGamesMenu():                                                                                     #
     print("* Help, saved games * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"                  #
        "\n *                                                                             * "                 #
        "\n *                                                                             * "                 #
        "\n *                  Type 'play X' to continue playing the game 'X'             * "                 #
        "\n *                  Type 'erase X' to erase the game 'X'                       * "                 #
        "\n *                  Type 'back' now to go back to the main menu                * "                 #
        "\n *                                                                             * "                 #
        "\n *                                                                             * "                 #
        "\n *                                                                             * "                 #
        "\n *                  Type 'back' now to go back to 'Saved games'                * "                 #
        "\n *                                                                             * "                 #
        "\n * Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * "                 #
    )                                                                                                         #
                                                                                                              #
###############################################################################################################



#########################################   NEW GAME, MENU    ##################################################
                                                                                                               
                                                                                                               
def newGameMenu():
    clear_terminal()

    print(" * New game  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
          "\n *                                                                             * "
          "\n *                                                                             * "
          "\n *                                                                             * "
          "\n *                                                                             * "
          "\n *                                                                             * "
          "\n *                  Set your name ?                                            * "
          "\n *                                                                             * "
          "\n *                  Type 'back' now to go back to 'Main Menu'                  * "
          "\n *                                                                             * "
          "\n * Back, Help  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
    )

    while True:
        player_name = input("What's your name (Link)? ").strip()  # Elimina espacios al inicio y final

        if player_name.lower() == 'back':
            mostrar_menu_aleatorio()
            prompt_usuari()
            break

        # Verificar si se ha ingresado un nombre
        if not player_name:
            player_name = 'Link'  # Asignar 'Link' si no se ingresa un nombre

        # Verificar validez del nombre
        if player_name.isalnum() or ' ' in player_name:
            # Validar que solo contiene letras, números y espacios
            print(f"Welcome to the game, {player_name}")
            # Ir a la sección 'Legend'
            legendMenu(player_name)  # Pasar player_name a legendMenu()
            break
        else:
            print(f'"{player_name}" is not a valid name')   
            
                                                                                                                 
                                                                                                               
#########################################   HELP NEW GAME, MENU    #############################################
                                                                                                               #     
                                                                                                               #
def helpNewGameMenu():                                                                                             #
     print("* Help, New game  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"                   #
        "\n *                                                                             * "                  #
        "\n *                                                                             * "                  #
        "\n *       When asked, type your name and press enter                            * "                  #
        "\n *       if 'Link' is fine for you, just press enter                           * "                  #
        "\n *                                                                             * "                  #
        "\n *       Name must be between 3 and 10 characters long and only                * "                  #
        "\n *       letters, numbers and spaces are allowed                               * "                  #
        "\n *                                                                             * "                  #
        "\n *       Type 'back' now to go back to 'Set Your Name'                         * "                  #
        "\n *                                                                             * "                  #
        "\n * Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * "                  #
    )                                                                                                          #
                                                                                                               #
################################################################################################################
     


##############################################  ABOUT, MENU    ##################################################
                                                                                                                #
def aboutMenu():                                                                                                #
     print("* About * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"                    #
        "\n *                                                                             * "                   #
        "\n *       Game developed by ‘Team 2, The hometown bugs’ :                       * "                   #
        "\n *                                                                             * "                   #
        "\n *                                                                             * "                   #
        "\n *             Arnau Mestre                                                    * "                   #
        "\n *             Adria Martinez                                                  * "                   #
        "\n *             Moha  El Amine                                                  * "                   #
        "\n *                                                                             * "                   #
        "\n *                                                                             * "                   #
        "\n *                                                                             * "                   #
        "\n * Back  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * "                   #
    )                                                                                                           #
                                                                                                                #
#################################################################################################################
     

##############################################  LEGEND, MENU    #################################################
                                                                                                                
def legendMenu(player_name):
        clear_terminal()
        print(" * Legend * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
              "\n *    10,000 years ago, Hyrule was a land of prosperity thanks to the Sheikah * "
              "\n *    tribe. The Sheikah were a tribe of warriors who protected the Triforce, * "
              "\n *    a sacred relic that granted wishes.                                     * "
              "\n *                                                                            * "
              "\n *    But one day, Ganondorf, an evil sorcerer, stole the Triforce and began  * "
              "\n *    to rule Hyrule with an iron fist.                                       * "
              "\n *                                                                            * "
              "\n *    The princess, with the help of a heroic young man, managed to defeat    * "
              "\n *    Ganondorf and recover the Triforce.                                     * "
              "\n *                                                                            * "
              "\n * Continue * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
        )

        while True:
            user_input = input("Type 'continue' to continue: ")

            if user_input.lower() == 'continue':
                
                plotMenu(player_name)
                break
            else:
                print("Invalid action.")

#################################################################################################################
     



################################################  PLOT, MENU    #################################################
                                                                                                                
def plotMenu(player_name):
    clear_terminal()

    print(" * Plot * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
          "\n *                                                                            * "
          "\n *                                                                            * "
         f"\n *   Now history is repeating itself, and Princess Zelda has been captured by * "
          "\n *   Ganon. He has taken over the Guardians and filled Hyrule with monsters.  * "
          "\n *                                                                            * "
          "\n *                                                                            * "
          f"\n *   But a young man named '{player_name}' has just awakened and                        * "
          "\n *   must reclaim the Guardians to defeat Ganon and save Hyrule.              * "
          "\n *                                                                            * "
          "\n *                                                                            * "
          "\n * Continue  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
    )
    while True:
        user_input = input("Type 'continue' to continue: ")

        if user_input.lower() == 'continue':
            print("The adventure begins")
            # Start the game section
            break
        
        else:
            print("Invalid action")
                                                                                                          
#################################################################################################################



################################################  DEAD    #######################################################
                                                                                                                
def deadMenu():                                                                                                 
     print("* Link Dead  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"                     
        "\n *                                                                            * "                    
        "\n *                                                                            * "                    
        "\n *                                                                            * "                    
        "\n *                                                                            * "                    
        "\n *      Game Over                                                             * "                    
        "\n *                                                                            * "                    
        "\n *                                                                            * "                    
        "\n *                                                                            * "                    
        "\n *                                                                            * "                    
        "\n * Continue * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * "                    
    )

#################################################################################################################



def rellenarEspacios(string):
    spaces = 79 - len(string)
    if spaces > 0:
        string += " " * spaces
    elif spaces < 0:
        string = string[:79]
    string += "*"
    return string



def map(santuarios):
    map = [
        f"\n* Map * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *",
        f"\n*                                                         *                   *",
        f"\n*  Hyrule        {str(santuarios[0]).rjust(3)}                       Death Mountain *                   *",
        f"\n*                                 {str(santuarios[2]).rjust(3)}                     *                   *",
        f"\n*        {str(santuarios[1]).rjust(3)}                                    {str(santuarios[3]).rjust(3)}       *                   *",
        f"\n*                                                         *                   *",
        f"\n*                         Castle                          *                   *",
        f"\n*                                                         *                   *",
        f"\n*                {str(santuarios[4]).rjust(3)}                                 {str(santuarios[5]).rjust(3)}  *                   *",
        f"\n*  Gerudo                             {str(santuarios[6]).rjust(3)}        Necluda  *                   *",
        f"\n*                                                         *                   *",
        f"\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
    ]

    print("".join(map))










def separarWeapons(equipment):
    uses = []
    count = []
    equipped = []

    for i in equipment:
        uses.append(i["uses"])
        count.append(i["count"])
        if i["equipped"] == True:
            equipped.append("  (equipped)")
        else:
            equipped.append("")
    return uses, count, equipped

def separarFood(foods):
    count = []
    hearts = []

    for i in foods:
        count.append(i["count"])
        hearts.append(i["hearts"])
    return count, hearts

def separarSantuarios(player_name):
    santuarios = []

    for clave, i in player[player_name]["sanctuaries"].items():
        if i == True:
            santuarios.append(clave + "?")
        else:
            santuarios.append(clave)
    return santuarios

def separarPlayer(equipment):
    listas = [[], [], [], []]  

    for clave,i in equipment.items():
        count = -1    

        for j in i.values():
            count += 1
            for k in j.values():
                listas[count].append(k)

    return clave, listas




