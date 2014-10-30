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
    heroImage_1 = schema.URI(
        title=_(u"Hero promotion image 1 url"),
        description=_(u"must inculde 'http://'"),
        required=False,
    )

    heroDescription_1 = schema.Text(
        title=_(u"Hero promotion 1 text"), 
        description=_(u"Using html language"),
        required=False, 
    )

    heroImage_2 = schema.URI(
        title=_(u"Hero promotion image 2 url"),
        description=_(u"must inculde 'http://'"),
        required=False, 
    )

    heroDescription_2 = schema.Text(
        title=_(u"Hero promotion 2 text"),
        description=_(u"Using html language"),
        required=False,
    )

    heroImage_3 = schema.URI(
        title=_(u"Hero promotion image 3 url"),
        description=_(u"must inculde 'http://'"),
        required=False,
    )

    heroDescription_3 = schema.Text(
        title=_(u"Hero promotion 3 text"),
        description=_(u"Using html language"),
        required=False,
    )

    heroImage_4 = schema.URI(
        title=_(u"Hero promotion image 4 url"),
        description=_(u"must inculde 'http://'"),
        required=False,
    )

    heroDescription_4 = schema.Text(
        title=_(u"Hero promotion 4 text"),
        description=_(u"Using html language"),
        required=False,
    )

    heroImage_5 = schema.URI(
        title=_(u"Hero promotion image 5 url"),
        description=_(u"must inculde 'http://'"),
        required=False,
    )

    heroDescription_5 = schema.Text(
        title=_(u"Hero promotion 5 text"),
        description=_(u"Using html language"),
        required=False,
    )

    promotionBanner = schema.Text(
        title=_(u"Prometion Banner"),
        description=_(u"Using html language"),
        required=False,
    )



    promotionTab_1 = schema.Text(
        title=_(u"Promotion tab 1 on homepage"),
        description=_(u"First line is catalog name, other line is products id"),
        required=False,
    )

    promotionTab_2 = schema.Text(
        title=_(u"Promotion tab 2 on homepage"),
        description=_(u"First line is catalog name, other line is products id"),
        required=False,
    )

    promotionTab_3 = schema.Text(
        title=_(u"Promotion tab 3 on homepage"),
        description=_(u"First line is catalog name, other line is products id"),
        required=False,
    )

    promotionTab_4 = schema.Text(
        title=_(u"Promotion tab 4 on homepage"),
        description=_(u"First line is catalog name, other line is products id"),
        required=False,
    )

    promotionTab_5 = schema.Text(
        title=_(u"Promotion tab 5 on homepage"),
        description=_(u"First line is catalog name, other line is products id"),
        required=False,
    )


class PromotionSetting(Container):
    grok.implements(IPromotionSetting)


class SampleView(grok.View):
    """ sample view class """

    grok.context(IPromotionSetting)
    grok.require('zope2.View')
    # grok.name('view')
