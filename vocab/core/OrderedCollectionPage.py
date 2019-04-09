# https://www.w3.org/ns/activitystreams#OrderedCollectionPage
#
# Used to represent ordered subsets of items from an OrderedCollection.
# Refer to the Activity Streams 2.0 Core for a complete description of the OrderedCollectionPage object. 
#
# Extends: OrderedCollection | CollectionPage

from vocab.core.OrderedCollection import OrderedCollection
from vocab.core.CollectionPage import CollectionPage
null = None # translation into python syntax bc i'm lazy

class OrderedCollectionPage(OrderedCollection, CollectionPage):

    def __init__(self, type="OrderedCollectionPage"):
        self.type = type
