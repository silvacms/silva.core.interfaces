from zope.interface import Interface
from zope.publisher.interfaces.browser import IBrowserRequest

#----------------------------------------------
# for content layout (silva.core.contentlayout)
#----------------------------------------------

class IDefaultContentTemplate(Interface):
    """The default content template for rendered Silva content which does not
       support IContentLayout.  This view wraps the rendered silva content 
       (passed in via set_content) with the desires default content template.
       The dct can add a left nav (or not), a title (at the appropriate heading
       level), etc.
       
       Override this in your own layer to provide a custom-tailored default
       content template for your own layout.  You can also create layouts
       tailored for specific content types by changing the grok.context.
       
       Before calling this template, you ought to set the following properties:
       
       page 
       -- the silva.core.views.views.Page
       rendered_content
       -- the rendered content being wrapped inside this default content 
          template
        layout
        -- the Layout object the page is wrapped around
    """

class IVersionedContentLayout(Interface):
    """Marker interface for VersionedContent objects wich
       store versiones supporting content layout
    """

class IContentLayout(Interface):
    """An interface to support complex content layouts.
       NOTE: for versionedcontent, the versions provide this interface
    """
    
    def add_part_to_slot(part, slot):
        """@part(IContentLayoutPart)
           @slot - name of a slot
           add the part to the slot with the given mane.
           May or may not require validation that the slot name
           is valid for the current layout
        """
    
    def get_parts_for_slot(slot):
        """@slot - name of a slot for the current layout
           returns the list of parts in the specified slot
        """

__all__ = ['IVersionedContentLayout','IContentLayout', 
           'IDefaultContentTemplate']