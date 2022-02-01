# MARC BAEGERT
# IA-M1VS-DS


# 1. Création de fonction mathématique simple en Python (12 points) :
# 2. Création de fonction comportant des modules de gestions des
# exceptions (5 points) :

##################################################################################################
# Import de la librairie
import math


##################################################################################################
print("#"*10,"Fonction func_poly (sans gestion entrée):","#"*10)
# Fonction func_poly (sans gestion entrée):
def func_poly(nombre_reel = 0):
    """
    Cette fonction retoune le résultat de la fonction polynomiale:
    f(x)=x^3-1,5x²-6x+5
    """
    resultat = nombre_reel**3-1.5*nombre_reel**2-6*nombre_reel+5
    return(resultat)

######### TEST #########
test_001 = func_poly(5)
print(test_001)
######### TEST #########
# Doit afficher 62,5

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
# Fonction func_poly (avec gestion entrée): -------------
print("#"*10,"Fonction func_poly_corr (avec gestion entrée):","#"*10)
def func_poly_corr(nombre_reel = 0):
    """
    Cette fonction retoune le résultat de la fonction polynomiale:
    f(x)=x^3-1,5x²-6x+5
    """
    # Gestion de l'entrée:
    nombre_reel_corr = give_limit_value(nombre_reel,list_good =[int,float])
    
    resultat = nombre_reel_corr**3-1.5*nombre_reel_corr**2-6*nombre_reel_corr+5
    return(resultat)

######### TEST #########
test_001 = func_poly_corr(5)
print(test_001)
######### TEST #########
# Doit afficher 62,5


######### TEST #########
test_002 = func_poly_corr(5.57665)
print(test_002)
######### TEST #########
# Doit afficher 98.319


######### TEST #########
test_003 = func_poly_corr(6)
print(test_003)
######### TEST #########
# Doit afficher 131.0

######### TEST #########
test_004 = func_poly_corr(5+6j)
print(test_004)
######### TEST #########
# Doit afficher Oops!  Ce n'est pas un type correct.  Essayez encore...
# Puis 21 en saissisant 4


######### TEST #########
test_005 = func_poly_corr(-23)
print(test_005)
######### TEST #########
# Doit afficher Votre valeur "X" n'est pas un nombre compris dans la borne : [ 0 , 999 ]
# Puis 11240.5 en saissisant 23


######### TEST #########
test_006 = func_poly_corr("Vive les partiels")
print(test_006)
######### TEST #########
# Doit afficher Oops!  Ce n'est pas un type correct.  Essayez encore...
# Puis -5.0 en saissisant 2