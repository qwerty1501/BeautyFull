from modeltranslation.translator import translator, TranslationOptions
from .models import Master, Services, Request


class MasterTranslationOptions(TranslationOptions):
    fields = ('name', 'information', 'experience', 'position')


class ServicesTranslationOptions(TranslationOptions):
    fields = ('title',)


class RequestTranslationOptions(TranslationOptions):
    fields = ('master', 'time', 'date', 'service', 'name', 'sms')


translator.register(Master, MasterTranslationOptions)
translator.register(Services, ServicesTranslationOptions)
translator.register(Request, RequestTranslationOptions)

