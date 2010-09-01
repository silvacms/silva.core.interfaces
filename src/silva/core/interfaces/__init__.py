# Copyright (c) 2002-2009 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from zope.interface import Interface


class IAccessManager(Interface):
    """Mixin class for objects to request local roles on the object"""

    def request_role(userid, role):
        """Request a role on the current object and send an e-mail to the
        editor/chiefeditor/manager"""

    def allow_role(userid, role):
        """Allows the role and send an e-mail to the user"""

    def deny_role(userid, role):
        """Denies the role and send an e-mail to the user"""


class RequiredParameterNotSetError(Exception):
    pass


class IContainerPolicy(Interface):
    """Policy for container's default documents"""

    def createDefaultDocument(container, title):
        """create default document in given container"""


class IIcon(Interface):
    # XXX I don't like the name

    def getIconIdentifier():
        """Returns icon identifier.

        The icon registry should be able to return an icon from an
        icon identifier.
        """


class IUpgrader(Interface):
    """Interface for upgrade classes.
    """

    def upgrade(anObject):
        """Upgrades object

        During upgrade the object identity of the upgraded object may
        change.
        """


class ISubscription(Interface):
    """Subscription interface.
    """

    def emailaddress():
        """Return emailaddress for the subscription.
        """
        pass

    def contentSubscribedTo():
        """Return object for this subscription.
        """
        pass


from silva.core.interfaces.content import *
from silva.core.interfaces.extension import *
from silva.core.interfaces.registry import *
from silva.core.interfaces.service import *
from silva.core.interfaces.adapters import *
from silva.core.interfaces.events import *
from silva.core.interfaces.auth import *
