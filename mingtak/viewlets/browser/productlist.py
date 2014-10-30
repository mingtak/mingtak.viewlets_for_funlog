# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import logging
#from plone import api
from random import shuffle


logger = logging.getLogger("productlist.py")


class ProductList(BrowserView):

    template = ViewPageTemplateFile('template/productlist.pt')

    def __call__(self):
        request = self.request
        context = self.context
        catalog = context.portal_catalog
        self.brain = catalog({"portal_type":"cj.product.cjproduct",
                              "Subject":request["catalog"],}, sort_on="modified", sort_order="reverse")
        return self.template()
