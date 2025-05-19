import json
import urllib.parse

def load_data():
    with open("q-vercel-python.json", "r") as f:
        return json.load(f)

def handler(request):
    query = urllib.parse.parse_qs(request["query"])
    names = query.get("name", [])
    data = load_data()

    result = {"marks": []}
    for name in names:
        for entry in data:
            if entry["name"] == name:
                result["marks"].append(entry["marks"])
                break

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(result)
    }
