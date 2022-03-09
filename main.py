import menus
import acerte_o_numero
import forca
menu = 0

while (menu != 9):
  print ("\033c")  
  menus.menu_suite2()
  menu = int(input())
  
  if (menu == 1):
    print ("\033c")
    menus.menu_suite1()
    menus.menu_acerte_num()
    sorteado = acerte_o_numero.sorteia_numero()
    t = 1
    ganhou = perdeu = 0
    
    while (t <= 7):
      n = int(input("Informe um número: "))
      print("Tentativas: ", t)
      
      ganhou = acerte_o_numero.ganhou_final(n, sorteado)
      perdeu = acerte_o_numero.perdeu_final(n, sorteado, t)
      acerte_o_numero.verifica_numero(n, sorteado) 

      if (ganhou == 1):
        t = 8 
      if (perdeu == 1):
        acerte_o_numero.perdeu()
      
      t += 1
  elif (menu == 2):
    print("calmai")
  elif (menu == 3):
    print("ainda nao")
  elif (menu == 4):
    print("\033c")
    menus.menu_forca()
    
    t = 0
    palavra = []
    vpalavra = []
    jogo = int(input("Informe a quantidade de erros possíveis: "))
    forca.recebe_palavra(palavra)
    forca.recebe_vpalavra(palavra, vpalavra)
    while (t < jogo+1):
      print("\033c")
      menus.menu_forca()
      print(vpalavra)
      print("Erros: ", t)
      tentativa = input("Informe uma letra: ")
      for i in range(0,len(palavra)):
        forca.verifica_palavra(i,tentativa, palavra,vpalavra)
      if(tentativa in palavra):
        t -=1 
      print(vpalavra)
      t += 1  
      if (vpalavra == palavra):
       forca.ganhou(t,vpalavra, palavra)
       break
      elif (t == jogo):
        forca.perdeu(t, jogo)
        break