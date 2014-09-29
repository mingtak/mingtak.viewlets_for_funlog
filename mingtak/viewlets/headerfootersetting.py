from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable


from mingtak.viewlets import MessageFactory as _


# Interface class; used to define content-type schema.

class IHeaderFooterSetting(form.Schema, IImageScaleTraversable):
    """
    Website header and footer setting
    """
    socialFacebook = schema.TextLine(
        title=_(u"Facebook url"),
        required=True,
    )

    socialGooglePlus = schema.TextLine(
        title=_(u"Google+ url"),
        required=True,
    )

    socialTwitter = schema.TextLine(
        title=_(u"Twitter url"),
        required=True,
    )

    socialEmail = schema.TextLine(
        title=_(u"Email address"),
        required=True,
    )


class HeaderFooterSetting(Container):
    grok.implements(IHeaderFooterSetting)


class SampleView(grok.View):
    """ sample view class """

    grok.context(IHeaderFooterSetting)
    grok.require('zope2.View')
    # grok.name('view')
