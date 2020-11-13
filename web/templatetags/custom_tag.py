from django import template

register = template.Library()

@register.filter
def title_slice(title):
	if len(title) > 28:
		title = title[:28] + '...'
		return title
	else :
		return title
