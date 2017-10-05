positif = int(input('Entrez un nombre entier positif :'))

def calculeFact(positif):
    factoriel = positif
    while positif < 0 :
        positif = int(input('Entrez un chiffre plus grand que 0.'))
    factoriel = positif
    if positif == 0 :
        ('Le factoriel est 1')
    elif positif > 0 :
       while ( positif > 1):

             factoriel = factoriel * (positif - 1)
             positif = (positif - 1)
       return factoriel

print("Le factoriel est", calculeFact(positif), "!")