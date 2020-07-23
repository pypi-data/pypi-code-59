from django_common_utils.libraries.handlers import HandlerDefinitionType, HandlerMixin
from django_common_utils.libraries.handlers.mixins import WhiteSpaceStripHandler
from django_common_utils.libraries.models import TitleMixin


class Article(HandlerMixin, TitleMixin):
    @staticmethod
    def handlers() -> HandlerDefinitionType:
        return {
            "title": WhiteSpaceStripHandler
        }
