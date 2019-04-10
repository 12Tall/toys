from wsgiref.simple_server import make_server

from wsgi_app import application

httpd = make_server("",8000,application)
print("server started at http://127.0.0.1:8000")
httpd.serve_forever()

