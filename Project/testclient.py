import http.client
import pprint

conn = http.client.HTTPConnection("localhost", 7050)
conn.request("GET", "index.html")
r1 = conn.getresponse()

# headers = r1.getheaders()
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint("Headers: {}".format(headers))

print(r1.status, r1.reason)
data1 = r1.read()
print(data1)

