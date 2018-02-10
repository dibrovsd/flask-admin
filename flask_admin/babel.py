from flask_babel import gettext, ngettext, lazy_gettext
from flask_admin import translations


class Translations(object):
    ''' Fixes WTForms translation support and uses wtforms translations '''
    def gettext(self, string):
        return gettext(string)

    def ngettext(self, singular, plural, n):
        return ngettext(singular, plural, n)


from .helpers import get_current_view
