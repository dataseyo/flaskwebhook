import json
import requests

webhook_url = "http://127.0.0.1:5000/hook"


test_data = {
    "name" : "username",
    "data" : [
        {
            "station": "1",
            "val": "test val 1",
            "status": "offline"
        },

        {
            "station": "2",
            "val": "test val 2",
            "status": "online"
        },

        {
            "station": "3",
            "val": "test val 3",
            "status": "online"
        }
    ]
}

response = requests.post(webhook_url,
                        data=json.dumps(test_data),
                        headers={'Content-Type': 'application/json'},
                        )
