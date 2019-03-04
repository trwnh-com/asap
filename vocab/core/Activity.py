# https://www.w3.org/ns/activitystreams#Activity
#
# An Activity is a subtype of Object that describes some form of action that may happen, is currently happening, or has already happened.
# The Activity type itself serves as an abstract base type for all types of activities.
# It is important to note that the Activity type itself does not carry any specific semantics about the kind of action being taken.
#
# Extends: Object

from vocab.core.Object import Object
null = None # translation into python syntax bc i'm lazy

class Activity(Object):
    type = "Activity"
    actor = null
    object = null
    
    target = null
    result = null
    origin = null
    instrument =  null