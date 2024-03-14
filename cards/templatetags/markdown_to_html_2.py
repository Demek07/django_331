from django import template

# в Django это регистрация библиотеки шаблонов, которая позволяет использовать пользовательские теги
# и фильтры в шаблонах Django.
register = template.Library()


# @register это декоратор, который используется в Django для создания простых пользовательских тегов шаблонов.
# @register.inclusion_tag - это декоратор, который используется для создания пользовательских тегов шаблонов,
# которые включают шаблон в шаблон.
@register.inclusion_tag('templates/include/markdown_to_html_tag.html', takes_context=True)
def markdown_to_html2(markdown_text: str) -> str:
    return {'markdown_text': markdown_text.upper() + ' - это тестовый текст'}
