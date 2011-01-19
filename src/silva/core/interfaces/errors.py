
from zope.interface.common.interfaces import IException
class INotViewable(IException):
    """Exception raised when a silva object has no viewable version"""
    
class INoDefaultDocument(IException):
    """Exception raised when attempting to access the public view
       of a container with no default document.  This is a 
       403 / forbidden error"""

