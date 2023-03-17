import Foundation

var statesNeeded : Set = ["mt", "wa", "or", "id", "nv", "ut", "ca", "az", "al"]

var stations = [String: Set<String>]()
stations["kone"] = ["id", "nv", "ut"]
stations["ktwo"] = ["wa", "id", "mt"]
stations["kthree"] = ["or", "nv", "ca"]
stations["kfour"] = ["nv", "ut"]
stations["kfive"] = ["ca", "az"]
stations["kAlaska"] = ["al"]

var finalStations = Set<String>();

func findBestStation() -> (String, Set<String>)? {
    var bestStation: (String, Set<String>)? = nil
    var bestCoverage = 0
    for station in stations {
        let count = statesNeeded.intersection(station.value).count
        if count > bestCoverage {
            bestCoverage = count
            bestStation = station
        }
    }
    return bestStation
}

while !statesNeeded.isEmpty {
    guard let (station, states) = findBestStation() else {
        print("all states can not be covered")
        break
    }
    statesNeeded.subtract(states)
    finalStations.insert(station)
}

print(statesNeeded)
print(finalStations)

