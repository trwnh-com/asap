# https://www.w3.org/ns/activitystreams#IntransitiveActivity
# Instances of IntransitiveActivity are a subtype of Activity representing intransitive actions.
# The object property is therefore inappropriate for these activities.
# Extends: Activity

class IntransitiveActivity(Activity):
    type = "IntransitiveActivity"
    id = null
    actor = null
    object = null