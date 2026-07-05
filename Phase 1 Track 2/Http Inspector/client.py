import http.client

host = "jsonplaceholder.typicode.com"
conn = http.client.HTTPConnection(host)

# headers = {"Host": "jsonplaceholder.typicode.com"}

# body_data = '{ "userId": 5, "id": 20, "title": "Testing", "body": "I am testing"}'

# conn.request("POST", "/posts", body=body_data, headers=headers)

conn.request("GET", "/posts/20", headers={"Host": host})

response = conn.getresponse()
print(response.status, response.reason)
print(response.read().decode("utf-8"))
# status = response.status
# data = response.read().decode("utf-8")
# print(
#     "headers: ",
#     response.headers,
#     "version: ",
#     response.version,
#     "message: ",
#     response.msg,
# )
# print("status", status)
# print("data:", data)


conn.close()
