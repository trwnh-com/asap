class Activity(Object):
    type = "Activity"
    id = null
    actor = null
    object = null
    def __init__(self, id, actor, object):
        self.id = id
        self.actor = actor
        self.object = object
    
    target = null
    result = null
    origin = null
    instrument =  null