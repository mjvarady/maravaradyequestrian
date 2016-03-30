import webapp2
import os
import logging
import jinja2

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class AllTheHandlers(webapp2.RequestHandler):

    def get(self):
      path = self.request.path
      logging.info("attempting")
          
      try:    

        template = JINJA_ENVIRONMENT.get_template('templates%s' % self.request.path)
        self.response.write(template.render({"current": path}))
      
        logging.info("complete") 
      except:      
        home_template = JINJA_ENVIRONMENT.get_template('templates/homepage.html')
        self.response.write(home_template.render({"current":path}))

        logging.info("I think its complete...")
 
class QuizHandler(webapp2.RequestHandler):


    def get(self):
        path = self.request.path
        logging.info("GET")
        template = JINJA_ENVIRONMENT.get_template('templates/quiz.html')
        self.response.write(template.render({"msg": "Answers are case sensitive (proper names are capitalized)","current": path}))

    def post(self):
        path = self.request.path
        logging.info("POST")
        template = JINJA_ENVIRONMENT.get_template('templates/quiz.html')
        finish_template = JINJA_ENVIRONMENT.get_template('templates/gallery.html')
        q1 = self.request.get("q1")
        q2 = self.request.get("q2")
        q3 = self.request.get("q3")
        q4 = self.request.get("q4")
        q5 = self.request.get("q5")
        q6 = self.request.get("q6")
        q7 = self.request.get("q7")
        q8 = self.request.get("q8")
        q9 = self.request.get("q9")
        q10 = self.request.get("q10")
        if q1 == "seven" and q2 == "Desi" and q3 == "Windermere Equestrian Center" and q4 == "Cassie" and q5 == "Points Secretary" and q6 == "tan" and q7 == "helmet" and q8 == "Dover Saddlery" and q9 == "hunter/jumper" and q10 == "Misty":
            self.response.write(finish_template.render({"current": path}))
        else:
            self.response.write(template.render({"msg": "Sorry, Try Again (Click 'Need Help' for the answer)", "current":path}))              

app = webapp2.WSGIApplication([
    ('/', AllTheHandlers),
    ('/team.html', AllTheHandlers),
    ('/home.html', AllTheHandlers),
    ('/why.html', AllTheHandlers),
    ('/began.html', AllTheHandlers),
    ('/quiz.html', QuizHandler),
    ('/homepage.html', AllTheHandlers),

], debug=True)
