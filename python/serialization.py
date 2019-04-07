import pickle
import json
dic = dict(name="12tall",age=12)

print(pickle.dumps(dic))
print(json.dumps(dic))
jsn = json.dumps(dic)
# parse a json string
print(json.loads(jsn))
# instance can not be serialiazed directly 
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143192607210600a668b5112e4a979dd20e4661cc9c97000
