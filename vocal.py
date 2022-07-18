import pyttsx3 #importation


engine = pyttsx3.init() #initialisation
print("entrez une valeur svp !")
messs = input('')
print("nous allons lire votre text")
engine.say(messs)


engine.runAndWait()#close