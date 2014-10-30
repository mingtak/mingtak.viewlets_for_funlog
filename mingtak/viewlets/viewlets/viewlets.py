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
from zope.viewlet.interfaces import IViewletManager


# Add viewlet manager, IGoogleAD, grok way
class IGoogleAdResponsive(grok.ViewletManager):
    grok.name('IGoogleAdResponsive')

# Add viewlet manager, IAddThis, grok way
class IAddThis(grok.ViewletManager):
    grok.name('IAddThis')

# Add viewlet manager, IDisqus, grok way
class IDisqus(grok.ViewletManager):
    grok.name('IDisqus')

# Add viewlet manager, IMaybeYouLike, grok way
class IMaybeYouLike(grok.ViewletManager):
    grok.name('IMaybeYouLike')

# Add viewlet manager, ICollection, ZCML way
class ICollection(IViewletManager):
    """A viewlet manager for collection
    """

# Add viewlet manager, IHomePage, ZCML way
class IHomePage(IViewletManager):
    """A viewlet manager for homepage
    """

# Add viewlet manager, IWebsiteTop, ZCML way
class IWebsiteTop(IViewletManager):
    """A viewlet manager
    """


# Below define customized viewlet
grok.context(Interface)
grok.templatedir('templates')

class SocialList(grok.Viewlet):
    grok.viewletmanager(IWebsiteTop)

class HomePageHero(grok.Viewlet):
    grok.viewletmanager(IHomePage)

class HomePagePromotionBanner(grok.Viewlet):
    grok.viewletmanager(IHomePage)

class HomePagePromotionTab(grok.Viewlet):
    grok.viewletmanager(IHomePage)

"""
class HomePageOnSale(grok.Viewlet):
    grok.viewletmanager(IHomePage)

class HomePageVacation(grok.Viewlet):
    grok.viewletmanager(IHomePage)

class HomePageDress(grok.Viewlet):
    grok.viewletmanager(IHomePage)

class HomePageBeauty(grok.Viewlet):
    grok.viewletmanager(IHomePage)

class HomePageHealth(grok.Viewlet):
    grok.viewletmanager(IHomePage)

class HomePageEntertainment(grok.Viewlet):
    grok.viewletmanager(IHomePage)

class CollectionContent(grok.Viewlet):
    grok.viewletmanager(ICollection)
"""

class AddThisViewlet(grok.Viewlet):
    grok.viewletmanager(IAddThis)

class Disqus(grok.Viewlet):
    grok.viewletmanager(IDisqus)

class MaybeYouLike(grok.Viewlet):
    grok.viewletmanager(IMaybeYouLike)

class GoogleAdResponsive(grok.Viewlet):
    grok.viewletmanager(IGoogleAdResponsive)

class FooterProductList(grok.Viewlet):
    grok.viewletmanager(IPortalFooter)

class GoogleAdInFooter(grok.Viewlet):
    grok.viewletmanager(IPortalFooter)
