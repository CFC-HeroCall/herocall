from django import template

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

@register.filter
def get_replies(replies, post_id):
    i = 0
    views = []
    for reply in replies:
        if reply.reply_post == post_id:
            if i % 3 == 0:
                views.append([reply])
            else:
                views[len(views)-1].append(reply)
            i += 1
    return views