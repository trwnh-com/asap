# https://www.w3.org/ns/activitystreams#Activity
# An Activity is a subtype of Object that describes some form of action that may happen, is currently happening, or has already happened.
# The Activity type itself serves as an abstract base type for all types of activities.
# It is important to note that the Activity type itself does not carry any specific semantics about the kind of action being taken.
#
# Extends: Object

class Activity(Object):
    type = "Activity"
    id = null
    actor = null
    object = null
    
    target = null
    result = null
    origin = null
    instrument =  null