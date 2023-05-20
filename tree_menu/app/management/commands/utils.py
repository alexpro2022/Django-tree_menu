from django.db import IntegrityError


def info(func):
    def wrapper(self, *args, **options):
        self.stdout.write(f'= Loading {self.name} data =')
        try:
            func(self, *args, **options)
            self.stdout.write(self.style.SUCCESS(
                f'=== Successfully loaded: {self._class.objects.all()} ==='))
        except IntegrityError:
            self.stdout.write(
                f'== {self.name} data already exists ... exiting ==')
    return wrapper
