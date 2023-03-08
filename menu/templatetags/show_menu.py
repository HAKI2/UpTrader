from django import template
from menu.models import MenuNode, MenuNodeTree
from django.utils.html import escape, mark_safe

register = template.Library()


@register.inclusion_tag('menu_sublist.html', takes_context=True)
def show_menu(context, name):
    ancestor = context['request'].GET.get('anc', '')
    level = context['request'].GET.get('level', '')
    menu = context['request'].GET.get('menu', '')
    first_menu_node = MenuNode.objects.filter(name=name).first()
    queryset = MenuNodeTree.objects.filter(ancestor=first_menu_node).order_by('nearestAncestor_id', 'level')
    if menu and first_menu_node.id == int(menu):
        if level:
            queryset = queryset.filter(level__lte=int(level) + 1)
        queryset = queryset.select_related('descendant').all()
        res = []
        for mn in queryset:
            if mn.level <= int(level):
                res.append(mn)
            elif ancestor and mn.nearestAncestor_id == int(ancestor):
                res.append(mn)
            print(res)
        return {'iterator': res}
    else:
        queryset = queryset.filter(level__lte=1).all()
        return {'iterator': queryset}


@register.simple_tag()
def render_ul(url, item):
    res = []
    for i in range(item.level):
        res.append('<ul>')
    res.append(
        f'<a href={url}?anc={str(item.descendant_id)}&level={str(item.level)}&menu={item.ancestor_id}>{item.descendant.name}</a>')
    for i in range(item.level):
        res.append('</ul>')
    return mark_safe(''.join(res))
