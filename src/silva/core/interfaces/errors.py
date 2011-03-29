# -*- coding: utf-8 -*-
# Copyright (c) 2011 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$


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
