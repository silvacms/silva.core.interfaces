# Copyright (c) 2002-2009 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from zope.interface import Interface


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

from silva.core.interfaces.content import *
from silva.core.interfaces.extension import *
from silva.core.interfaces.registry import *
from silva.core.interfaces.service import *
from silva.core.interfaces.adapters import *
from silva.core.interfaces.events import *
from silva.core.interfaces.auth import *
from silva.core.interfaces.errors import *
from silva.core.interfaces.silvaxml import *


CLASS_CHANGES = {
    'silva.core.interfaces.service IFilesService':
        'silva.core.services.interfaces IFilesService',
}

