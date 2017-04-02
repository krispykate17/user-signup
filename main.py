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
import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return not email or EMAIL_RE.match(email)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        username_error = self.request.get("username_error")
        username_error = "<span class='error'>" + username_error + "</span>"

        password_error = self.request.get("password_error")
        password_error = "<span class='error'>" + password_error + "</span>"

        verify_error = self.request.get("verify_error")
        verify_error = "<span class='error'>" + verify_error + "</span>"

        email_error = self.request.get("email_error")
        email_error = "<span class='error'>" + email_error + "</span>"

        header = "<h1>Signup</h1>"
        username_label ="<label>Username </label>"
        username = "<input type='text' name='username' value='{0}'>"
        updated_username = self.request.get("new_username")

        password_label ="<label>Password </label>"
        password = "<input type='password' name='password'>"

        verify_label ="<label>Verify Password </label>"
        verify = "<input type='password' name='verify'>"

        email_label ="<label>Email (optional) </label>"
        email = "<input type='text' name='email' value='{1}'>"
        updated_email = self.request.get("new_email")

        submit = "<input type='submit'/>"

        form = ("<form action='/welcome' method='post'>" + header +
                    username_label + username + username_error + "<br>" +
                    password_label + password + password_error + "<br>" +
                    verify_label + verify + verify_error + "<br>" +
                    email_label + email + email_error + "<br>" +
                    submit + "</form>")

        form = form.format(updated_username, updated_email)

        page_header = """<!DOCTYPE html>
        <html>
        <head>
            <title>User Signup</title>
            <style type="text/css">
                .error {
                    color: red;
                }
            </style>
        </head>
        <body>
        """

        page_footer = """
        </body>
        </html>
        """

        content = page_header + form + page_footer

        self.response.write(content)

class Welcome(webapp2.RequestHandler):
    def post(self):
        new_username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        new_email = self.request.get("email")

        keep_username_email = "&new_username=" + new_username + "&new_email=" + new_email

        if not valid_username(new_username):
            self.redirect("/?username_error= Please enter a valid username" + keep_username_email)

        elif not valid_password(password):
            self.redirect("/?password_error=" + " Please enter a valid password" + keep_username_email)

        elif password != verify:
            self.redirect("/?verify_error=" + " Your passwords don't match" + keep_username_email)

        elif not valid_email(email):
            self.redirect("/?email_error=" + " Please enter a valid email" + keep_username_email)

        else:
            welcome = "<h1>Welcome, " + username + "!</h1>"
            self.response.write(welcome)

app = webapp2.WSGIApplication([
    ('/', MainHandler), ('/welcome', Welcome)
], debug=True)
