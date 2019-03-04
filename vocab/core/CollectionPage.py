# https://www.w3.org/ns/activitystreams#CollectionPage
#
# Used to represent distinct subsets of items from a Collection.
# Refer to the Activity Streams 2.0 Core for a complete description of the CollectionPage object. 
#
# Extends: Collection

from vocab.core.Collection import Collection
null = None # translation into python syntax bc i'm lazy

class CollectionPage(Collection):
    type = "CollectionPage"

    partOf: Collection
    next = null
    prev = null