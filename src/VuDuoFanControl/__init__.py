from gettext import bindtextdomain, dgettext, gettext
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS

PluginLanguageDomain = "FanControl"
PluginLanguagePath = "SystemPlugins/FanControl/locale"


def locale_init():
	bindtextdomain(PluginLanguageDomain, resolveFilename(SCOPE_PLUGINS, PluginLanguagePath))


def _(txt):
	if gettext.dgettext(PluginLanguageDomain, txt):
		return dgettext(PluginLanguageDomain, txt)
	else:
		print(f"[{PluginLanguageDomain}] fallback to default translation for {txt}")
		return gettext(txt)


locale_init()
language.addCallback(locale_init)

__version__ = "1.1"
