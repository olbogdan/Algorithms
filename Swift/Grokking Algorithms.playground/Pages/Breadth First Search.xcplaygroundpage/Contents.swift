import Foundation

let graphFriends = ["me": ["alis", "bob"], "bob": ["petr"], "alis": ["oksana"], "oksana" : [], "petr": []]

func findThePerson(_ name: String) -> Bool {
    var checked: [String] = []
    var friendsToCheck: [String] = []
    if let myFriends = graphFriends["me"] {
        friendsToCheck.append(contentsOf: myFriends)
    }
    
    while !friendsToCheck.isEmpty {
        let person = friendsToCheck.removeFirst()
        if checked.contains(person) {
            continue
        }
        if person == name {
            return true
        } else {
            checked.append(person)
            if let person = graphFriends[person] {
                friendsToCheck.append(contentsOf: person)
            }
        }
    }
    return false
}
var greeting = "\(findThePerson("oksana"))"
print(greeting)
