from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils.dateparse import parse_date
from app.models import Title, StreamingPlatform
import csv
import os

class Command(BaseCommand):
    help = 'Imports data from CSV files for Netflix, Disney+, and Amazon Prime into the database'

    def handle(self, *args, **options):
        # Mapping platform names to their respective CSV file names
        platform_files = {
            'Netflix': 'netflix_titles.csv',
            'Disney+': 'disney_plus_titles.csv',
            'Amazon Prime': 'amazon_prime_titles.csv'
        }

        platforms = {name: StreamingPlatform.objects.get_or_create(name=name)[0] for name in platform_files.keys()}

        # Loop through each platform and import the corresponding CSV file
        for platform_name, csv_filename in platform_files.items():
            # Construct the full path to the CSV file
            file_path = os.path.join(settings.BASE_DIR, 'app/data', csv_filename)

            try:
                with open(file_path, newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        title, created = Title.objects.update_or_create(
                            show_id=row['show_id'],
                            platform=platforms[platform_name],
                            defaults={
                                'type': row['type'],
                                'title': row['title'],
                                'director': row.get('director', ''),
                                'cast': row.get('cast', ''),
                                'country': row.get('country', ''),
                                'date_added': parse_date(row['date_added']) if row['date_added'] else None,
                                'release_year': int(row['release_year']),
                                'rating': row.get('rating', ''),
                                'duration': row['duration'],
                            }
                        )
            except FileNotFoundError:
                raise CommandError(f"File {file_path} does not exist")

            self.stdout.write(self.style.SUCCESS(f'Successfully imported data from {file_path}'))
