from app.models import MenuItem
from django import template
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.inclusion_tag('app/menu.html')
def draw_menu(menu_name: str = None):
    items = MenuItem.objects.all()

    def get_menu(menu_name: str = None, submenu: list = None):
        menu = list(items.filter(parent=None)) if menu_name is None \
            else list(items.filter(parent__name=menu_name))
        try:
            menu.insert(menu.index(submenu[0].parent) + 1, submenu)
        except (IndexError, TypeError):
            pass
        try:
            return get_menu(items.get(name=menu_name).parent.name, menu)
        except AttributeError:
            return get_menu(submenu=menu)
        except ObjectDoesNotExist:
            return menu

    if menu_name == 'main':
        return {'menu': get_menu()}
    return {'menu': get_menu(menu_name)}
