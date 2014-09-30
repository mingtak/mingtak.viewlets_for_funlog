from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from ..promotionsetting import IPromotionSetting
from plone.z3cform import layout
from z3c.form import form

class PromotionSettingControlPanel(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = IPromotionSetting

PromotionSettingControlPanelView = layout.wrap_form(PromotionSettingControlPanel, ControlPanelFormWrapper)
PromotionSettingControlPanelView.label = u"Promotional product list setting"
