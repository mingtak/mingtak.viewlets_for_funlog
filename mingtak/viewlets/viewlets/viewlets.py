from zope.interface import Interface
from five import grok
from plone.app.layout.viewlets.interfaces import *
""" below viewlets manager can use.
IHTTPHeaders , IHtmlHead, IHtmlHeadLinks, IPortalTop,
IMainNavigation, IGlobalStatusMessage, IPortalHeader,
IToolbar, IAboveContent, IAboveContentTitle,
IDocumentActions,IBelowContentTitle, IAboveContentBody,
IBelowContentBody, IBelowContent, IPortalFooter, IScripts
"""


# Add viewlet manager, IWebsiteTop
from zope.viewlet.interfaces import IViewletManager
class IWebsiteTop(IViewletManager):
    """A viewlet manager
    """


# Below define customized viewlet
grok.context(Interface)
grok.templatedir('templates')


class SocialList(grok.Viewlet):
    grok.viewletmanager(IWebsiteTop)
