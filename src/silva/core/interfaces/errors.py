# -*- coding: utf-8 -*-
# Copyright (c) 2011 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from silva.translations import translate as _
from OFS.interfaces import ITraversable


class SilvaError(Exception):
    """Generic error.
    """

    def reason(self):
        return self.args[0]


class VersioningError(SilvaError):
    """Error on versioning system.
    """


class PublicationWorkflowError(VersioningError):
    """Workflow errors.
    """


class ExportError(SilvaError):
    """An error during content export.
    """


class ExternalReferenceError(ExportError):
    """A reference is referring external content.
    """


class ImportError(SilvaError):
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
