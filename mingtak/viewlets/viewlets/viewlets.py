from zope.interface import Interface
from five import grok
from plone.app.layout.viewlets.interfaces import IPortalHeader, IAboveContent, IBelowContentBody
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.contenttypes.interfaces import IImage

# viewlet nameing format: ContentType_Position_ViewletFunction
class IImage_IAboveContent_ResponsiveAd(grok.Viewlet):
    grok.viewletmanager(IAboveContent)
    grok.context(IImage)
    template = ViewPageTemplateFile('templates/responsivead.pt')

    def render(self):
        return self.template()


class All_IBelowContentBody_TopBanner(grok.Viewlet):
    grok.viewletmanager(IBelowContentBody)
    grok.context(Interface)
    template = ViewPageTemplateFile('templates/topbanner.pt')

    def render(self):
        return self.template()
