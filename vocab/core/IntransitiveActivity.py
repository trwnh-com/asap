# https://www.w3.org/ns/activitystreams#IntransitiveActivity
#
# Instances of IntransitiveActivity are a subtype of Activity representing intransitive actions.
# The object property is therefore inappropriate for these activities.
#
# Extends: Activity

from vocab.core.Activity import Activity
null = None # translation into python syntax bc i'm lazy

class IntransitiveActivity(Activity):
    type = "IntransitiveActivity"
    # Activity.object should not be inherited, but there isn't any way to model this with classic inheritance?
    # - At best, perhaps we can say that a sanitizer should verify that IntransitiveActivity.object = null...