import json

data = {
    "User": {
        "Username": "David",
        "Password": "aBC",
        "Accounts": [
            {
                "Type": "Saving account",
                "Interest rate": 0.99,
                "Balance": 200,
            },
            {
                "Type": "Saving account",
                "Interest rate": 4.99,
                "Balance": 5000,
            }
        ],
        "Address": "2 Birmingham Street"
    }
}

with open("David.json", "w") as f:
    json.dump(data, f, indent=4)