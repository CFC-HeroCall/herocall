from django import template
from main.models import Tab
from django.utils.html import format_html
from markdown import markdown

register = template.Library()

@register.filter
def org_replies(replies, tab_id):
    i = 0
    views = []
    for reply in replies:
        if reply.reply_tab == tab_id:
            if i % 2 == 0:
                views.append([reply])
            else:
                views[len(views)-1].append(reply)
            i += 1
    return views

@register.filter
def markdown_parse(text):
    # parsed = markdown(text)
    # print(parsed)
    return text

@register.simple_tag
def get_tabs(post):
    response = "<select class='form-select' onchange='select_tab(this)'><option selected>Select tab</options>"
    tabs = Tab.objects.all().filter(post=post)

    if len(tabs) == 0:
        return ""

    for tab in tabs:
        response += f'<option value="rtab_{tab.id}">{tab.title}</option>'
    response += "</select>"
    return format_html(response)