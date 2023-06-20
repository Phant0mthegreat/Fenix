import URIs, os, cores as c, banners, sys

from pystyle import Colorate, Colors

try:

 while True:

  os.system('clear')

  print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))

  print(f'''

┎――――――――――――――――――――――――――――――――――――――――┒

|       {Colorate.Vertical(Colors.yellow_to_red, '          FENIX')}                  |

|――――――――――――――――――――――――――――――――――――――――|

| [01] {Colorate.Vertical(Colors.blue_to_purple, 'Escanear')}     │ [03] {Colorate.Vertical(Colors.blue_to_purple, 'Criador')}       |

| [02] {Colorate.Vertical(Colors.blue_to_purple, 'Informações')}  │ [00] {Colorate.Vertical(Colors.blue_to_purple, 'Sair')}          |

└――――――――――――――――――――――――――――――――――――――――┘''')

  ech=input(f'\nDigite sua escolha [{c.bblue}>{c.white}] ')

  os.system('clear')

  if ech=='01' or ech=='1':

    print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))

    URIs.URIs()

  elif ech=='02' or ech=='2':

    print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))

    print(f'\n[ {c.yellow}×{c.white} ] O Fenex, é uma ferramenta de penterster, ele tem a capacidade de encontrar diretórios em sites, e páginas que podem haver alguma vulnerabilidade.')

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
