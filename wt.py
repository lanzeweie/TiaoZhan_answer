#text放入 cookie ，一键格式化
import json

text = '_cliid=H8x4R7MekezHZPvx; scope=snsapi_base; faiOpenId=oosnVwoBokZk3QoPMuJEMc465j3I; hdOpenIdSign_19276789=bbb1c9cd9ba26e1b7430d6f58986ad13; t_wx01d290431209367c=owRlkwiIFP9OI2tyn2QezlByRfRs; oid_19276789_205=oosnVwoBokZk3QoPMuJEMc465j3I; visitorA=0.43566014338813885; oid_19276789_204=oosnVwoBokZk3QoPMuJEMc465j3I; _AID=19276789; oid_19276789_207=oosnVwoBokZk3QoPMuJEMc465j3I'

# Split the string into a list of key-value pairs
pairs = text.strip().split('; ')

# Create a dictionary to store the cookies
cookies = {}

# Loop through each key-value pair and add it to the dictionary
for i, pair in enumerate(pairs):
    name, value = pair.split('=')
    cookies[f'cook{i+1}'] = [{'name': name.strip(), 'value': value.strip()}]

# Convert the dictionary to JSON format and print it
print(json.dumps(cookies, indent=4))
