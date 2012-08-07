#!/usr/bin/python

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

########################################################################
class MainHandler(webapp.RequestHandler):

    def get(self, string):
        theme, name = string.split('/')
        indexFile = theme + ".html"
        if '_' in name:
            nameList = name.split('_')
            name = ""
            for i in xrange(len(nameList)):
                name = name + " " + nameList[i]
        self.response.out.write(template.render(indexFile, {"name" : name }))
        
application = webapp.WSGIApplication([('/(.*)', MainHandler)], debug=True)

def main():
    run_wsgi_app(application)
    
if __name__ == "__main__":
    main()
    