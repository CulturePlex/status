import jinja2
import os
import webapp2

from google.appengine.api import users
from google.appengine.api import urlfetch

from settings import DEBUG, MACHINES
from utils import render_to_response


class MainPage(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        final_status = True
        services = []
        for machine_key, machine_value in MACHINES.items():
            machine_services = machine_value["services"]
            for service in machine_services:
                address = service["address"]
                status_code = 500
                try:
                    status_code = urlfetch.fetch(address).status_code
                except:
                    status_code = -1
                final_status = final_status and status_code == 200
                service["status"] = status_code
                services.append(service)
        render_to_response(self, 'index.html', {
            "services": services,
            "final_status": final_status,
        })


class UpdatePage(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        if user:
            render_to_response(self, 'index.html', {
                "user_name": user.nickname(),
            })
            # self.response.headers['Content-Type'] = 'text/html'
        else:
            self.redirect(users.create_login_url(self.request.uri))

app = webapp2.WSGIApplication([
    ('/update', UpdatePage),
    ('/', MainPage),
], debug=DEBUG)
