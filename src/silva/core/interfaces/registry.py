
# Copyright (c) 2002-2009 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from zope import interface


class IRegistry(interface.Interface):
    """An registry is a special utility which exists only in memory
    (it's not dump in the ZOBD).
    """


class IContentMimetypeRegistry(IRegistry):
    """Associate content factory to content mimetype.
    """

    def get(mimetype, default=None):
        """Return a content factory associated to this mimetype, or
        return default (which default to None).
        """

    def register(mimetype, factory, extension):
        """Register the factory ``factory`` to create a content of
        type ``mimetype``. Factory comes from ``extension``.
        """

    def unregister(factory):
        """Unregister the given factory.
        """


class IIconRegistry(IRegistry):
    """A registry which contains icons.
    """

    def get_icon(content):
        """Get the icon associated with the content.
        """

    def get_icon_by_identifier(identifier):
        """Get the icon associated with the identifier, which can by a
        meta_type or a mime type.
        """

    def register(identifier, icon_url):
        """Register the given icon url for the identifier (meta_type,
        or mime type).
        """


class IUpgradeRegistry(IRegistry):
    """It's a registry for upgrade purpose.
    """

    def register(upgrader, version=None, meta_type=None):
        """Register an upgrade step to go to the given version for the
        given object type.
        """

    def get_upgraders(version, meta_type):
        """Return the registered upgrade_handlers of meta_type.
        """

    def upgrade_tree(obj, version):
        """Upgrade obj and all its children up for the given version.
        """

    def upgrade(root, from_version, to_version):
        """Upgrade obj and all its children for all version between
        from_version and to_version.
        """
