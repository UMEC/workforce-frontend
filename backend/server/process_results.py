import pickle
import json

def process_results(path):
    with open("results.pkl", "rb") as f:
        results = pickle.load(f)

    with open("population.pkl", "rb") as f:
        population = pickle.load(f)

    pd = {}
    for year in results:
        print(year)
        pd[year] = {}
        for county in results[year]:
            if "MCD" not in county:
                county_clean = county.replace(" County", "")
                pd[year][county_clean] = {}
                pd[year][county_clean]["demand"] = list(results[year][county]["demand"].values())[0]
                pd[year][county_clean]["supply"] = results[year][county]["supply"]
                pd[year][county_clean]["population"] = population[year][county]


    localHealthDistricts = {
        "Bear River": ["Box Elder", "Cache", "Rich"],
        "Central Utah": ["Juab", "Millard", "Piute", "Sevier", "Wayne", "Sanpete"],
        "Davis": ["Davis"],
        "Salt Lake": ["Salt Lake"],
        "San Juan": ["San Juan"],
        "Southeast Utah":  ["Carbon", "Emery", "Grand"],
        "Southwest Utah": ["Garfield", "Iron", "Kane", "Washington", "Beaver"],
        "Summit": ["Summit"],
        "Tooele":  ["Tooele"],
        "TriCounty": ["Daggett", "Duchesne", "Uintah"],
        "Utah": ["Utah"],
        "Wasatch": ["Wasatch"],
        "Weber-Morgan": ["Weber", "Morgan"]
    }


    lhdData = {}
    for year in results:
        lhdData[year] = {}
        for district in localHealthDistricts:
            lhdData[year][district] = {"population": 0, "demand": {}, "supply": {}}
            for county in localHealthDistricts[district]:
                lhdData[year][district]["population"] += pd[year][county]["population"]
                for prof, val in pd[year][county]["demand"].items():
                    lhdData[year][district]["demand"].setdefault(prof, 0)
                    lhdData[year][district]["demand"][prof] += val
                for prof, val in pd[year][county]["supply"].items():
                    lhdData[year][district]["supply"].setdefault(prof, 0)
                    lhdData[year][district]["supply"][prof] += val
        lhdData[year]["State of Utah"] = pd[year]["State of Utah"]

    stateData = {"counties": pd, "LHD": lhdData}
    
    with open(path, "w") as f:
        json.dump(stateData, f)