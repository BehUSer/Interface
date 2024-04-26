from time import sleep
from random import randint
print('Hoje é um belo dia para passear não acha?')
sleep(3)
print('Você pede um uber até uma loja de alugueis de carro')
sleep(2)
print('...')
sleep(2)
print('...')
sleep(2)
print('Você chega na loja')
sleep(2)
print('Hoje as opções de carro pra alugar são...')
sleep(1)
print("""
1- Toyota Supra MK4
2- Porsche GT3 RS
3- Ford/Shelby Mustang""")
esc = int(input('Escolha um carro digitando seu respectivo numero; '))
if esc == 1:
    print('Você escolheu o Toyota Supra MK4, um classico JDM')
    sleep(2)
    print('Você vai para uma rodovia testar essa delicinha de carro')
    sleep(2)
    print('Um carro colou ao seu lado bozinando para começar um racha!')
    sleep(2)
    print('Vôce todo empolgado começa a acelerar')
    MK4 = randint(100, 280)
    if MK4 <= 120:
        print('Vocês correm por varios Km...')
        sleep(2)
        print('Você na emoção do momento acaba não percebendo um rada de velocidade logo a frente, mas para sua sorte você estava dentro da velocidade permitida')
    else:
        print('Vocês correm por varios Km...')
        sleep(2)
        print('Você no calor do momento acaba nem percebendo o radar de velocidade logo a frente...')
        sleep(2)
        print('E acaba passando do limite de velocidade permitido na rodovia')
        multa =  (MK4 - 120) * 7
        sleep(2)
        print(f'No dia seguinte você recebe uma carta com uma multa de velocidade R${multa} por passar no radar de velocidade de {MK4}Km/h')
elif esc == 2:
    print('Você escolheu o Porsche GT3 RS, o Esportivo Alemão mais rapido de sua marca!.')
    sleep(2)
    print('Você vai para uma rodovia com essa belezinha .')
    sleep(2)
    print('Um carro cola ao seu lado e buzina pedindo um racha.')
    sleep(3)
    print('Você todo empolgado começa a acelerar e sorrir')
    RS = randint(100, 340)
    if RS <= 120:
        print('Vocês correm por varios Km...')
        sleep(2)
        print('Você na emoção do momento acaba nem percebendo o radar de velocidade logo a frente, mas sua sorte você estava dentro da velocidade permitida')

    else:
        print('Vocês correm por varios Km...')
        sleep(2)
        print('Você no calor do momento acaba nem percebendo o radar de velocidade logo a frente...')
        sleep(2)
        print('E acaba passando o limite de velocidade permtido na rodovia.')
        multa = (RS - 120) * 7
        sleep(2)
        print(f'No dia seguinte você recebe uma carta com uma multa de velocidade de R${multa} por passar no radar com a velocidade de {RS}Km/h')
elif esc == 3:
    print('Você escolheu o Ford/Shelby Mustang, um MuscleCar americano com um torque gigantesco e uma aceleração magnifica')
    sleep(2)
    print('Você vai para uma rodovia testar esse monstro!.')
    sleep(2)
    print('Um carro cola ao seu lado e  buzina para iniciar uma corrida')
    sleep(3)
    print('Você sente a emoção ao acelerar')
    Mustang = randint (100, 350)
    if Mustang <= 120:
        print('Vocês correm por varios Km...')
        sleep(2)
        print('Você na emoção do momento acaba nem percebendo o radar de velocidade logo a frente, mas para sua sorte você estava dentro da velocidade permitida')
    else:
         print('Vocês correm por varios Km...')
         sleep(2)
         print('Você no calor do momemnto acaba nem percebendo o radar de velocidade a frente...')
         sleep(2)
         print('E acaba passando o limite de velocidade permitido na rodovia')
         multa = (Mustang - 120) * 7
         sleep(2)
         print(f'no dia seguinte você recebe uma carta com uma multa de velocidade de R${multa} por passar no radar com a velocidade {Mustang}Km?h')
