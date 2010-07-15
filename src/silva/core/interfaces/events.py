# Copyright (c) 2009 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from zope.interface import Attribute, implements
from zope.component.interfaces import IObjectEvent, ObjectEvent


# Content publication

class IContentPublicationEvent(IObjectEvent):
    pass


class IContentApprovedEvent(IContentPublicationEvent):
    pass


class IContentClosedEvent(IContentPublicationEvent):
    pass


# Content import/export

class IContentImportedExported(IObjectEvent):
    """A content have been imported or exported from the site.
    """


class IContentImported(IContentImportedExported):
    """A new content have been imported in the site.
    """


class IContentExported(IContentImportedExported):
    """A content have been exported from the site.
    """


class ContentImportedExported(ObjectEvent):
    implements(IContentImportedExported)


class ContentImported(ContentImportedExported):
    implements(IContentImported)


class ContentExported(ContentImportedExported):
    implements(IContentExported)


# Security

class ISecurityEvent(IObjectEvent):
    """A security setting has been changed.
    """


class ISecurityRestrictionModifiedEvent(ISecurityEvent):
    """A security restriction has been set on an object.
    """
    role = Attribute(u"Role needed to access the object")


class ISecurityRoleChangedEvent(ISecurityEvent):
    """A security role has been changed for a user.
    """
    username = Attribute(u"Username affected by the change.")
    roles =  Attribute(u"Modified role.")


class ISecurityRoleAddedEvent(ISecurityRoleChangedEvent):
    """A role as been attributed to a user.
    """


class ISecurityRoleRemovedEvent(ISecurityRoleChangedEvent):
    """A user as seen its access revoked.
    """


class SecurityRestrictionModifiedEvent(ObjectEvent):
    implements(ISecurityRestrictionModifiedEvent)

    def __init__(self, obj, role):
        super(SecurityRestrictionModifiedEvent, self).__init__(obj)
        self.role = role


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





