import re

with open("elsass_index_speicher.txt", "r", encoding="utf-8") as f:
    index = f.readlines()

title = []
ort = []
combo = []
for line in index:
    v = re.sub(r"\t+.+\n", "", line)
    if not v == "":
        m = v[0].upper()
        v = m + v[1:]
        v = re.sub(r"\.+", "", v)
        v = re.sub(r"\s+$", "", v)
        ort.append(v)
    t = re.sub(r".+\t+", "", line)
    t = re.sub(r"\n", "", t)
    t = re.sub(r"^\d+\.\s*", "", t)
    t = re.sub(r"•*\s*\d+$", "", t)
    t = re.sub(r"[\.•·]", "", t)
    t = re.sub(r"\s+$", "", t)
    t = re.sub(r"\sst\s", " St. ", t)
    title.append(t)
    combo.append([t,v])
#print(combo)

output = "["
for i in title:
    output += "'" + i + "'" + ","
output += "]"
print(output)

dict_out = "{"
for i in combo:
    dict_out += "'" + i[0] + "': '" + i[1] + "',"
dict_out += "}"
#print(dict_out)