import csv
from restaurants.models import Restaurant
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = 'Load data into Restaurant model from a given csv file'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)


    def handle(self, *args, **options):
        with open(options['path']) as f:
            reader = csv.DictReader(f)
            for row in reader:
                _, created = Restaurant.objects.get_or_create(
                    id=row['id'],
                    rating=row['rating'],
                    name=row['name'],
                    site=row['site'],
                    email=row['email'],
                    phone=row['phone'],
                    street=row['street'],
                    city=row['city'],
                    state=row['state'],
                    lat=row['lat'],
                    lng=row['lng']
                )
                # creates a tuple of the new object or
                # current object and a boolean of if it was created

            self.stdout.write(self.style.SUCCESS('Successfully write data into model'))
