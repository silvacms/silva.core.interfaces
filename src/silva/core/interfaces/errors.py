# -*- coding: utf-8 -*-
# Copyright (c) 2011 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from silva.translations import translate as _
from OFS.interfaces import ITraversable
from zope.schema.interfaces import InvalidValue

# Ghost validation

class InvalidTarget(InvalidValue):
    __doc__ = _("Invalid ghost target.")


class EmptyInvalidTarget(InvalidTarget):
    __doc__ = _(u"Missing required ghost target.")


class CircularInvalidTarget(InvalidTarget):
    __doc__ = _(u"Ghost target creates a circular reference.")


class GhostInvalidTarget(InvalidTarget):
    __doc__ = _(u"Ghost target is a ghost.")


class ContainerInvalidTarget(InvalidTarget):
    __doc__ = _(u"Ghost target should be a container.")


class ContentInvalidTarget(InvalidTarget):
    __doc__ = _(u"Ghost target should be a content.")


# Silva errors

class SilvaError(Exception):
    """Generic error.
    """

    def __init__(self, reason):
        self.reason = reason


class ContentError(SilvaError):
    """An error that happened on content.
    """

    def __init__(self, reason, content):
        super(ContentError, self).__init__(reason)
        self.content = content


class ContainerError(ContentError):
    """An error happened while working on a container.
    """


class VersioningError(ContentError):
    """Error on versioning system.
    """

    def __init__(self, reason, content, version=None):
        super(VersioningError, self).__init__(reason, content)
        self.version = version


class PublicationError(VersioningError):
    """Workflow errors.
    """


class ExportError(ContentError):
    """An error during content export.
    """


class ExternalReferenceError(ExportError):
    """A reference is referring external content.
    """


class ImportError(ContentError):
    """An error during import.
    """


class ImportWarning(ImportError):
    """An non-fatal error during import.
    """

    def reason(self):
        path, reason = self.args
        if ITraversable.providedBy(path):
            path = '/'.join(path.getPhysicalPath())
        return _(u"Error while importing: ${path}: ${reason}",
                 mapping=dict(path=path, reason=reason))
