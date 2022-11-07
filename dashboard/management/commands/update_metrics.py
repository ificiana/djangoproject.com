from django.core.management import BaseCommand

from ...models import Metric
from ...utils import reset_generation_key


class Command(BaseCommand):
    def handle(self, **options):
        verbose = int(options.get('verbosity', 0))
        for MC in Metric.__subclasses__():
            for metric in MC.objects.all():
                if verbose:
                    self.stdout.write(f"Updating {metric.name.lower()} ... ", ending="")
                if verbose:
                    datum = metric.data.create(measurement=metric.fetch())
                    print(datum.measurement)
        reset_generation_key()
