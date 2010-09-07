# Copyright (c) 2009 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from zope.interface import Attribute, implements
from zope.component.interfaces import IObjectEvent, ObjectEvent


# Content publication

class IPublishingEvent(IObjectEvent):
    """A publication action has been done.
    """


class IApprovalEvent(IPublishingEvent):
    """A approval operation is going on.
    """


class IContentApprovedEvent(IApprovalEvent):
    """A content has been approved.
    """


class IContentUnApprovedEvent(IApprovalEvent):
    """A content has been unapproved.
    """


class IRequestApprovalEvent(IApprovalEvent):
    """An approval request is being managed.
    """


class IRequestApprovalFailedEvent(IRequestApprovalEvent):
    """An approval request has been managed.
    """


class IContentRequestApprovalEvent(IRequestApprovalEvent):
    """A content seeks to be approved.
    """


class IContentApprovalRequestCanceledEvent(IRequestApprovalFailedEvent):
    """A content request for approval have been cancelled.
    """


class IContentApprovalRequestRefusedEvent(IRequestApprovalFailedEvent):
    """A content request for approval have been refused.
    """


class IContentPublishedEvent(IPublishingEvent):
    """A content has been published.
    """


class IContentClosedEvent(IPublishingEvent):
    """A content as been closed.
    """


class IContentExpiredEvent(IContentClosedEvent):
    """A content expired.
    """


class PublishingEvent(ObjectEvent):
    implements(IPublishingEvent)


class ContentApprovedEvent(PublishingEvent):
    implements(IContentApprovedEvent)


class ContentUnApprovedEvent(PublishingEvent):
    implements(IContentUnApprovedEvent)


class ContentRequestApprovalEvent(PublishingEvent):
    implements(IContentRequestApprovalEvent)


class ContentApprovalRequestCanceledEvent(PublishingEvent):
    implements(IContentApprovalRequestCanceledEvent)


class ContentApprovalRequestRefusedEvent(PublishingEvent):
    implements(IContentApprovalRequestRefusedEvent)


class ContentPublishedEvent(PublishingEvent):
    implements(IContentPublishedEvent)


class ContentClosedEvent(PublishingEvent):
    implements(IContentClosedEvent)


class ContentExpiredEvent(ContentClosedEvent):
    implements(IContentExpiredEvent)


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


class IInvalidateSidebarEvent(IObjectEvent):
    """ flush sidebar cache for the object
    """

class InvalidateSidebarEvent(ObjectEvent):
    implements(IInvalidateSidebarEvent)
