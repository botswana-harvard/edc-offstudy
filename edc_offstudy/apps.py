import sys

from django.apps import AppConfig as DjangoAppConfig
from django.apps import apps as django_apps


class EdcOffstudyAppConfigError(Exception):
    pass

ATTR = 0
MODEL_LABEL = 1


class AppConfig(DjangoAppConfig):
    name = 'edc_offstudy'
    # app_label = 'edc_example'
    verbose_name = 'Edc Offstudy'
    # offstudy_models = {'edc_example': ('subjectoffstudy', 'edc_example.subjectoffstudy')}

    def ready(self):
        from edc_offstudy.signals import off_study_post_save
        # sys.stdout.write('Loading {} ...\n'.format(self.verbose_name))
        # sys.stdout.write('  * using offstudy models from \'{}\'\n'.format(self.app_label))
        # sys.stdout.write(' Done loading {}.\n'.format(self.verbose_name))

#     def offstudy_model(self, app_label):
#         """Return the offstudy model for this app_label."""
#         try:
#             offstudy_model = django_apps.get_model(*self.offstudy_models[app_label][MODEL_LABEL].split('.'))
#         except LookupError as e:
#             raise EdcOffstudyAppConfigError(
#                 'Invalid offstudy model specified. See AppConfig for \'edc_offstudy\'. Got {}'.format(str(e)))
#         return offstudy_model