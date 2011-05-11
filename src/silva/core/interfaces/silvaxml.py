from zope.interface import Interface, Attribute


class IImportExportSettings(Interface):
    """ settings for import/export context information
    """

    errors = Attribute('list of non fatal errors')

    def append_error(error):
        """ Add a non fatal error
        """


class IExportSettings(IImportExportSettings):
    """ export settings
    """


class IImportSettings(IImportExportSettings):
    """ import settings
    """


class ISilvaXMLHandler(Interface):
    """ import/export handler
    """


class ISilvaXMLImportHandler(ISilvaXMLHandler):
    """ import Handler
    """


class ISilvaXMLExportHandler(ISilvaXMLHandler):
    """ export Handler
    """


