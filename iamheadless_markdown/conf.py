from django.conf import settings as dj_settings

from .apps import IamheadlessMarkdownConfig as AppConfig
from .loader import load


class Settings:

    _WIDGET_REGISTRY = None

    APP_NAME = AppConfig.name
    VAR_PREFIX = APP_NAME.upper()

    VAR_WIDGET_REGISTRY_CLASS = f'{VAR_PREFIX}_WIDGET_REGISTRY_CLASS'
    VAR_WIDGETS_LIST = f'{VAR_PREFIX}_WIDGETS_LIST'
    VAR_WIDGETS_LIST_EXTENSION = f'{VAR_PREFIX}_WIDGETS_LIST_EXTENSION'

    @property
    def WIDGETS_LIST(self):

        return getattr(
            dj_settings,
            self.VAR_WIDGETS_LIST,
            [
                f'{self.APP_NAME}.widgets.HeadingH1',
                f'{self.APP_NAME}.widgets.HeadingH2',
                f'{self.APP_NAME}.widgets.HeadingH3',
                f'{self.APP_NAME}.widgets.HeadingH4',
                f'{self.APP_NAME}.widgets.HorizontalRule',
                f'{self.APP_NAME}.widgets.Image',
                f'{self.APP_NAME}.widgets.UnorderedListElement',
                f'{self.APP_NAME}.widgets.OrderedListElement',
                f'{self.APP_NAME}.widgets.Paragraph',
            ],
        )

    @property
    def WIDGETS_LIST_EXTENSION(self):
        return getattr(
            dj_settings,
            self.VAR_WIDGETS_LIST_EXTENSION,
            [],
        )

    @property
    def WIDGET_REGISTRY(self):
        if self._WIDGET_REGISTRY is not None:
            return self._WIDGET_REGISTRY
        self._WIDGET_REGISTRY = load(self.WIDGET_REGISTRY_CLASS)()
        return self._WIDGET_REGISTRY

    @property
    def WIDGET_REGISTRY_CLASS(self):
        return getattr(
            dj_settings,
            self.VAR_WIDGET_REGISTRY_CLASS,
            f'{self.APP_NAME}.registry.MarkdownWidgetRegistry',
        )

    def __getattr__(self, name):
        return getattr(dj_settings, name)


settings = Settings()
