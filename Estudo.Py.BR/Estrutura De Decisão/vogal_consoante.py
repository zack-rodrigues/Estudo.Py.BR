letra=str(input('Type an letter so we can tell if its Vowel or Consonant:  '))

vogais = 'aeiouAEIOU'

if letra in vogais and letra .isalpha():
    print('É uma vogal')

elif letra not in vogais and letra .isalpha():
    print('É uma consoante')

else:
    print('is not an letter')
