import time
import menus

def recebe_palavra(palavra):
  palavra.extend(input("Informe uma palavra: "))
  print("Carregando...")
  time.sleep(4)


def recebe_vpalavra(palavra, vpalavra):
  for i in range(0,len(palavra)):
    vpalavra.append('-')  


def verifica_palavra(i,tentativa, palavra, vpalavra):
   if (tentativa in palavra[i]):
     vpalavra[i] = tentativa 


def ganhou(t,vpalavra, palavra):
  if (vpalavra == palavra):
    print("\033c")
    menus.menu_forca()
    print(vpalavra)
    print("Parabéns! Você acertou a palavra, errando", t ,"vezes.\n Voltando para o menu...")
    time.sleep(4)
   

def perdeu(t, jogo):
  if(t == jogo):
   print("\033c") 
   menus.menu_forca()
   print("¯\_(ツ)_/¯ Você perdeu ¯\_(ツ)_/¯ \n Voltando para o menu...")
   time.sleep(4)