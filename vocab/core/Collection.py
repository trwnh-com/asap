# https://www.w3.org/ns/activitystreams#Collection
#
# A Collection is a subtype of Object that represents ordered or unordered sets of Object or Link instances.
# Refer to the Activity Streams 2.0 Core specification for a complete description of the Collection type. 
#
# Extends: Object


from Object import Object
null = None # translation into python syntax bc i'm lazy

class Collection(Object):
    def __init__(self, type="Collection"):
        self.type = type

    totalItems = null
    current = null
    first = null
    last = null
    items = null
    orderedItems = null # this one is actually not documented in as-vocab, it's only in as-core?
    # imo... either orderedItems should not exist, or OrderedCollection should not exist.