import random
from time import sleep
'''player1 = int(input('Digite um número de 1 a 20: '))
bot = random.randint(1, 20)
print('Eu escolho {}'.format(bot))
print('Parabéns, você venceu!' if player1 >= bot else 'Não foi dessa vez, tente numa próxima oportunidade!')
'''
#Glossário de cores
limpa = '\033[m'
red_bold = '\033[1;31m'
green = '\033[36m'
green_bold = '\033[1;36m'
sub = '\033[4m'
red_inv = '\033[7;31m'
yellow_inv = '\033[7;33m'
green_inv = '\033[7;32m'
blue_inv = '\033[7;34m'
roxo_inv = '\033[7;35m'
white_inv = '\033[7;30m'

repeat = 'S'

print('-=-'*9)
print('{}{} VAMOS JOGAR 21! {}{}'.format('='*5, red_bold, limpa, '='*5))
print('-=-'*9)
while repeat != 'N':
    card1 = str(input('{}Pegar uma carta?{} {}(S/N){}'.format(green, limpa, green_bold, limpa))).upper()
    if card1 == 'S':
        player1 = random.randint(0, 20)
        print('Sua carta vale {}{} pontos{}'. format(sub , player1, limpa))

        bot1 = random.randint(0, 20)

        print('-'*15)
        print('{}Player: {} pontos.{}'.format(yellow_inv, player1, limpa))
        print('{}Bot: {} pontos.{}'.format(blue_inv, bot1, limpa))
        print('-'*15)

        print('{}{}MAIS UMA VEZ{}{}'.format('='*5, red_bold, limpa, '='*5))
        card2 = str(input('{}Acha que precisa de mais uma carta?{} {}(S/N){}'.format(green, limpa, green_bold, limpa)).upper())

        if card2 == 'S':
            player2 = random.randint(0, 20)
            print('Sua segunda carta vale {}{} pontos.{}'.format(sub, player2, limpa))
        if card2 == 'N':
            player2 = 0
            print('Ok, você ficará então com os seus {}{} pontos.{}'.format(sub, player1, limpa))

        if 15 > bot1:
            if bot1 <= player1 + player2:
                bot2 = random.randint(0, 20)
                print('O Bot pegou uma carta de {}{} pontos.{}'.format(sub, bot2, limpa))
            if bot1 > player1 + player2:
                bot2 = 0
                print('O Bot optou por não pegar a segunda carta e ficará com os seus {}{} pontos.{}'.format(sub, bot1, limpa))
        if bot1 >= 15:
            if bot1 <= player1 + player2 and player1 + player2 < 21:
                bot2 = random.randint(0, 20)
                print('O Bot pegou uma carta de {}{} pontos.{}'.format(sub, bot2, limpa))
            if bot1 < player1 + player2 and player1 + player2 > 21:
                bot2 = 0
                print('O Bot optou por não pegar a segunda carta e ficará com os seus {}{} pontos.{}'.format(sub, bot1, limpa))
            if bot1 > player1 + player2 and bot1 <= 21:
                bot2 = 0
                print('O Bot optou por não pegar a segunda carta e ficará com os seus {}{} pontos.{}'.format(sub, bot1, limpa))

        print('-'*15)
        player = int(player1 + player2)
        bot = int(bot1 + bot2)
        print('{}Player: {} pontos.{}'.format(yellow_inv, player, limpa))
        print('{}Bot: {} pontos.{}'.format(blue_inv, bot, limpa))

        print('{}CALCULANDO QUEM VENCEU{}'.format(white_inv, limpa), end='')
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.')


        if player <= 21 and player > bot:
            print('{}Parabéns, você venceu!!! =D{}'.format(green_inv, limpa))
        else:
            if player > 21 and bot > 21:
                print('{}Ninguém venceu, você e o bot fizeram mais de 21 pontos e os dois perderam{}'.format(roxo_inv, limpa))
            if player > 21 and bot <= 21:
                print('{}Infelizmente você passou de 21 e você perdeu, vitória do robô!{}'.format(red_inv, limpa))
            if player <= 21 and bot > 21:
                print('{}PARABÉNS, o robô passou de 21 pontos e você foi o grande vencedor!{}'.format(green_inv,limpa))
            if player < 21 and player < bot and bot <= 21:
                print('{}Infelizmente o robô ganhou dessa vez!{}'.format(red_inv, limpa))
            if player == bot:
                print('{}EMPATOU!!!{}'.format(roxo_inv,limpa))

        print('='*50)

        repeat = str(input('{}Jogar novamente?{} {}(S/N):{} '.format(green, limpa, green_bold, limpa)).upper())
        if repeat == 'S':
            print('OK')
        else:
            print('Foi um prazer jogar com você, até logo!')

    if card1 == 'N':
        print('{}Ok então, não vamos jogar!{}'.format(white_inv, limpa))