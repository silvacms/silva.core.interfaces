# -*- coding: utf-8 -*-
# Copyright (c) 2002-2013 Infrae. All rights reserved.
# See also LICENSE.txt

from zope.interface import Interface
import zope.deferredimport
from grokcore.component.interfaces import IContext
from silva.core.interfaces.content import IReferable

zope.deferredimport.deprecated(
    'IFilesService moved to silva.core.services.interfaces. '
    'This import will be removed in Silva 3.1',
    IFilesService='silva.core.services.interfaces:IFilesService')


class IZMIObject(IContext, IReferable):
    """An object in ZMI.
    """


class IInvisibleService(Interface):
    """Marker interface for services that want to be not visible in
    the ZMI."""


class ISilvaService(IZMIObject):
    """Basic Silva service.
    """


class ISilvaLocalService(ISilvaService):
    """A Silva service which can be added in a local site.
    """


class IMessageService(ISilvaService, ISilvaLocalService):
    """Send messages to members.
    """

    def send_message(from_memberid, to_memberid, subject, message):
        """Send a message from one member to another.
        """

    def send_pending_messages():
        """Send all pending messages.

        This needs to be called at the end of a request otherwise any
        messages pending may be lost.
        """

