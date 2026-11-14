#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler

# definisce l'handler HTTP per gestire le richieste del browser
class Handler(BaseHTTPRequestHandler):
    # Definisci cosa fare quando arriva una richiesta GET
    def do_GET(self):
        # PREPARA IL DOCUMENTO HTML DA INVIARE COME RISPOSTA AL BROWSER
        nome = 'Raffaele'
        html = "<html>"
        html += "<head></head>"
        html += "<body><h3>Ciao " + nome + "</h3></body>"
        html += "</html>"
        # Trasforma la stringa 'html' in una sequenza di byte
        html = html.encode('UTF-8')
        
        # INVIA LA TESTATA DEL DOCUMENTO HTTP 1.1
        self.send_response(200)     # --> OK         
        self.send_header('Content-type', 'text/html')
        self.send_header('Content-Length', str(len(html)))
        self.end_headers()          # fine head e aggiunge una riga vuota          
        
        # SCRIVI IL DOCUMENTO HTML / CONTENUTO DELLA RISPOSTA
        # wfile è l'oggetto simile a un file che si usa per scrivere 
        # la risposta HTTP e inviarla al client. E' il canale di output
        # utilizzato dal server per parlare al browser dell'utente
        self.wfile.write(html) 

# Avvia il server: ascolta sulla porta 8000 e gestisce le richieste con Handler
# Intercetta CTRL+C per interrompere il server
httpd = HTTPServer(('', 8000), Handler)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print('Server fermato')
except Exception as e:
    print ('Errore:', e)
finally:
    httpd.server_close()
