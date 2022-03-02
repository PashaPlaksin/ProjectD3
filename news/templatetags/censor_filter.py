from django import template
from flashtext import KeywordProcessor

register = template.Library()


@register.filter(name='censor')
def censor(value):
    keyword_processor = KeywordProcessor(case_sensitive=True)

    keyword_processor.add_keyword("Коронавирус", "COVID")
    text = KeywordProcessor.replace_keywords(keyword_processor,value)

    return text
