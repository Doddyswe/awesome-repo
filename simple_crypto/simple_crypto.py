#Caesar-cipher for the Swedish alphabet

#Initialize our swedish alphabet variable
alfabet='abcdefghijklmnopqrstuvwxyzåäö';
print('Första bokstaven i alfabetet är "%s" och den sista är "%s".' % (alfabet[0],alfabet[28]))

#Secret key variable
key = int(input('Var god ange ett heltal som nyckel...'));

#User input to encrypt
karaktär = input('Var god ange en bokstav...')
position = alfabet.find(karaktär);
print('Din bokstav har position %s i alfabetet.' % (position+1))

#Encrypt with new character by adding key to position
nyPosition = (position + key) % 29;
nyKaraktär = alfabet[nyPosition];
print('Den nya bokstaven har position %s i alfabetet.' % (nyPosition+1))

#Print the encrypted character
print('Den nya bokstaven är "%s".' % nyKaraktär)

#Decrypt each character by using the inverse key
decryptKey = (-1)*key;
decryptnyKaraktär = alfabet[(nyPosition+decryptKey)];
print('Bokstaven som dekrypterades med nyckeln du angav är %s.' % decryptnyKaraktär)
