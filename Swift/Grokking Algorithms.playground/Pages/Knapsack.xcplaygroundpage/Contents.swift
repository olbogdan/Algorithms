import Foundation

struct Item {
    let name: String
    let weight: Int
    let value: Int
}

let items = [Item(name: "television", weight: 1, value: 500),
             Item(name: "candlesticks", weight: 1, value: 300),
             Item(name: "stereo", weight: 5, value: 400),
             Item(name: "laptop", weight: 7, value: 10000),
]

func knapsack(items: [Item], maxCapacity: Int) {
    var grid = [[Int]](
        repeating: [Int](repeating: 0, count: maxCapacity+1),
        count: items.count+1)
    for row in 1...items.count {
        let item = items[row-1]
        
        for column in 1...maxCapacity {
            
            if (item.weight > column) {
                grid[row][column] = grid[row-1][column]
                continue
            }
            else {
                grid[row][column] =
                max(
                    grid[row-1][column-item.weight] + item.value,
                    grid[row-1][column]
                )
            }
        }
    }
    
    // figure out solution from table
    var solution: [Item] = [Item]()
    var capacity = maxCapacity
    for i in stride(from: items.count, to: 0, by: -1) { // work backwards
        if grid[i - 1][capacity] != grid[i][capacity] {
            // did we use this item?
            solution.append(items[i - 1])
            capacity -= items[i - 1].weight
            // if we used an item, remove its weight
        }
    }
    print(solution)
}

knapsack(items: items, maxCapacity: 7)

/// Recoursive solution

func knapsack(items: [Item], currentIndex: Int, maxCapacity: Int) -> Int {
    
    if currentIndex < 0 || maxCapacity == 0 {
        return 0
    }
    let currentItem = items[currentIndex]
    if currentItem.weight > maxCapacity {
        return knapsack(items: items, currentIndex: currentIndex-1, maxCapacity: maxCapacity)
    } else {
        return max(knapsack(items: items, currentIndex: currentIndex-1, maxCapacity: maxCapacity),
                   knapsack(items: items, currentIndex: currentIndex-1, maxCapacity: maxCapacity - currentItem.weight) + currentItem.value)
    }
}

let price = knapsack(items: items, currentIndex: items.count-1, maxCapacity: 6)
print(price)
