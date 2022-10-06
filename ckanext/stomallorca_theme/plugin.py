import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib.plugins import DefaultTranslation
from ckan.common import config

def default_locale():
    '''Wrap the ckan default locale in a helper function to access
    in templates.
    Returns 'en' by default.
    :rtype: string
    '''
    value = config.get('ckan.locale_default', 'en')
    return value

class StomallorcaThemePlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.ITranslation)
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
#    plugins.implements(plugins.IPackageController)

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
        }

    # IPackageController
    def before_index(self, data_dict):
        titles = json.loads(data_dict.get('title_translated', '{}'))
        data_dict['title_ca'] = titles.get('ca', '')
        data_dict['title_en'] = titles.get('en', '')
        data_dict['title_string'] = titles.get('es', '')

    def read(self, entity):
        pass

    def create(self, entity):
        pass

    def edit(self, entity):
        pass

    def delete(self, entity):
        pass

    def before_search(self, search_params):
        pass

