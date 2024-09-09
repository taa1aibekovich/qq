from .models import *
from modeltranslation.translator import TranslationOptions,register


#
@register(Faculty)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Professor)
class ProductTranslationOptions(TranslationOptions):
    fields = ('professor_name', 'title')



@register(Course)
class ProductTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')



