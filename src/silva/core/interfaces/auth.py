# -*- coding: utf-8 -*-
# Copyright (c) 2010 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from zope import interface, schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from silva.translations import translate as _


class IMember(interface.Interface):
    """A Silva member object.
    """

    def userid():
        """Return unique identifer for member (username).
        """

    def fullname():
        """Return full name of the menber.
        """

    def email():
        """Return user's email address if known, None otherwise.
        """

    def extra(name):
        """Return bit of extra information, keyed by name.
        """

    def is_approved():
        """Return true if this member is approved. Unapproved members
        may face restrictions on the Silva site.
        """

    def allowed_roles():
        """Private method which return a list of roles that that user
        can have.
        """


class IEditableMember(IMember):
    """A member which is able to see its information to be modified.
    """

    def set_email(email):
        """Change member email.
        """

    def set_fullname(fullname):
        """Change member fullname.
        """


class IGroup(interface.Interface):

    def groupid():
        """Return group unique identifier.
        """

    def groupname():
        """Return friendly group name (or identifier if unknown).
        """

    def allowed_roles():
        """Private method which return a list of roles that that the
        group can have.
        """


class IAccessSecurity(interface.Interface):
    """Manage access restriction to the content.
    """
    minimum_role = interface.Attribute(
        u"Property giving access to set_minimum_role/get_minimum_role")
    acquired = interface.Attribute(u"Property giving access to is_acquired")

    def set_acquired():
        """Set the access restriction to acquire its settings.
        """

    def is_acquired():
        """Check whether the access restriction is acquired (the
        current restriction is set on one of the parents, not the
        content itself).
        """

    def set_minimum_role(role):
        """Set `role` as the minimum role needed to access this
        content.

        If `role` is Anonymous, the access restriction will be
        acquired.
        """

    def get_minimum_role():
        """Get the minimum role needed to access the content here.
        """

def _add_silva_role(terms):
    for value, title in [('Viewer', _('Viewer')),
                         ('Viewer +', _('Viewer +')),
                         ('Viewer ++', _('Viewer ++')),
                         ('Reader', _('Reader')),
                         ('Author', _('Author')),
                         ('Editor', _('Editor')),
                         ('ChiefEditor', _('ChiefEditor')),
                         ('Manager', _('Manager')),]:
        terms.append(SimpleTerm(value=value, token=value, title=title))

@apply
def role_vocabulary():
    terms = [SimpleTerm(value=None, token='None', title=_(u'select:'))]
    _add_silva_role(terms)
    return SimpleVocabulary(terms)


@apply
def authenticated_role_vocabulary():
    terms = [SimpleTerm(value=None, token='None', title=_(u'select:')),
             SimpleTerm(value='Authenticated',
                        token='Authenticated',
                        title=_('Authenticated'))]
    _add_silva_role(terms)
    return SimpleVocabulary(terms)


class IAuthorization(interface.Interface):
    """A user authorization.
    """
    identifier = schema.TextLine(
        title=_(u"identifier"))
    type = interface.Attribute(u"user or group")
    acquired_role = schema.Choice(
        title=_(u"role defined above"),
        source=role_vocabulary,
        required=False)
    local_role = schema.Choice(
        title=_(u"role defined here"),
        source=role_vocabulary,
        required=False)

    def grant(role):
        """Grant a new role to the user, if it doesn't already have it
        The current user must have at least that role.
        """

    def revoke():
        """Revoke all Silva roles defined at this level for this user,
        if the current user have at least that role.
        """


class IAuthorizationManager(interface.Interface):
    """Manage authorization at a given level.
    """

    def get_user_role(user_id=None):
        pass

    def get_authorization(identifer=None, dont_acquire=False):
        """Return authorization object for the given user or group.

        If no identifier is specified, return authorization object for the
        current authenticated user.

        If dont_acquire is set to True, no acquired roles would be
        looked up (only local roles).
        """

    def get_authorizations(identifiers, dont_acquire=False):
        """Return all authorizations objects at this level for the
        given list of users or groups.

        If dont_acquire is set to True, no acquired roles would be
        looked up (only local roles).
        """

    def get_defined_authorizations(dont_acquire=False):
        """Return current all authorizations objects that defines
        authorization in Silva for users and groups at this level.

        If dont_acquire is set to True, no acquired roles would be
        looked up (only local roles).
        """


__all__ = [
    'IMember', 'IEditableMember', 'IGroup',
    'IAccessSecurity', 'IAuthorizationManager', 'IAuthorization',
    'authenticated_role_vocabulary', 'role_vocabulary']
