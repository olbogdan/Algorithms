import Foundation

var graph = [String: [String: Double]]()
graph["Start"] = [String: Double]()
graph["Start"]?["A"] = 10
graph["Start"]?["B"] = 2
graph["A"] = [String: Double]()
graph["A"]?["Finish"] = 100
graph["B"] = [String: Double]()
graph["B"]?["A"] = 1
graph["B"]?["Finish"] = 20
graph["Finish"] = [String: Double]()

var costs = [String: Double]()
costs["Start"] = 0
costs["Finish"] = Double.infinity


func calculateShotestPath() {
    var parents = [String: String]()
    var processed: [String] = [String]()
    
    var node = findLowestCostNode(in: costs, exclude: processed)
    while node != nil {
        let cost = costs[node!]
        let neighbors = graph[node!]
        for (neighbor, nCost) in neighbors! {
            let newCost = cost! + nCost
            if costs[neighbor] ?? Double.infinity > newCost {
                costs[neighbor] = newCost
                parents[neighbor] = node!
            }
        }
        processed.append(node!)
        node = findLowestCostNode(in: costs, exclude: processed)
    }
    
    print(costs)
    print(parents)
}

func findLowestCostNode(in costs: [String: Double], exclude processed: [String]) -> String? {
    var lowestCost = Double.infinity
    var lowestCostNode: String? = nil

    for node in costs {
        let cost = node.value
        if (cost < lowestCost) && !processed.contains(node.key) {
            lowestCost = cost
            lowestCostNode = node.key
        }
    }
    return lowestCostNode
}

calculateShotestPath()

