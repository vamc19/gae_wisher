#!/usr/bin/python

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

########################################################################
class MainHandler(webapp.RequestHandler):

    def get(self):
        self.response.out.write(template.render("index.html", {}))
        
application = webapp.WSGIApplication([('/', MainHandler)], debug=True)

def main():
    run_wsgi_app(application)
    
if __name__ == "__main__":
    main()
     
