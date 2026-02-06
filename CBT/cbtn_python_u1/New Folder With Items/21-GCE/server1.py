import cherrypy

class HelloWorld(object):
    def index(self):
        return "Hello World!"
    index.exposed = True

    def pagex(self):
        return "This is the pagex route."
    pagex.exposed = True

cherrypy.server.socket_host = '0.0.0.0'
cherrypy.quickstart(HelloWorld())