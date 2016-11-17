# This module used the API of textPreprocess for calculating
# the document distances


def docdistance(documents1, documents2):
    distance = 0
    for word in documents1.getwords():
        distance += documents1.getoccurence(word) * documents2.getoccurence(word)
    distance = distance / (documents1.returnmodel() * documents2.returnmodel())
    return distance

