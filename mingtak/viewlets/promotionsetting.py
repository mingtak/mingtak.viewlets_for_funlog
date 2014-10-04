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


class IPromotionSetting(form.Schema, IImageScaleTraversable):
    """
    Promotional product setting
    """
    onSale = schema.Text(
        title=_(u"On sale product list"),
        description=_(u"List format is ....???"),
        required=False,
    )

    vacation = schema.Text(
        title=_(u"Vacation special product list"),
        description=_(u"List format is ....???"),
        required=False,
    )

    dress = schema.Text(
        title=_(u"Dress product list"),
        description=_(u"List format is ....???"),
        required=False,
    )

    beauty = schema.Text(
        title=_(u"Beauty product list"),
        description=_(u"List format is ....???"),
        required=False,
    )

    health = schema.Text(
        title=_(u"Haelth product list"),
        description=_(u"List format is ....???"),
        required=False,
    )

    entertainment = schema.Text(
        title=_(u"Entertainment product list"),
        description=_(u"List format is ....???"),
        required=False,
    )


class PromotionSetting(Container):
    grok.implements(IPromotionSetting)


class SampleView(grok.View):
    """ sample view class """

    grok.context(IPromotionSetting)
    grok.require('zope2.View')
    # grok.name('view')
