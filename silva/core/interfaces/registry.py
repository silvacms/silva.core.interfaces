# Copyright (c) 2002-2009 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from zope import interface


class IRegistry(interface.Interface):
    """An registry is a special utility which exists only in memory
    (it's not dump in the ZOBD).
    """

class IIconRegistry(IRegistry):
    """A registry which contains icons.
    """

    def getIcon(content):
        """Get the icon associated with the content.
        """

    def getIconByIdentifier(identifier):
        """Get the icon associated with the identifier, which can by a
        meta_type or a mime type.
        """

    def registerIcon(identifier, icon_url):
        """Register the given icon url for the identifier (meta_type,
        or mime type).
        """


class IUpgradeRegistry(IRegistry):
    """It's a registry for upgrade purpose.
    """

    def registerUpgrader(upgrader, version=None, meta_type=None):
        pass

    def registerSetUp(function, version):
        pass

    def registerTearDown(function, version):
        pass

    def getUpgraders(version, meta_type):
        """Return the registered upgrade_handlers of meta_type
        """

    def upgradeObject(obj, version):
        pass

    def upgradeTree(root, version):
        """Upgrade a whole tree to version."""

    def upgrade(root, from_version, to_version):
        pass

    def setUp(root, version):
        pass

    def tearDown(root, version):
        pass
