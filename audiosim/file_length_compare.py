# This algorithm is still very inefficient because it adds many of the pairs more than once
# Memoization using hashing must be added in order for this algorithm to be useful.

# Parameters : sorted list, integer representing max difference in length of files that should be compared
# Returns list of pairs of files that should be compared based on similarity in length
def findPairs(slist, dif):
    listLen = len(slist)
    for x in range(0, listLen - 1):
        for x2 in range(x+1, listLen):
            if slist[x2].fileLength - slist[x].fileLength <= dif:
                x2 += 1
            else:
                results = results + findPairs(slist, x, x2-1)
            x += 1
    return results


# Paramenters: sorted list, index1 and index2 defining the range of files that should be paired with each other
# Returns a list of lists: a list of every pair of files within a given range
def findPairs(slist, index1, index2):
    results = []
    for x in range(index1+1, index2):
        pair = [index1, x]
        results.append(pair)
        x += 1
    results = results + findPairs(slist, index1+1, index2)
    return results
