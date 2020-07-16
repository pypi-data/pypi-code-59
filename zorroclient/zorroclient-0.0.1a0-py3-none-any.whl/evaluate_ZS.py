from datetime import datetime
import json
from .models.indicator import Indicator
from . import presets

def evaluate_preset_bad(preset_id, ticker):
    presets = json.load(open("../presets.json"))
    if not preset_id in presets:
        return "Preset ID not Found!"

    p = presets[preset_id]["content"]

    if p["type"] == "operator":

        bool = p["boolean_operator"]

        indic = []
        for i in p["params"]:
            if i["type"] == "indicator":
                temp = Indicator(i["indicator"], "base-url")
                set = i["settings"]
                set["operator"] = p["operator"]
                indic.append(temp.calculate(ticker, datetime.now(), set))

        if bool == "and": return not False in indic
        elif bool == "or": return True in indic
        elif bool == "atleast2": return indic.count(True) >= 2


    return False


#Returns a ZorroScript Command to be appended to commands[]
def process_preset(preset_id, ticker):
    presets = json.load(open("../presets.json"))
    if not preset_id in presets:
        return "Preset ID not Found!"

    return preset[preset_id]["content"]
