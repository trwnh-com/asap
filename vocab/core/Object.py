# https://www.w3.org/ns/activitystreams#Object
# 
# Describes an object of any kind.
# The Object type serves as the base type for most of the other kinds of objects defined in the Activity Vocabulary,
# including other Core types such as Activity, IntransitiveActivity, Collection and OrderedCollection.
# 
# Disjoint with: Link

null = None # translation into python syntax bc i'm lazy

class Object:
    def __init__(self, type="Object"):
        self.type = type
    id = null # every Object needs one of these
    
    attachment = null
    attributedTo = null
    audience = null
    content = null
    context = null
    name = null
    endTime = null
    generator = null
    icon = null
    image = null
    inReplyTo = null
    location = null
    preview = null
    published = null
    replies = null
    startTime = null
    summary = null
    tag = null
    updated = null
    url = null
    to = null
    bto = null
    cc = null
    bcc = null
    mediaType = null
    duration = null