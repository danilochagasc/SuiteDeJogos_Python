import random
import time

def sorteia_numero():
  sorteado = random.randint(0,100)
  return sorteado


def ganhou():
    print("Parabéns, você acertou o número sorteado.\n Voltando para o menu...")
    time.sleep(4)


def ganhou_final(n, numero):
  if(n == numero):
    return 1
  else:
    return 0


def perdeu():
  print("¯\_(ツ)_/¯ Você perdeu ¯\_(ツ)_/¯ \n Voltando para o menu...")
  time.sleep(4)


def perdeu_final(n, numero, t):
  if (t == 7 and n != numero):
    return 1
  else:
    return 0


def verifica_numero(n, numero):
  if (n>=0 and n<=100): 
    if (n == numero):
      ganhou()
    elif (n < numero):
      print("O número procurado é maior que o informado.\n")
    else:
      print("O número procurado é menor que o informado.\n")
  else:
    print("Número inválido. Informe novamente outro valor.\n")