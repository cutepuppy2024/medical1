# url 라이브러리

from urllib import request

# urlopen()gkatn
target = request.urlopen("https://www.google.com")
output = target.read()

print(type(output))
# print(output)




