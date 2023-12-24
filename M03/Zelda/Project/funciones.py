from datetime import datetime
import random



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
                                                                                                               #
                                                                                                               #
def newGameMenu():                                                                                             #
     print("* New game  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"                   #
        "\n *                                                                             * "                  #
        "\n *                                                                             * "                  #
        "\n *                                                                             * "                  #
        "\n *                                                                             * "                  #
        "\n *                                                                             * "                  #
        "\n *                  Set your name ?                                            * "                  #
        "\n *                                                                             * "                  #
        "\n *                                                                             * "                  #
        "\n *                  Type 'back' now to go back to 'Main Menu'                  * "                  #
        "\n *                                                                             * "                  #
        "\n * Back, Help  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * "                  #
    )                                                                                                          #
                                                                                                               #
#########################################   HELP NEW GAME, MENU    #############################################
                                                                                                               #     
                                                                                                               #
def newGameMenu():                                                                                             #
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
                                                                                                                #
def legendMenu():                                                                                               #
     print("* Legend * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"                     #
        "\n *    10,000 years ago, Hyrule was a land of prosperity thanks to the Sheikah * "                    #
        "\n *    tribe. The Sheikah were a tribe of warriors who protected the Triforce, * "                    #
        "\n *    a sacred relic that granted wishes.                                     * "                    #
        "\n *                                                                            * "                    #
        "\n *    But one day, Ganondorf, an evil sorcerer, stole the Triforce and began  * "                    #
        "\n *    to rule Hyrule with an iron fist.                                       * "                    #
        "\n *                                                                            * "                    #
        "\n *    The princess, with the help of a heroic young man, managed to defeat    * "                    #
        "\n *    Ganondorf and recover the Triforce.                                     * "                    #
        "\n *                                                                            * "                    #
        "\n * Continue * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * "                    #
    )                                                                                                           #
#################################################################################################################
     



################################################  PLOT, MENU    #################################################
                                                                                                                #
def plotMenu():                                                                                                 #
     print("* Plot * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"                     #
        "\n *                                                                            * "                    #
        "\n *                                                                            * "                    #
        "\n *   Now history is repeating itself, and Princess Zelda has been captured by * "                    #
        "\n *   Ganon. He has taken over the Guardians and filled Hyrule with monsters.  * "                    #
        "\n *                                                                            * "                    #
        "\n *                                                                            * "                    #
        "\n *   But a young man named 'Link' has just awakened and                       * "                    #
        "\n *   must reclaim the Guardians to defeat Ganon and save Hyrule.              * "                    #
        "\n *                                                                            * "                    #
        "\n *                                                                            * "                    #
        "\n * Continue * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * "                    #
    )                                                                                                           #
#################################################################################################################



################################################  DEAD    #######################################################
                                                                                                                #
def deadMenu():                                                                                                 #
     print("* Link Dead  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"                     #
        "\n *                                                                            * "                    #
        "\n *                                                                            * "                    #
        "\n *                                                                            * "                    #
        "\n *                                                                            * "                    #
        "\n *      Game Over                                                             * "                    #
        "\n *                                                                            * "                    #
        "\n *                                                                            * "                    #
        "\n *                                                                            * "                    #
        "\n *                                                                            * "                    #
        "\n *                                                                            * "                    #
        "\n * Continue * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * "                    #
    )

#################################################################################################################




###############################  OPCIONES MENU INICIO ##############################

# Lista de funciones de menú disponibles
menus = [menu1, menu2, menu3]

def mostrar_menu_aleatorio():
    menu_aleatorio = random.choice(menus)
    menu_aleatorio()

def prompt_usuari():
    opcions_valides = ["continue", "new game", "help", "about", "exit"]
    accio = input("What to do now? ").lower()
    
    while accio not in opcions_valides:
        print("Invalid action")
        accio = input("What to do now? ").lower()

    # Realitzar accions segons l'opció escollida
    if accio == "continue":
        # Acció per a "Continue"
        pass
    elif accio == "new game":
        # Acció per a "New Game"
        pass
    elif accio == "help":
        # Acció per a "Help"
        pass
    elif accio == "about":
        # Acció per a "About"
        pass
    elif accio == "exit":
        # Acció per a "Exit"
        pass


##################################################################################