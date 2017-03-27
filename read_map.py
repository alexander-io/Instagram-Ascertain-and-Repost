# content
import time

with open("post_map", "r") as post_map:
    content = post_map.readlines()

print(content)


for x in content:
    print(x)
    time.sleep(.5)
