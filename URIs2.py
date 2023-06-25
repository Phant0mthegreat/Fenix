import requests, banners, sys
import cores as c, os
from pystyle import Colorate, Colors
try:
 def URIs2():
  
  urlll=input(f'\n[ {c.yellow}i{c.white} ] Atenção, não coleque "/" (barra) no final dos links, exemplo ↓\n\n[{c.bgreen}Correto{c.white}: https://www.google.com]\n[{c.bred}Incorreto{c.white}: https://www.google.com/]\n\nDigite seu alvo (URL): ')
  urlll=urlll.replace(" ", "")
  os.system('clear')
  print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
  print(f'\n[ {Colorate.Vertical(Colors.red_to_purple, "X")} ] Alvo: {urlll}\n')
  
  qnut=0
  timeout = 5
  def nt():
   try:
        requests.get(urlll, timeout=timeout)
        return True
   except requests.exceptions.MissingSchema:
        return False
   except requests.exceptions.ConnectionError:
        return False
   except requests.exceptions.InvalidSchema:
        return False
   except requests.exceptions.InvalidURL:
        return False
  if not nt():
    print(f'{c.red}Não foi possível se conectar ao Alvo !\nPossíveis causas ↓\n• Existe uma / no final da URL\n• A URL não foi escrita corretamente\n• O site está offline')
    sys.exit()
  elif urlll[-1:]=='/':
    print(f'{c.red}Não foi possível se conectar ao Alvo !\nPossíveis causas ↓\n• Existe uma / no final da URL\n• A URL não foi escrita corretamente\n• O site está offline')
    sys.exit()

  uris = [
    "/wp-content",
    "/admin",
    "/wp-content/uploads",
    "/wp-content/assets",
    "/wp-content/plugins",
    "/login",
    "/wp-login.php",
    "/wp-admin",
    "/robots.txt",
    "/sitemap.xml",
    "/passwords",
    "/.mysql_history",
    "/search",
    "/index.html",
    "/shell",
    "/assets",
    "/images",
    "/css",
    "/js",
    "/wp-content/mysql.sql",
    "/wp-includes",
    "/img",
    "/fonts",
    "/xmlrpc.php",
    "/wp-load.php",
    "/wp-blog-header.php",
    "/wp-trackback.php",
    "/wp-mail.php",
    "/wp-links-opml.php",
    "/vendor",
    "/wp-cron.php",
    "/wp-comments-post.php",
    "/wp-activate.php",
    "/wp-settings.php",
    "/wp-signup.php",
    "/wp-config-sample.php",
    "/.htaccess",
    "/wp-config.php",
    "/.git",
    "/web.config",
    "/wp-register.php",
    "/uploads",
    "/templates",
    "/app",
    "/cgi-bin",
    "/system",
    "/themes",
    "/composer.json",
    "/cache",
    "/includes",
    "/README.md",
    "/static",
    "/mix-manifest.json",
    "/files",
    "/plugins"
    "/.DS_Store"
    "/media",
    "/application",
    "/manifest.json",
    "/config.php",
    "/.well-known",
    "/.composer.lock",
    "/upload",
    "/scripts",
    "/public",
    "/config",
    "/lib",
    "/pdf",
    "/data",
    "/test",
    "/modules",
    "/storage",
    "/.idea",
    "/news",
    "/blog",
    "/error_log",
    "/resources",
    "/.gitignore",
    "/docs",
    "/video",
    "/api",
    "/catalog",
    "/_notes",
    "/src",
    "/library",
    "/scss",
    "/BingSiteAuth.xml",
    "/styles",
    "/videos",
    "/package.json",
    "/inc",
    "/about",
    "/ads.txt",
    "/test.php",
    "/install",
    "/font",
    "/bootstrap",
    "/node_modules",
    "/browserconfig.xml",
    "/common" 
]
  for uri in uris:
    
    
    full_urll = urlll + uri

    response = requests.get(full_urll)
    if response.status_code == 200 or response.status_code // 100 == 3:
      print(f'[ {c.green}!{c.white} ] {full_urll} - Encontrada\n')
      qnut=qnut+1
    else:
      qnut=qnut
  print(f'[{c.blue}&{c.white}] Escaneamento finalizado\n[{c.cyan}√{c.white}] Total de páginas encontradas: {qnut}\n\n{c.bwhite}[ENTER]{c.white} para voltar ao menu.')
  input('')
except KeyboardInterrupt:
  print('\n[#] O programa foi interrompido.')
