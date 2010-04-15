
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

    def __init__(self, obj, username, roles):
        super(SecurityRoleChangedEvent, self).__init__(obj)
        self.username = username
        self.roles = roles


class SecurityRoleAddedEvent(SecurityRoleChangedEvent):
    implements(ISecurityRoleAddedEvent)


class SecurityRoleRemovedEvent(SecurityRoleChangedEvent):
    implements(ISecurityRoleRemovedEvent)





