# https://www.w3.org/ns/activitystreams#Link
#
# A Link is an indirect, qualified reference to a resource identified by a URL.
# The fundamental model for links is established by RFC5988.
# Many of the properties defined by the Activity Vocabulary allow values that are either instances of Object or Link.
# When a Link is used, it establishes a qualified relation connecting the subject (the containing object) to the resource identified by the href.
# Properties of the Link are properties of the reference as opposed to properties of the resource.
#
# Disjoint with: Object

null = None # translation into python syntax bc i'm lazy

class Link:
    type = "Link"
    href = null # every Link needs one of these
    
    rel = null
    mediaType = null
    name = null
    hreflang = null
    height = null
    width = null
    preview = null