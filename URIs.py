import requests, banners, sys
import cores as c, os
from pystyle import Colorate, Colors
try:
 def URIs():
  urll=input(f'\n[ {c.yellow}i{c.white} ] Atenção, não coleque "/" (barra) no final dos links, exemplo ↓\n\n[{c.bgreen}Correto{c.white}: https://www.google.com]\n[{c.bred}Incorreto{c.white}: https://www.google.com/]\n\nDigite seu alvo (URL): ')
  url=urll.replace(" ", "")
  os.system('clear')
  print(Colorate.Vertical(Colors.yellow_to_red, banners.banner1))
  print(f'\n[ {Colorate.Vertical(Colors.red_to_purple, "X")} ] Alvo: {url}\n')
  qnut=0
  if url[-1:]=='/':
    print(f'{c.red}Não foi possível se conectar ao Alvo !\nPossíveis causas ↓\n• Existe uma / no final da URL\n• A URL não foi escrita corretamente\n• O site está offline')
    sys.exit()
  try:
   full_url0=url+'/wp-content'
   response = requests.get(full_url0)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url0} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /wp-content não foi encontrada...\n')
   full_url1=url+'/admin'
   response = requests.get(full_url1)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url1} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /admin não foi encontrada...\n')
   full_url2=url+'/wp-content/uploads'
   response = requests.get(full_url2)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url2} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /wp-content/uploads não foi encontrada...\n')
   full_url3=url+'/wp-content/assets'
   response = requests.get(full_url3)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url3} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /wp-content/assets não foi encontrada...\n')
   full_url3_4=url+'/wp-content/plugins'
   response = requests.get(full_url3_4)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url3_4} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /wp-content/plugins não foi encontrada...\n')
   full_url5=url+"/login"
   response = requests.get(full_url5)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url5} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /login não foi encontrada...\n')
   full_url6=url+"/wp-login.php"
   response = requests.get(full_url6)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url6} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /wp-login.php não foi encontrada...\n')
   full_url7=url+"/wp-admin"
   response = requests.get(full_url7)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url7} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /wp-admin não foi encontrada...\n')
   full_url8=url+"/robots.txt"
   response = requests.get(full_url8)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url8} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /robots.txt não foi encontrada...\n')
   full_url9=url+"/sitemap.xml"
   response = requests.get(full_url9)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url9} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /sitemap.xml não foi encontrada...\n')
   full_url10=url+"/passwords"
   response = requests.get(full_url10)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url10} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /passwords não foi encontrada...\n')
   full_url11=url+"/.mysql_history"
   response = requests.get(full_url11)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url11} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /.mysql_history não foi encontrada...\n')
   full_url12=url+'/search'
   response = requests.get(full_url12)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url12} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /search não foi encontrada...\n')
   full_url13=url+'/index.html'
   response = requests.get(full_url13)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url13} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /index.html não foi encontrada...\n')
   full_url14=url+'/shell'
   response = requests.get(full_url14)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url14} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /shell não foi encontrada...\n')
   full_url15=url+'/assets'
   response = requests.get(full_url15)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url15} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /assets não foi encontrada...\n')
   full_url16=url+'/images'
   response = requests.get(full_url16)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url16} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /images não foi encontrada...\n')
   full_url17=url+'/css'
   response = requests.get(full_url17)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url17} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /css não foi encontrada...\n')
   full_url18=url+'/js'
   response = requests.get(full_url18)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url18} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /js não foi encontrada...\n')
   full_url19=url+'/wp-content/mysql.sql'
   response = requests.get(full_url19)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url19} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /wp-content/mysql.sql não foi encontrada...\n')
   full_url20=url+'/wp-includes'
   response = requests.get(full_url20)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url20} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /wp-includes não foi encontrada...\n')
   full_url21=url+'/img'
   response = requests.get(full_url21)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url21} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /img não foi encontrada...\n')
   full_url22=url+'/fonts'
   response = requests.get(full_url22)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url22} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /fonts não foi encontrada...\n')
   full_url23=url+'/license.txt'
   response = requests.get(full_url23)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url23} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /license.txt não foi encontrada...\n')
   full_url24=url+'/xmlrpc.php'
   response = requests.get(full_url24)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url24} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /xmlrpc.php não foi encontrada...\n')
   full_url25=url+'/wp-load.php'
   response = requests.get(full_url25)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url25} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /wp-load.php não foi encontrada...\n')
   full_url26=url+'/wp-blog-header.php'
   response = requests.get(full_url26)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url26} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /wp-blog-header.php não foi encontrada...\n')
   full_url27=url+'/wp-trackback.php'
   response = requests.get(full_url27)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url27} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /wp-trackback.php não foi encontrada...\n')
   full_url28=url+'/wp-mail.php'
   response = requests.get(full_url28)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url28} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /wp-mail.php não foi encontrada...\n')
   full_url29=url+'/wp-links-opml.php'
   response = requests.get(full_url29)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url29} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /wp-links-opml.php não foi encontrada...\n')
   full_url30=url+'/vendor'
   response = requests.get(full_url30)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url30} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /vendor não foi encontrada...\n')
   full_url31=url+'/wp-cron.php'
   response = requests.get(full_url31)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url31} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /wp-cron.php não foi encontrada...\n')
   full_url32=url+'/wp-comments-post.php'
   response = requests.get(full_url32)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url32} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /wp-comments-post.php não foi encontrada...\n')
   full_url33=url+'/wp-activate.php'
   response = requests.get(full_url33)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url33} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /wp-activate.php não foi encontrada...\n')
   full_url34=url+'/wp-settings.php'
   response = requests.get(full_url34)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url34} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /wp-settings.php não foi encontrada...\n')
   full_url35=url+'/wp-signup.php'
   response = requests.get(full_url35)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url35} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /wp-signup.php não foi encontrada...\n')
   full_url36=url+'/wp-config-sample.php'
   response = requests.get(full_url36)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url36} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /wp-config-sample.php não foi encontrada...\n')
   full_url37=url+'/.htaccess'
   response = requests.get(full_url37)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url37} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /.htaccess não foi encontrada...\n')
   full_url38=url+'/wp-config.php'
   response = requests.get(full_url38)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url38} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /wp-config.php não foi encontrada...\n')
   full_url39=url+'/.git'
   response = requests.get(full_url39)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url39} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /.git não foi encontrada...\n')
   full_url40=url+'/web.config'
   response = requests.get(full_url40)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url40} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /web.config não foi encontrada...\n')
   full_url41=url+'/wp-register.php'
   response = requests.get(full_url41)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url41} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /wp-register.php não foi encontrada...\n')
   full_url42=url+'/uploads'
   response = requests.get(full_url42)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url42} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /uploads não foi encontrada...\n')
   full_url43=url+'/templates'
   response = requests.get(full_url43)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url43} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /templates não foi encontrada...\n')
   full_url44=url+'/app'
   response = requests.get(full_url44)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url44} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /app não foi encontrada...\n')
   full_url45=url+'/cgi-bin'
   response = requests.get(full_url45)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url45} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /cgi-bin não foi encontrada...\n')
   full_url46=url+'/system'
   response = requests.get(full_url46)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url46} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /system não foi encontrada...\n')
   full_url47=url+'/themes'
   response = requests.get(full_url47)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url47} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /themes não foi encontrada...\n')
   full_url48=url+'/composer.json'
   response = requests.get(full_url48)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url48} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /composer.json não foi encontrada...\n')
   full_url49=url+'/cache'
   response = requests.get(full_url49)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url49} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /cache não foi encontrada...\n')
   full_url50=url+'/includes'
   response = requests.get(full_url50)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url50} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /includes não foi encontrada...\n')
   full_url51=url+'/README.md'
   response = requests.get(full_url51)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url51} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /README.md não foi encontrada...\n')
   full_url52=url+'/static'
   response = requests.get(full_url52)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url52} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /static não foi encontrada...\n')
   full_url53=url+'/mix-manifest.json'
   response = requests.get(full_url53)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url53} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /mix-manifest.json não foi encontrada...\n')
   full_url54=url+'/files'
   response = requests.get(full_url54)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url54} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /files não foi encontrada...\n')
   full_url55=url+'/plugins'
   response = requests.get(full_url55)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url55} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /plugins não foi encontrada...\n')
   full_url56=url+'/.DS_Store'
   response = requests.get(full_url56)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url56} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /.DS_Store não foi encontrada...\n')
   full_url57=url+'/media'
   response = requests.get(full_url57)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url57} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /media não foi encontrada...\n')
   full_url58=url+'/application'
   response = requests.get(full_url58)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url58} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /application não foi encontrada...\n')
   full_url59=url+'/manifest.json'
   response = requests.get(full_url59)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url59} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /manifest.json não foi encontrada...\n')
   full_url60=url+'/config.php'
   response = requests.get(full_url60)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url60} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /config.php não foi encontrada...\n')
   full_url62=url+'/.well-known'
   response = requests.get(full_url62)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url62} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /.well-known não foi encontrada...\n')
   full_url63=url+'/.composer.lock'
   response = requests.get(full_url63)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url63} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /composer.lock não foi encontrada...\n')
   full_url64=url+'/upload'
   response = requests.get(full_url64)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url64} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /upload não foi encontrada...\n')
   full_url65=url+'/scripts'
   response = requests.get(full_url65)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url65} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /scripts não foi encontrada...\n')
   full_url67=url+'/public'
   response = requests.get(full_url67)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url67} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /public não foi encontrada...\n')
   full_url68=url+'/config'
   response = requests.get(full_url68)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url68} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /config não foi encontrada...\n')
   full_url69=url+'/lib'
   response = requests.get(full_url69)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url69} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /lib não foi encontrada...\n')
   full_url70=url+'/pdf'
   response = requests.get(full_url70)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url70} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /pdf não foi encontrada...\n')
   full_url71=url+'/data'
   response = requests.get(full_url71)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url71} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /data não foi encontrada...\n')
   full_url72=url+'/test'
   response = requests.get(full_url72)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url72} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /test não foi encontrada...\n')
   full_url73=url+'/modules'
   response = requests.get(full_url73)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url73} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /modules não foi encontrada...\n')
   full_url74=url+'/storage'
   response = requests.get(full_url74)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url74} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /storage não foi encontrada...\n')
   full_url75=url+'/.idea'
   response = requests.get(full_url75)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url75} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /.idea não foi encontrada...\n')
   full_url76=url+'/news'
   response = requests.get(full_url76)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url76} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /news não foi encontrada...\n')
   full_url77=url+'/blog'
   response = requests.get(full_url77)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url77} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /blog não foi encontrada...\n')
   full_url78=url+'/error_log'
   response = requests.get(full_url78)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url78} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /error_log não foi encontrada...\n')
   full_url79=url+'/resources'
   response = requests.get(full_url79)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url79} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /resources não foi encontrada...\n')
   full_url80=url+'/.gitignore'
   response = requests.get(full_url80)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url80} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /.gitignore não foi encontrada...\n')
   full_url81=url+'/docs'
   response = requests.get(full_url81)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url81} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /docs não foi encontrada...\n')
   full_url82=url+'/video'
   response = requests.get(full_url82)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url82} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /video não foi encontrada...\n')
   full_url83=url+'/api'
   response = requests.get(full_url83)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url83} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /api não foi encontrada...\n')
   full_url84=url+'/catalog'
   response = requests.get(full_url84)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url84} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /catalog não foi encontrada...\n')
   full_url85=url+'/_notes'
   response = requests.get(full_url85)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url85} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /_notes não foi encontrada...\n')
   full_url86=url+'/src'
   response = requests.get(full_url86)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url86} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /src não foi encontrada...\n')
   full_url87=url+'/library'
   response = requests.get(full_url87)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url87} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /library não foi encontrada...\n')
   full_url88=url+'/scss'
   response = requests.get(full_url88)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url88} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /scss não foi encontrada...\n')
   full_url89=url+'/BingSiteAuth.xml'
   response = requests.get(full_url89)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url89} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /BingSiteAuth.xml não foi encontrada...\n')
   full_url90=url+'/styles'
   response = requests.get(full_url90)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url90} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /styles não foi encontrada...\n')
   full_url91=url+'/videos'
   response = requests.get(full_url91)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url91} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /videos não foi encontrada...\n')
   full_url92=url+'/package.json'
   response = requests.get(full_url92)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url92} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /package.json não foi encontrada...\n')
   full_url93=url+'/inc'
   response = requests.get(full_url93)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url93} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /inc não foi encontrada...\n')
   full_url94=url+'/about'
   response = requests.get(full_url94)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url94} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /about não foi encontrada...\n')
   full_url95=url+'/ads.txt'
   response = requests.get(full_url95)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url95} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /ads.txt não foi encontrada...\n')
   full_url96=url+'/test.php'
   response = requests.get(full_url96)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url96} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /test.php não foi encontrada...\n')
   full_url97=url+'/install'
   response = requests.get(full_url97)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url97} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /install não foi encontrada...\n')
   full_url98=url+'/font'
   response = requests.get(full_url98)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url98} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /font não foi encontrada...\n')
   full_url99=url+'/bootstrap'
   response = requests.get(full_url99)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url99} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /bootstrap não foi encontrada...\n')
   full_url100=url+'/node_modules'
   response = requests.get(full_url100)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url100} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /node_modules não foi encontrada...\n')
   full_url101=url+'/browserconfig.xml'
   response = requests.get(full_url101)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url101} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /browserconfig.xml não foi encontrada...\n')
   full_url102=url+'/common'
   response = requests.get(full_url102)
   if response.status_code == 200 or response.status_code // 100 == 3:
         print(f'[ {c.green}!{c.white} ] {full_url102} - Encontrada\n')
         qnut=qnut+1
   else:
       print(f'[ ÷ ] Página /common não foi encontrada...\n')
   print(f'[{c.blue}&{c.white}] Escaneamento finalizado\n[{c.cyan}√{c.white}] Total de páginas encontradas: {qnut}\n\n{c.bwhite}[ENTER]{c.white} para voltar ao menu.')
   input('')
  except KeyboardInterrupt:
      print(f'\n[#] O programa foi interrompido.')
      sys.exit()
  except:
      print(f'{c.red}Não foi possível se conectar ao Alvo !\nPossíveis causas ↓\n• Existe uma / no final da URL\n• A URL não foi escrita corretamente\n• O site está offline')
      sys.exit()
except KeyboardInterrupt:
  print(f'\n[#] O programa foi interrompido.')
