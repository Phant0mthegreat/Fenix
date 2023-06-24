import URIs, os, cores as c, banners, sys, time, URIs2
from pystyle import Colorate, Colors
try:
 banners.carregando()
 print('      © Phant0m The Great\n\n')
 time.sleep(2)
 while True:
  os.system('clear')
  print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
  print(f'''
╔════════════════════════════════════════╗
║                                        ║
║       {Colorate.Vertical(Colors.yellow_to_red, '          FENIX')}                  ║
║                                        ║
║════════════════════════════════════════║
║                                        ║
║  [01] {c.blue}Escanear{c.white}    ║   [03] {c.blue}Criador{c.white}     ║
║                                        ║
║  [02] {c.blue}Informações{c.white} ║   [00] {c.blue}Sair{c.white}        ║
║                                        ║
╚════════════════════════════════════════╝''')
  ech=input(f'\nDigite sua escolha [{c.bblue}>{c.white}] ')
  os.system('clear')
  if ech=='01' or ech=='1':
    print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
    print(f'[ {c.yellow}?{c.white} ] Você deseja visualizar os diretórios/arquivos que não foram encontrados ? ({c.green}s{c.white}/{c.red}n{c.white})')
    sn=input(f'\n[{c.bblue}>{c.white}] ')
    if sn=='s' or sn=='S':
      os.system('clear')
      print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
      URIs.URIs()
    elif sn=='n' or sn=='N':
      os.system('clear')
      print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
      URIs2.URIs2()
      

  elif ech=='02' or ech=='2':
    print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
    print(f'\n[ {c.yellow}∆{c.white} ] O Fenex, é uma ferramenta de pentester, ele tem a capacidade de encontrar diretórios em sites, e páginas que podem haver alguma vulnerabilidade.\n\n[ {c.yellow}V{c.white} ] Versão: 2.0\n\n[ {c.yellow}×{c.white} ] Bugs: Caso tenho encontrado algum bug no Fenix, faça um Bug-Report entrando em contato com o criador.')
    print(f'\n{c.bwhite}[ENTER]{c.white} para voltar ao menu.')
    input()
  elif ech=='03' or ech=='3':
    print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
    print(f'\n[ © ] Criador: Phant0m The Great\n[ {c.bblue}D{c.white} ] {c.bblue}Discord{c.white}: phant0mthegreat\n[ ~ ] Mais informações em: https://www.phant0m007.repl.co/\n')
    print(f'\n{c.bwhite}[ENTER]{c.white} para voltar ao menu.')
    input('')
  elif ech=='00' or ech=='0':
    print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
    print('\nAté a próxima !')
    sys.exit()
except KeyboardInterrupt:
  print(f'\n[#] O programa foi interrompido.')
