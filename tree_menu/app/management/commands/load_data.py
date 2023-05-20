from django.core.management import BaseCommand

from app.models import MenuItem
from . utils import info


class Command(BaseCommand):
    _class = MenuItem
    name = 'MENU'

    @info
    def handle(self, *args, **kwargs):
        size = 5
        for i in range(size):
            level = f'level-{i+1}'
            main_menu = self._class.objects.create(name=level)
            for j in range(size):
                sublevel = f'{level} sublevel-{j+1}'
                submenu = self._class.objects.create(
                    name=sublevel, parent=main_menu)
                for k in range(size):
                    subsublevel = f'{sublevel} sub-sublevel-{k+1}\n'
                    self._class.objects.create(
                        name=subsublevel, parent=submenu)
