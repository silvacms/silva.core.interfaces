
from zope.interface import Attribute, implements
from zope.component.interfaces import IObjectEvent, ObjectEvent


class ISecurityRoleChangedEvent(IObjectEvent):

    username = Attribute(u"Username affected by the change.")
    role =  Attribute(u"Modified role.")


class ISecurityRoleAddedEvent(ISecurityRoleChangedEvent):
    pass

class ISecurityRoleRemovedEvent(ISecurityRoleChangedEvent):
    pass


class SecurityRoleChangedEvent(ObjectEvent):
    implements(ISecurityRoleChangedEvent)

    def __init__(self, obj, username, role):
        super(SecurityChangedEvent, self).__init__(obj)
        self.username = username
        self.role = role


class SecurityRoleAddedEvent(SecurityChangedEvent):
    implements(ISecurityRoleAddedEvent)


class SecurityRoleRemovedEvent(SecurityChangedEvent):
    implements(ISecurityRoleRemovedEvent)





