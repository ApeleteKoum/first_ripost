print("=== Vérificateur d'éligibilité UL ===")
Age = int(input("Age :"))
Mention = input("Mention au BAC : ")
inscrit = input("Inscrit à l'UL (Oui/Non) :")
moyenne = input("Votre Moyenne generale sur 20 :")
nation = input("Nationalité : ") 


critAge = Age <= 22
#critmoyenne = float(moyenne)<= 12 
critMention = (Mention == "Tres Bien") or (Mention == "Assez Bien") or (Mention == "Bien")
critinscrit = (inscrit == "Oui")
critnation = (nation == "Togolaise")

eligible = critAge and critMention and critinscrit and critnation

print("\n=== Résultat ===")
print("Age <=22 : ", critAge)
#print("Moyenne < 12 : ", critmoyenne)
print("Mention Bien ou Tres Bien : ", critMention)
print("Inscrit à l'UL : ", critinscrit)
print("Nationalité Togolaise : ", critnation)
print("\nÉligibilité générale (tous critères vrais) : ", eligible)