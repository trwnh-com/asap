# https://www.w3.org/ns/activitystreams#OrderedCollection
#
# A subtype of Collection in which members of the logical collection are assumed to always be strictly ordered.
#
# Extends: Collection

from vocab.core.Collection import Collection
null = None # translation into python syntax bc i'm lazy

class OrderedCollection(Collection):
    def __init__(self, type="OrderedCollection"):
        self.type = type