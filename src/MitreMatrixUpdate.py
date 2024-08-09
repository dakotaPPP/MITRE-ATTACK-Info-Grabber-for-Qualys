import requests
from mitreattack.stix20 import MitreAttackData
from os import remove, rmdir, mkdir

def updateJson():
    response = requests.get(url="https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json")
    mkdir("temp")
    f = open('temp/enterprise-attack.json', 'w')
    f.write(response.text)
    f.close()

def getTactics():
    updateJson()
    mitre_attack_data = MitreAttackData("temp/enterprise-attack.json")
    output = []
    tactics = mitre_attack_data.get_tactics(remove_revoked_deprecated=True)
    for tactic in tactics:
        for reference in tactic["external_references"]:
            if reference["source_name"] == "mitre-attack":
                output.append({"id":reference["external_id"],"name":tactic["name"]})
    remove("temp/enterprise-attack.json")
    rmdir("temp")
    return output
