web_users = ["najma", "alex", "maggie", "taryn", "cecilia"]

new_users = ["alex", "najma", "rosario", "kelly", "ashley"]

for user in new_users:
    if user in web_users:
        print("This user name is already in use. Please choose a different user name.")
    else:
        print("This user name is available.")
        cities = {
    "barcelona": {
        "country": "Spain",
        "population": 1700000,
        "fact": "Barcelona is known for Gaudí architecture."
    },
    "mogadishu": {
        "country": "Somalia",
        "population": 2969320,
        "fact": "Mogadishu is the capital and largest city of Somalia."
    },
    "seattle": {
        "country": "United States",
        "population": 780995,
        "fact": "Seattle is home to the Seahawks, who won Super Bowl XLVIII."
    }
}

for city, info in cities.items():
    print("City:", city.title())
    print("Country:", info["country"])
    print("Population:", info["population"])
    print("Fact:", info["fact"])
    print()
