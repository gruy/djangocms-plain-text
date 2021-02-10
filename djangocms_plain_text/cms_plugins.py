from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import PlainText


@plugin_pool.register_plugin
class PlainTextPlugin(CMSPluginBase):
    cache = False
    model = PlainText
    name = _('Plain Text')
    render_template = 'djangocms_plain_text/text.html'
    text_enabled = True

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context
