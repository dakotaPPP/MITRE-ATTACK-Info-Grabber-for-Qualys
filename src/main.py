from ExportToEXCEL import saveCSVData
from MitreMatrixUpdate import getTactics
from QualysAPIRequest import getTechniqueCounts
import json
from datetime import datetime
from os import path, makedirs

if not path.exists("logs"):
    makedirs("logs")
    if not path.exists("logs/CSVs"):
        makedirs("logs/CSVs")

if not path.exists("config"):
    makedirs("config")
    f = open("config/config.json", "w")
    f.write("{\"username\":\"API_USERNAME\", \"password\":\"API_PASSWORD\", \"base_url\":\"https://BASE_URL\"}")
    f.close()
    raise RuntimeError("Please update the default config/config.json file!")

#I don't like that I've had to hardcode this but it helps prevent rate limiting
mitreTacticsInVMDR = ["Initial Access", "Execution", "Persistence", "Privilege Escalation", "Defense Evasion", "Credential Access", "Lateral Movement", "Collection", "Impact"]
data = []
for tactic in getTactics():
    if tactic["name"] in mitreTacticsInVMDR:
        data.append({"tactic":tactic["name"], "techniques":getTechniqueCounts(tactic["id"])})
        print(data[-1])

now = datetime.now()
formatted_now = now.strftime("%Y-%m-%dT%H-%M-%S")

f = open("logs/data_log.txt", "a")
f.write(f"\n\nTIMEDATE: {formatted_now}\n")
f.write(json.dumps(data))
f.close()

filename = f"logs/CSVs/tactic_technique_counts_{formatted_now}.csv"
saveCSVData(data, filename)