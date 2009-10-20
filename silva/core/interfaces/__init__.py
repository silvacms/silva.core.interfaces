# Copyright (c) 2002-2009 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from zope.interface import Interface

class IAccessManager(Interface):
    """Mixin class for objects to request local roles on the object"""

    def request_role(self, userid, role):
        """Request a role on the current object and send an e-mail to the
        editor/chiefeditor/manager"""

    def allow_role(self, userid, role):
        """Allows the role and send an e-mail to the user"""

    def deny_role(self, userid, role):
        """Denies the role and send an e-mail to the user"""


class RequiredParameterNotSetError(Exception):
    pass


class IMember(Interface):
    """A Silva member object.
    """

    def userid():
        """Return unique id for member/username
        """

    def fullname():
        """Return full name
        """

    def email():
        """Return users's email address if known, None otherwise.
        """

    def extra(name):
        """Return bit of extra information, keyed by name.
        """

    def is_approved():
        """Return true if this member is approved. Unapproved members
        may face restrictions on the Silva site.
        """

    def allowed_roles():
        """Private method which return a list of roles that that user
        can have.
        """


class IEditableMember(IMember):
    """A member which is able to see its information to be modified.
    """

    def set_fullname(fullname):
        """Change the fullname of the user.
        """

    def set_email(email):
        """Change member email.
        """

    def set_editor(editor):
        """Change editor email.
        """



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


from content import *
from extension import *
from registry import *
from service import *
from adapters import *
