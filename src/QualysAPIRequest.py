import requests
import json
from requests.auth import HTTPBasicAuth
from time import sleep

def getTechniqueCounts(tacticID):
    with open("config/config.json") as config_file:
        config = json.load(config_file)
        username = config["username"]
        password = config["password"]
        BASE_URL = config["base_url"]

    if username == "API_USERNAME" or password == "API_PASSWORD" or BASE_URL == "https://BASE_URL":
        raise RuntimeError("Please update the default config/config.json file!")
    url = f'{BASE_URL}/portal-front/rest/assetview/1.0/assetvuln/pivotList?limit=200&offset=0&query=&groupByPivot=VM&havingQuery=(vulnerabilities.typeDetected:Confirmed and (vulnerabilities.severity:3 or vulnerabilities.severity:4 or vulnerabilities.severity:5) and vulnerabilities.nonRunningKernel:FALSE ) and (vulnerabilities.typeDetected: [Confirmed, Potential] and vulnerabilities.found: TRUE and vulnerabilities.disabled: FALSE and vulnerabilities.ignored: FALSE)&groupBy=vulnerabilities.vulnerability.mitre.attack.tactic.id:{tacticID}&invalidateCache=true'
    output = []

    # Sometimes qualys will give us a landing page saying "Please wait"
    # When this occurs just retry 3 times and if it still doesn't work then return
    retry_count = 3
    delay = 30

    for attempt in range(retry_count):
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        if response.status_code == 200:
            if("</html>" in response.text):
                print(f"Rate limited, retrying...")
                sleep(delay)
                delay *= 2
                continue

            data = response.json()
            if data["total"] == 0:
                return []
            
            for technique in data["data"]:
                output.append({"name":technique["vulnerabilities.vulnerability.mitre.attack.technique.name"],"count":technique["count"]})

            return output
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return []
    print("Retry limit reached")
    return []