x = input('Enter your name : ')
str2 = 'welcome '
str3 = str2.upper() + x.upper()
print('\n\t\t',str3.center(27,'*'))
print('\n\n\t\tYour game is about to begin,you\n\t\twill get four chances in this\n\t\tgame to guess the number b/w (1-8).')
import random
ran = random.randint(1,8)
for a in range(1,5):
    a = int(input('\nGuess the number here --->'))
    if a>ran:
        print('you hit the greater number')
    elif a<ran:
        print('you hit the smallest number')
    elif a==ran:
        print('\tYou hit the right number\n\tCONGRATULATIONS!\n\tYou Won The Game')
        break
print('true value is : ',ran)
        
    
    
