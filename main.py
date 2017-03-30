#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

def valid_username(username):
    return username

def valid_password(password):
    return password

def valid_email(email):
    return email

def build_page(username, email):
    username_label ="<label>Username</label>"
    username = "<input type='text' name='username'/>"

    password_label ="<label>Password</label>"
    password = "<input type='text' name='password'>"

    verify_label ="<label>Verify Password</label>"
    verify = "<input type='text' name='verify'>"

    email_label ="<label>Email (optional)</label>"
    email = "<input type='text' name='email'>"

    submit = "<input type='submit'/>"

    form = ("<form action='/welcome' method='post'>" + username_label + username + "<br>" +
                password_label + password + "<br>" + verify_label +
                verify + "<br>" + email_label + email + "<br>" +
                submit + "</form>")

    header = "<h1>Signup</h1>"
    return header + form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("", "")
        self.response.write(content)

class Welcome(webapp2.RequestHandler):
    def post(self):
        username = self.request.get("username")
        #rotation = int(self.request.get("rotation"))
        #encrypted_message = caesar.encrypt(message, rotation)
        #escaped_msg = cgi.escape(encrypted_message)
        #content = build_page() <---(Maybe keep for if user inputs something stupid?
        content = "<h1>Welcome, " + username + "!</h1>"
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler), ('/welcome', Welcome)
], debug=True)
