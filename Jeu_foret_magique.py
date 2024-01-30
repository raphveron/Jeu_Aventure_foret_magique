import random
import os
import time

def clear_screen(delay=4):
    time.sleep(delay) 
    os.system('cls' if os.name == 'nt' else 'clear')

def display_pv(pv):
    print(color_text(f"PV restants: {pv}\n", "yellow"))

def color_text(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "end": "\033[0m",
    }
    return colors.get(color, "white") + text + colors["end"]

def get_user_choice():
    while True:
        choice = input("Votre choix (Oui/Non) : ").lower()
        if choice in ["oui", "non"]:
            return choice
        print("Veuillez répondre par 'Oui' ou 'Non'.")

def encounter_mage():
    print("Vous rencontrez un mage vereux qui vous demande de sacrifier un point de vie en échange d'un cadeau exceptionnel. Acceptez-vous ?")
    choice = get_user_choice()
    if choice == "oui":
        print("Le mage vous remet un crapeau vereux. Il glousse bizarrement. Vous perdez un point de vie.")
        return -1
    else:
        print("Vous refusez poliment. Le mage boude et disparaît dans un nuage de fumée.")
        return 0

def cross_bridge():
    print("Un pont suspendu semble être le seul moyen de traverser la rivière. Oserez-vous l'emprunter ?")
    choice = get_user_choice()
    if choice == "oui":
        print("Le pont craque sous votre poids, mais vous réussissez à traverser. Ouf !")
        return 0
    else:
        print("Sage décision. Un troll apparaît et répare le pont avec vous. il vous a pris pour une planche, Quelle chance vous ne perdez qu'un PV et traversez le ponts!")
        return -1

def talking_tree():
    print("Un arbre semble vous parler, demandant un de vos PV pour révéler un secret ancien. Écoutez-vous ?")
    choice = get_user_choice()
    if choice == "oui":
        print("L'arbre murmure : 'Ne fais jamais confiance aux arbres parlants.' Ironique. Vous perdez un PV.")
        return -1
    else:
        print("Vous ignorez l'arbre et passez votre chein.")
        return 0

def fee_farceuse():
    print("Une fée farceuse vous propose un marché : perdre un PV pour une chance de gagner deux. Acceptez-vous ?   ")
    choice = get_user_choice()
    if choice == "oui":
        print("La fée rit et vous donne deux PV. 'J'adore les joueurs audacieux !', dit-elle.")
        return 2
    else:
        print("La fée semble déçue mais vous laisse un PV pour votre prudence.")
        return 0

def mysterious_cavern():
    print("Une grotte mystérieuse promet trésors et dangers. Osez-vous y entrer ?")
    choice = get_user_choice()
    if choice == "oui":
        print("À l'intérieur, vous trouvez un PV... et un dragon ! Vous fuyez en vitesse. mais le dragon vous brule les fesse. Vous perdez 2 PV")
        return -1
    else:
        print("Vous passez votre chemin. Un peu plus loin, un écriteau indique 'Grotte des ours'. Ouf !")
        return 0

def old_well():
    print("Un vieux puits vous offre de l'eau magique. Un PV en moins pour goûter. Buvez-vous ?")
    choice = get_user_choice()
    if choice == "oui":
        print("L'eau vous revigore. Vous perdez un PV mais en gagnez deux. Rafraîchissant !")
        return 1
    else:
        print("Vous refusez. Plus loin, un panneau avertit : 'Eau empoisonnée'. Bonne décision !")
        return 0

def fun_mushroom():
    print("Un champignon rigolard promet de vous redonner un PV si vous acceptez de rire de sa blague. Acceptez-vous ?")
    choice = get_user_choice()
    if choice == "oui":
        print("Sa blague est terrible, mais vous riez poliment. Vous gagnez un PV, mais vous vous pendez sur place, il a tué votre bonne humeur.")
        return -10
    else:
        print("Vous passez votre chemin sans rire. Le champignon boude, mais vous gardez les pieds sur terre ...")
        return 0

def philosophale_stone():
    print("Une pierre brillante prétend pouvoir transformer un de vos PV en deux. Tentez-vous le sort ?")
    choice = get_user_choice()
    if choice == "oui":
        print("La pierre scintille et vous vous sentez revigoré. Vous gagnez un PV supplémentaire !")
        return +1
    else:
        print("Vous ignorez la pierre. Mais souvenez vous, la chance sourit aux prudents.")
        return 0

def lonely_wolf():
    print("Un loup solitaire vous défie en duel pour un de vos PV. Acceptez-vous le combat ?")
    choice = get_user_choice()
    if choice == "oui":
        print("Vous triomphez du loup et gagnez son respect... ainsi que .... son respect. Votre fesse droite est intact.")
        return + 1
    else:
        print("Vous refusez le duel. Le loup hoche la tête respectueusement et vous laisse passer. Lorsque vous lui tourner le dos il se jette sur votre fesse droite,et s'enfui dans la forets.")
        return -1

def sibylline_witch():
    print("Une sorcière vous propose un élixir mystérieux : perdre un PV maintenant pour en gagner deux plus tard. Buvez-vous ?")
    choice = get_user_choice()
    if choice == "oui":
        print("Vous buvez l'élixir. Rien ne se passe immédiatement, mais plus tard, vous gagnez deux PV.")
        return 2
    else:
        print("Prudent, vous refusez. La sorcière hoche la tête et vous donne un PV pour votre méfiance.")
        return 1

# Liste des étapes possibles
steps = [encounter_mage, cross_bridge, talking_tree, fee_farceuse, mysterious_cavern, old_well, fun_mushroom, philosophale_stone, lonely_wolf, sibylline_witch]

def game():
    pv = 3
    completed_steps = 0
        
    while pv > 0 and completed_steps < 10:
        if completed_steps == 0:
            clear_screen()
            display_pv(pv)
            print(color_text("Bienvenue dans la forêt magique ! Vous avez 3 PV. Votre but sera de sortir indemne de cette foret maudites.", "cyan"))
        clear_screen()
        display_pv(pv)
        step = random.choice(steps)
        pv += step()
        steps.remove(step)  # Retire l'étape de la liste pour éviter les répétitions
        completed_steps += 1
        time.sleep(2)

        if pv <= 0:
            clear_screen()
            display_pv(pv)
            print(color_text("Vous avez perdu tous vos PV. Game Over.", "red"))
            break
        if completed_steps == 10:
            clear_screen()
            display_pv(pv)
            print(color_text("Félicitations ! Vous avez survécu à la forêt maudite et gagné le jeu.", "green"))
            break

game()