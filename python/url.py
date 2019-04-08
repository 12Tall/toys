from urllib import request
# urlopen can transfer param in the seccond position 
# like: request.urlopen(url,data) -->POST
# proxyHandler to set proxy
with request.urlopen('https://apis.map.qq.com/ws/place/v1/search') as f:
    # get response
    data = f.read()
    # statud
    print("status:",f.status,f.reason)
    # get headers
    for k,v in f.getheaders():
        print("%s:%s"%(k,v))
    # print response data
    print("data:",data.decode("utf-8"))

# emulate a browser
# create a request instance
req = request.Request('http://www.douban.com/')
# add headers
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# then do the same thing as uo
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))


