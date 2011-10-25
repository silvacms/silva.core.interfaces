# Copyright (c) 2009 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from zope.interface import Attribute, implements
from zope.component.interfaces import IObjectEvent, ObjectEvent
from zope.lifecycleevent.interfaces import IObjectModifiedEvent
from zope.lifecycleevent import ObjectModifiedEvent
from silva.core.interfaces.adapters import IRequestForApprovalStatus


# Root installation

class IInstallEvent(IObjectEvent):
    """An installation happened.
    """


class IInstallRootServicesEvent(IInstallEvent):
    """Root default services are being installed.

    Services should listen to this event to add themselves to a Silva
    root.
    """


class InstallRootServicesEvent(ObjectEvent):
    implements(IInstallRootServicesEvent)


class IInstalledExtensionEvent(IObjectEvent):
    """An extension have been installed.
    """
    root = Attribute(u"Root in which the extension have been installed")


class InstalledExtensionEvent(ObjectEvent):
    implements(IInstalledExtensionEvent)

    def __init__(self, extension, root):
        super(InstalledExtensionEvent, self).__init__(extension)
        self.root = root


class IInstalledServiceEvent(IObjectEvent):
    """A service has been installed.

    Code that want to configure a service after its installation
    should listen to this event.
    """


class InstalledServiceEvent(ObjectEvent):
    implements(IInstalledServiceEvent)


class IInstallRootEvent(IInstallEvent):
    """A Root is being installed. Root services are already installed
    and should be usable.
    """


class InstallRootEvent(ObjectEvent):
    implements(IInstallRootEvent)


# Ordered content move

class IContentOrderChangedEvent(IObjectEvent):
    """The position of a content have changed in an ordered container.
    """
    new_position = Attribute(u"New content position")
    old_position = Attribute(u"Old content position")


class ContentOrderChangedEvent(ObjectEvent):
    implements(IContentOrderChangedEvent)

    def __init__(self, obj, new_position, old_position):
        super(ContentOrderChangedEvent, self).__init__(obj)
        self.new_position = new_position
        self.old_position = old_position


# Content publication

class IPublishingEvent(IObjectModifiedEvent):
    """A publication action has been done.
    """


class IApprovalEvent(IPublishingEvent):
    """A approval operation is going on.
    """
    status = Attribute('Request for approval status')


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


class IContentApprovalRequestWithdrawnEvent(IRequestApprovalFailedEvent):
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


class PublishingEvent(ObjectModifiedEvent):
    implements(IPublishingEvent)


class ApprovalEvent(PublishingEvent):
    implements(IApprovalEvent)

    def __init__(self, obj, status=None):
        super(ApprovalEvent, self).__init__(obj)
        if status is None:
            status = IRequestForApprovalStatus(obj)
        self.status = status


class ContentApprovedEvent(ApprovalEvent):
    implements(IContentApprovedEvent)


class ContentUnApprovedEvent(ApprovalEvent):
    implements(IContentUnApprovedEvent)


class ContentRequestApprovalEvent(ApprovalEvent):
    implements(IContentRequestApprovalEvent)


class ContentApprovalRequestWithdrawnEvent(ApprovalEvent):
    implements(IContentApprovalRequestWithdrawnEvent)


class ContentApprovalRequestRefusedEvent(ApprovalEvent):
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

