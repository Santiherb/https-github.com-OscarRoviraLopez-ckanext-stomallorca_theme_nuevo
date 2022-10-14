import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib.plugins import DefaultTranslation
from ckan.common import config
import ckan.lib.helpers as h

def default_locale():
    '''Wrap the ckan default locale in a helper function to access
    in templates.
    Returns 'en' by default.
    :rtype: string
    '''
    value = config.get('ckan.locale_default', 'en')
    return value

def stomallorca_portal_url():
    portal_url = config.get('ckanext.stomallorca_theme.portal_url', 'https://stomallorca.com/')
    if (h.lang() != 'es'):
      portal_url += h.lang() + '/'
    return portal_url

class StomallorcaThemePlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.ITranslation)
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "stomallorca_theme")

    # ITemplateHelpers
    def get_helpers(self):
        """
        Provide template helper functions
        """
        return {
            'extrafields_default_locale': default_locale,
            'stomallorca_portal_url': stomallorca_portal_url,
        }

