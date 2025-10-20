import json
with open("client.json","r") as f:
    client= json.load(f)

with open("film.json","r") as f:
    sceance = json.load(f)


while True:
    conexion_inscription = input("connexion ou inscription ?")
    conexion_inscription = conexion_inscription.lower().strip()

    if conexion_inscription == "inscription" :
        pseudo = input("choix du pseudo ")
        pseudo = pseudo.lower().strip()
        if  pseudo not in client :
         password = input("choix du mots de passe ")
         age = int(input("Quelle age avez-vous ? "))
         sold =int(input("de combien voulez-vous crediter votre compte ? "))
         client[pseudo] ={"password":password,"age":age,"sold":sold}
         print("votre compte a bien été enregistré")
         with open("exo//cinéma//client.json","w") as f:
            json.dump(client,f,indent=4)
         break
        else:
            print("pseudo deja utiliser")
    if conexion_inscription == "connexion":
        break
    else:
        print("je n'est pas compris votre réponce essayer a nouveau")


compteur = 0
while True :
    print("vous aver", 3 - compteur ,"essai")
    if compteur ==  3 :
        print("limite atteinte")
        exit()
    pseudo = input("quelle est votre pseudo ? ")
    password = input("quelle est votre mots de passe? ")
    pseudo = pseudo.strip().lower()
    if pseudo in client and password == client[pseudo]["password"]:
        print(" bienvenue " + pseudo)
        break
    else:
        print("votre pseudo ou votre mots de passe est inconu ?")
        compteur += 1

while True:
    print("1 pour modifier votre compte ")
    print("2 pour accéder au sceance ")
    menu_sceance = int(input("quelle est votre choix ? "))
    if menu_sceance == 1:
        while True:
            print("    menue   ")
            print("que vouler vous modifier ?")
            print("1 =  pseudo")
            print("2 =  mots de passe")
            print("3 =  age ")
            print("4 pour créditer le compte")
            print("5 pour quiter le menue")
            film_modif= int(input("entré le numéro de votre choix ? "))
            if film_modif == 1:
                while True :
                    new_pseudo = input("nouveau pseudo ?")
                    new_pseudo = new_pseudo.lower().strip()
                    if new_pseudo in client:
                        print("ce pseudo est deja utiliser")
                    if new_pseudo == pseudo:
                        print("pseudo identique")
                        break
                    else :
                        client[new_pseudo] = client[pseudo]
                        del client[pseudo]
                        pseudo = new_pseudo
                        print(client) 
                        break
            if film_modif == 2:
                new_password = input("nouveau mots de passe ?")
                client[pseudo]["password"] = new_password
            if film_modif == 3:
                new_age = int(input("quelle age avez-vous ?"))
                client[pseudo]["age"] = new_age
            if film_modif == 4:
                crediter = int(input("de combien voulez-vous créditer ?"))
                client[pseudo]["sold"] = client[pseudo]["sold"] + crediter
            if film_modif == 5:
                with open("client.json","w") as f:
                    json.dump(client,f,indent=4)
                break
    if menu_sceance == 2:
        break

    print(client)



print(pseudo, client[pseudo]["age"],"ans", "et votre sold est de {}$".format(client[pseudo]["sold"]) )

print(sceance)

while True:
    sceance_choix = input("quelle film voulez-vous regarder ? ")
    sceance_choix = sceance_choix.strip().lower()
    if sceance_choix in sceance :
        break
    else:
        print("le film n'existe pas essayer encore")



if client[pseudo]["age"] < sceance[sceance_choix]["age min"]:
    print("vous n'aver pas lage pour ce contenue")
    exit()


with open("reduc.json","r") as f:
    reduc = json.load(f)

print(reduc)
            
while True:
    price = input("choisir un tarif, un justificatif peut vous etre demander ? ")
    price = price.lower().strip()
    if price == "enfant":
        if client[pseudo]["age"] <= 10:
            break
        else:
             print("vous n'aver pas lage requi")
    if price == "segnor":
         if client[pseudo]["age"] >= 60:
                break
         else:
             print("vous n'aver pas lage requi")
    if price in reduc:
        break
    else:
        print("je n'est pas comprit votre reponce ")

price  = reduc[price]

print("la place de cinéma  est de {}$".format(price))
while True:
    popcorn = input("voulez-vous du popcorn ? oui/non ")
    popcorn = popcorn.strip().lower()
    if popcorn == "oui":
        price +=  5
        break
    if popcorn == "non":
        print("tampis une prochaine fois ")
        break

print("le total de vos achat est de {}$".format(price),"votre sold est de {}$".format(client[pseudo]["sold"]))
while True :
    if price > client[pseudo]["sold"] :
        crediter = input("font inssufisant,voulez-vous recrédier votre compte oui/non ?")
        crediter = crediter.lower().strip()
        if crediter == "oui":
            credit = int(input("de combien voulez-vous crediter? "))
            client[pseudo]["sold"] += credit
            break
        if crediter == "non":
            print("bonne journé")
            exit()
    else:
        break

client[pseudo]["sold"] -=  price
print("merci de votre achat,votre solde est de {}$".format(client[pseudo]["sold"]))
print("bonne sceance")

with open("client.json","w") as f:
    json.dump(client,f,indent=4)

exit()




