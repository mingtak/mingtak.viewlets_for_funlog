from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from ..headerfootersetting import IHeaderFooterSetting
from plone.z3cform import layout
from z3c.form import form

class HeaderFooterControlPanel(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = IHeaderFooterSetting

HeaderFooterControlPanelView = layout.wrap_form(HeaderFooterControlPanel, ControlPanelFormWrapper)
HeaderFooterControlPanelView.label = u"Header and footer setting"
