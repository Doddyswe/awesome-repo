alfabet = 'abcdefghijklmnopqrstuvwxyzåäö'
key = int(input('Var god ange ett heltal som nyckel...'))
nyttMeddelande = ''

meddelande = input('Var god ange ett meddelande...')
for bokstav in meddelande:
    if bokstav in alfabet:
        position = alfabet.find(bokstav)
        nyPosition = (position + key) % 29
        nyBokstav = alfabet[nyPosition]
        nyttMeddelande += nyBokstav
    else:
        nyttMeddelande += bokstav

print(nyttMeddelande)
