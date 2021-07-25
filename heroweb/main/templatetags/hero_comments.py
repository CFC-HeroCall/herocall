from django import template
from main.models import Tab
from django.utils.html import format_html

register = template.Library()

@register.filter
def org_replies(replies, tab_id):
    i = 0
    views = []
    for reply in replies:
        if reply.reply_tab == tab_id:
            if i % 3 == 0:
                views.append([reply])
            else:
                views[len(views)-1].append(reply)
            i += 1
    return views

@register.simple_tag
def get_tabs(post):
    response = ''
    tabs = Tab.objects.all().filter(post=post)
    for tab in tabs:
        response += f'<option value="{tab.id}">{tab.title}</option>'

    return format_html(response)