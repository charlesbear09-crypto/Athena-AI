import json
import os


FILE = "truck_data.json"



def load_truck():

    if not os.path.exists(FILE):

        return {}

    with open(FILE, "r") as f:

        return json.load(f)



def save_truck(data):

    with open(FILE, "w") as f:

        json.dump(
            data,
            f,
            indent=4
        )



def add_mod(mod):

    truck = load_truck()

    truck["mods"].append(mod)

    save_truck(truck)



def add_maintenance(item):

    truck = load_truck()

    truck["maintenance"].append(item)

    save_truck(truck)



def athena_mechanic():

    truck = load_truck()


    advice = []


    if "6.2L Swap" not in truck["mods"]:

        advice.append(
            "Consider planning upgrades before an engine swap."
        )


    if len(truck["maintenance"]) == 0:

        advice.append(
            "Create a maintenance history so Athena can track reliability."
        )


    if len(truck["mods"]) > 3:

        advice.append(
            "Your build is becoming advanced. Check supporting systems."
        )


    return advice
