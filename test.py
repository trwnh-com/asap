from vocab.core.OrderedCollectionPage import OrderedCollectionPage
from vocab.core.OrderedCollection import OrderedCollection

page = OrderedCollectionPage()
collection = OrderedCollection()
page.partOf = collection
collection.id = 2
print("part of " + page.partOf.type + " " + str(page.partOf.id))