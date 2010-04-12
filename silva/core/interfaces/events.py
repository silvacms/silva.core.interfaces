
from zope.interface import Attribute, implements
from zope.component.interfaces import IObjectEvent, ObjectEvent


class ISecurityChangedEvent(IObjectEvent):

    username = Attribute(u"Username affected by the change.")


class ISecurityRoleAddedEvent(ISecurityChangedEvent):
    pass

class ISecurityRoleRemovedEvent(ISecurityChangedEvent):
    pass


class SecurityChangedEvent(ObjectEvent):
    implements(ISecurityChangedEvent)

    def __init__(self, obj, username):
        super(SecurityChangedEvent, self).__init__(obj)
        self.username = username


class SecurityRoleAddedEvent(SecurityChangedEvent):
    implements(ISecurityRoleAddedEvent)


class SecurityRoleRemovedEvent(SecurityChangedEvent):
    implements(ISecurityRoleRemovedEvent)





