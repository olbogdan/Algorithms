package leetcode.medium

class `1233 Remove Sub-Folders from the Filesystem` {
    fun removeSubfolders(folder: Array<String>): List<String> {
        val result = mutableListOf<String>()
        folder.sort()
        var prev = folder[0]
        result.add(prev)
        for (i in 1 ..< folder.size) {
            if (!folder[i].startsWith("$prev/")) {
                result.add(folder[i])
                prev = folder[i]
            }
        }
        return result
    }
}