import os, re

lines = open("image_urls.txt").read().splitlines()

data_string = ''.join(lines)

#urls = re.findall(r'url:\s*"([^"]+)"', data_string)
#print (urls)

print ("OK!")

output = []

for url in lines:
    row = "\t\t\"{img %s}\"," % url
    output.append(row)

with open("formattedurls.txt", "w") as f:
    for line in output:
        f.write(f"{line}\n")

