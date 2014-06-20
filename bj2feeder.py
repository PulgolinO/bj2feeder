#Importa as bibliotecas necessarias
import feedparser, urllib2, os

#-----------------------------------#
#------CONFIGURACOES DO USUARIO-----#
#-----------------------------------#

#Define o diretório que quer salvar os arquivos
os.chdir( '/home/nome_do_usuario' )
#Ex: os.chdir( '/home/fulano/downloads' )
#Tenha certeza que tem direito para escrever no diretório

#Define os releases que deverão ser baixados
#Não se esqueça de colocar o nome de cada release separado por vígula e dentro de aspas duplas
RELEASES = [ "Release1|Release2|Release3" ]
#Ex: RELEASES = [ "Game of Thrones", "Spiderman", "Da Vinci" ]

#Aqui é preciso definir os cookies necessários para acessar o site
PASS = "Sua_Passkey_do_BJ2" #Coloque aqui sua pass do cookie. Não se esqueça de colocar entre aspas.
#Ex: PASS = "abcdefg123456789"
UID = "Sua_UID_do_BJ2" #Coloque aqui seu UID do BJ2. Não se esqueça de colocar entre aspas.
#Ex: UID = "123456789"

#------------------------------------#
#----NAO EDITE NADA A PARTIR DAQUI---#
#------------------------------------#

#Define a URL do Tracker que será acessado pelo feedparser
#Utilize o método "feedparser.parse" sempre que precisar acessar um feed
bjurl = 'http://bj2.me/rss.php'
bjurl = feedparser.parse( bjurl )

#Verifica se algum release definido satisfaz algum download
print('Procurando por torrents para baixar...\n')
for rel in range( len(RELEASES) ):
        #Percorre a lista de feeds e os mostra um a um
        for max_feeds in range( 20 ):
                #percorre os feeds e mostra apenas os que tem alguma palavra definida no
                title = bjurl.entries[ max_feeds ].title
                link = bjurl.entries[ max_feeds ].link
                link = link.replace( 'detalhes', 'download' )
                if re.search( RELEASES[ rel ], title, re.I ):
                        print( 'Baixando Torrent: ' + title )
                        print( 'Link: ' + link )
                        os.system( "wget -q --header \"Cookie: pass=" + str( PASS ) + ";uid=" + str( UID ) + "\" -O \"" + title + ".torrent\" " + link )
                        print( 'Download concluido.\n' )
print( 'Script finalizado com sucesso!' )
