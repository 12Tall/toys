# environ: an instance called httprequest in .NET which contains all request params
# start_response: function to response a httprequest
def application(environ,start_response):
    # response httpheaders
    # could be called only Once
    start_response("200 OK",[("Content-Type","text/html")])
    # return html or other content
    # saving string as bytes
    return [b"hello 12tall~"]


