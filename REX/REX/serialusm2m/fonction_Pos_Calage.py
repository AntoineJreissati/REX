"""
Created on Mon Sep 30 16:16:22 2023 (in Bangkok Baby)
@author: Antoine Jreissati
code Pos,calage SerialusM2M
"""

import serialusM2M as s


'''
    reponse du style  cf fonction envoi_reponse @serialusM2M.py:

    Returns:
        list: Une liste contenant les éléments suivants dans l'ordre :
            - La donnée reçue en sortie (data_out)
            - La donnée reçue en entrée (data_in)
            - Indique si une erreur de lecture s'est produite (err_read)
            - Indique si une erreur de décodage s'est produite (err_decode)
            - Indique si une erreur de réception du message attendu s'est produite (err_recep_msg)
            - Le temps écoulé pour l'opération reponse (timer)
            - Le temps écoulé pour l'opération complete (timer)
    
'''


def get_pos(ser):
    code_function = '00'
    reponse = s.Envoi_reponse(code_function, ser)
    XYT=reponse[1]
    try:
        X,Y,T=XYT.split("_")
        return X,Y,T
    except:
        return XYT

def set_pos(x,y,t,ser):
    code_function = '010'
    if len(x) != 4:
        return False
    if len(y) != 4:
        return False
    if len(t)!=3:
        return False
    reponse = s.Envoi_reponse(code_function + x + y, ser)
    return reponse[1]

def get_Couleur(ser):
    code_function = '500'
    reponse = s.Envoi_reponse(code_function, ser)
    couleur=reponse[1]
    
    return couleur #bleu=0
                    #jaune=1

def set_Couleur(couleur,ser):
    code_function = '510'
    reponse = s.Envoi_reponse(code_function+couleur, ser)
    couleur=reponse[1]
    return couleur


def Callage_All(ser):
    """
    Fonction pour envoyer une commande pour caler le robot avec la fonction callage_all depui strategie.c le robot.

    Returns:
        tuple:
            - Réponse du robot
    """
    code_function = '120'
    
    reponse = s.Envoi_reponse(code_function, ser)
    XYT=reponse[1]
    try:
        X,Y,T=XYT.split("_")
        return X,Y,T
    except:
        return XYT
        
    

"""   
serial_port = '/dev/ttyUSB0'
Baudrate=1000000    
ttl9600=False
Timeout=2
ser=s.init_serial(Baudrate,serial_port,Timeout,False)

print(get_pos(ser))

ser.close()
"""

def Callage_X(x,t,sens,v,ser):
    """
    Fonction pour envoyer une commande pour caler le x du robot.

    Args:
        x (str, 4): pos_x en millimètres.
        t(ste, 3): pos_theta en deg (0-360)
        v(str, 3): Vitesse de déplacement en %.
        sens(str,1): sens 
        
        ser (serial.Serial): Objet de la connexion série.

    Returns:
        tuple:
            - Réponse du robot
    """
    code_function="100"
    reponse = s.Envoi_reponse(code_function+x+t+sens+v, ser)
    XYT=reponse[1]
    try:
        X,Y,T=XYT.split("_")
        return X,Y,T
    except:
        return XYT
    

def Callage_Y(y,t,sens,v,ser):
    """
    Fonction pour envoyer une commande pour caler le x du robot.

    Args:
        y(str, 4): pos_y en millimètres.
        t(ste, 3): pos_theta en deg (0-360)
        v(str, 3): Vitesse de déplacement en %.
        sens(str,1): sens 
        
        ser (serial.Serial): Objet de la connexion série.

    Returns:
        tuple:
            - Réponse du robot
    """
    code_function="110"
    reponse = s.Envoi_reponse(code_function+y+t+sens+v, ser)
    XYT=reponse[1]
    try:
        X,Y,T=XYT.split("_")
        return X,Y,T
    except:
        return XYT