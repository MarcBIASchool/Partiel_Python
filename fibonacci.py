# MARC BAEGERT
# IA-M1VS-DS


# 1. Création de fonction mathématique simple en Python (12 points) :
# 2. Création de fonction comportant des modules de gestions des
# exceptions (5 points) :


##################################################################################################
# Import de la librairie
import math


##################################################################################################
print("#"*10,"Fonction suite_fibonnaci (sans gestion entrée):","#"*10)
# Fonction fibonnaci (donne un nombre de la suite de fibonnaci):
def fibonnaci(nombre_reel=0):
    """
    Cette fonction définit les nombres de la suite de fibonnaci
    """
    # Génération de la suite de fibonnaci:
       #Gestion de 1 et 0
    if nombre_reel == 0:
        return(0)
    elif nombre_reel == 1:
        return(1)
    else:
        #Les nombres sont plus grand que 1 et 0
        return(fibonnaci(nombre_reel-1)+fibonnaci(nombre_reel-2))
    
# Fonction suite_fibonnaci (La suite de fibonnaci en fonction d'un index):
def suite_fibonnaci():
    """
    Cette fonction permet d'intéragir avec l'utilisateur (prise en compte d'une entrée)
    et retourne la suite de fibonnaci associé
    Exemple:
        suite_fibonnaci() ---------------------
        | Entrez un nombre : 3
        | La suite de fibonacci est :
        |   >>> 0,1,1,2
        |--------------------------------------
    """
    # Gestion de l'entrée:
    input_user = int(input("Entrez un nombre: "))
    
    # Génération de la suite de fubonacci:
    suite_f = []
    for i in range(input_user+1):
        suite_f.append(fibonnaci(i))
    print(f"La suite de fubonacci F{input_user} est:")
    print(f"   >>> {suite_f}")

######### TEST #########
suite_fibonnaci()
######### TEST #########
# En entrée on a 6
# Doit afficher 0,1,1,2,3,5,8

print("#"*50)

##################################################################################################
# Fonction d'aide à la gestion des inputs:---------------
def check_type(value,list_good =[int]):
    """
    def check_type(value,list_good =[int]): return 1 if value type is in list good
    
    Inputs:
        - list_good : list of accepted type for value
        - value : it's an element to compare
    Ouput:
        - good: return 1 if value has a good type or 0 if not
    """
    type_value = type(value)

    # On édite une variable good indiquant si la variable d'entrée est bonne: 1->ok | 0->nok
    good = [1 for i in list_good if i == type_value]
    if len(good) == 0:
        good = 0
    else:
        good = 1
        
    return good


def give_right_type(value, list_good =[int], force_int = False):
    """
    def give_right_type(value, list_good =[int]) : ask user to give a good value type
    
    Inputs:
        - list_good : list of accepted type for value
        - value : it's an element to compare
        - force_int : Force le passage en entier quand c'est possible
    Ouput:
        - value_r: return a better value (with a good type)
    """
    # On regarde si le type est correct ou non:
    good_type = check_type(value,list_good)
    value_r = value
    index_while = 0
    
    while good_type<1: 
        try:
            value_r = float(value_r)
            if force_int == True:
                value_r = int(math.floor(value_r))
        except:
            print("Oops!  Ce n'est pas un type correct.  Essayez encore...")
            value_r = input("Entrez un entier:")
            
        good_type = check_type(value_r,list_good)    
    return value_r



def give_limit_value(value, bornes =[0,999],list_good =[int],force_int = False):
    """
    give_limit_value(value, bornes =[0,999],list_good =[int]):
    
    Inputs:
        - list_good : list of accepted type for value
        - bornes : defines the min and max value of value
        - value : it's an element to compare
        - force_int : Force le passage en entier quand c'est possible
    Ouput:
        - value_r: return a better value (with a good type)
    """
    # On vérifie le type de la valeur d'entrée:
    value_r = give_right_type(value, list_good,force_int)
    
    # On vérifie la valeur de value_r par rapport aux bornes:
    while (value_r<bornes[0]) | (value_r>bornes[1]):
        print(f"Votre valeur {value_r} n'est pas un nombre compris dans la borne : [ {bornes[0]} , {bornes[1]} ] ")
        value_r = "wrong"
        value_r = give_right_type(value_r, list_good,force_int)
        
    return value_r


##################################################################################################
# Fonction suite_fibonnaci_corr (avec gestion entrée): -------------
print("#"*10,"Fonction suite_fibonnaci_corr (avec gestion entrée):","#"*10)
def suite_fibonnaci_corr():
    """
    Cette fonction permet d'intéragir avec l'utilisateur (prise en compte d'une entrée)
    et retourne la suite de fibonnaci associé
    Exemple:
        suite_fibonnaci() ---------------------
        | Entrez un nombre : 3
        | La suite de fibonacci est :
        |   >>> 0,1,1,2
        |--------------------------------------
    """
    # Gestion de l'entrée:
    input_user = input("Entrez un nombre: ")
    input_user_corr = give_limit_value(input_user,force_int=True)
    
    
    # Génération de la suite de fubonacci:
    suite_f = []
    for i in range(input_user_corr+1):
        suite_f.append(fibonnaci(i))
    print(f"La suite de fubonacci jusqu'au F{input_user_corr} est:")
    print(f"   >>> {suite_f}")

######### TEST #########
suite_fibonnaci_corr()
######### TEST #########
# En entrée on a 6
# Doit afficher 0,1,1,2,3,5,8

######### TEST #########
suite_fibonnaci_corr()
######### TEST #########
# En entrée on a 4.3
# Doit afficher 0, 1, 1, 2, 3

######### TEST #########
suite_fibonnaci_corr()
######### TEST #########
# En entrée on a -2
# Doit afficher Votre valeur -2 n'est pas un nombre compris dans la borne : [ 0 , 999 ]

######### TEST #########
suite_fibonnaci_corr()
######### TEST #########
# En entrée on a 9999999999
# Doit afficher Votre valeur 9999999999 n'est pas un nombre compris dans la borne : [ 0 , 999 ]

######### TEST #########
suite_fibonnaci_corr()
######### TEST #########
# En entrée on a j+1
# Doit afficher Oops!  Ce n'est pas un type correct.  Essayez encore...


######### TEST #########
suite_fibonnaci_corr()
######### TEST #########
# En entrée on a "Vive les partiels"
# Doit afficher Oops!  Ce n'est pas un type correct.  Essayez encore...