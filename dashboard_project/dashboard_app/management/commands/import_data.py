import json
from django.core.management.base import BaseCommand
from dashboard_app.models import Data

class Command(BaseCommand):
    help = 'Import data from JSON file'

    def handle(self, *args, **kwargs):
        # with open('C:/Users/hp/Desktop/New folder/project8/dashboard_project/dashboard_app/management/commands/data.json') as f:
        with open('C:/Users/hp/Desktop/New folder/project8/dashboard_project/dashboard_app/management/commands/data.json', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                if item['start_year'] and item['country']:
                    d = Data(
                        intensity=item['intensity'],
                        likelihood=item['likelihood'],
                        relevance=item['relevance'],
                        start_year=item['start_year'],
                        end_year=item['end_year'],
                        country=item['country'],
                        topic=item['topic'],
                        region=item['region'],
                    )
                    d.save()
        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))
