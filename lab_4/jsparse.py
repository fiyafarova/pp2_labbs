import json

with open("sample-file.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("================================================================================")
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<5}")
print("-------------------------------------------------- --------------------  ------  ------" )

for interface in data.get("imdata", []):  
    attributes = interface.get("l1PhysIf", {}).get("attributes", {})
    
    dn = attributes.get("dn", "")
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "inherit")
    mtu = attributes.get("mtu", "9150")

    print(f"{dn:<50} {description:<20} {speed:<7} {mtu:<5}")