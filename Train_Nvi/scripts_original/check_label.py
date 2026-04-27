import yaml

yaml_path = "/Users/chenzishu/Documents/Project/CY/Data_Set/Yolo/data.yaml"

with open(yaml_path, "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

names = data["names"]
nc = data["nc"]

print("nc =", nc)
print("number of names =", len(names))

if nc != len(names):
    print("ERROR: nc does not match names length")
else:
    print("OK")