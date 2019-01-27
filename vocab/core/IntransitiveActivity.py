class IntransitiveActivity(Activity):
    type = "IntransitiveActivity"
    id = null
    actor = null
    object = null
    def __init__(self, id, actor):
        self.id = id
        self.actor = actor