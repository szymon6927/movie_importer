from django.core.management.base import BaseCommand
from django.db import IntegrityError
import pandas as pd

from movies.utils.imdb import IMDBName, IMDBTitle
from movies.models import Title, Name


class Command(BaseCommand):
    help = 'Import data form .tsv files into DB'

    def add_arguments(self, parser):
        parser.add_argument('-n', '--names', type=str, help='Path to .tsv file with name data')
        parser.add_argument('-t', '--titles', type=str, help='Path to .tsc file with title data')

    def handle(self, *args, **options):
        names_file_path = options['names']
        titles_file_path = options['titles']

        titles_data = pd.read_csv(titles_file_path, sep='\t')
        names_data = pd.read_csv(names_file_path, sep='\t')

        for index, row in titles_data.iterrows():
            imdb_title = IMDBTitle(row)

            try:
                Title.objects.create(imdb_title_id=imdb_title.imdb_title_id, type=imdb_title.type,
                                     primary_title=imdb_title.primary_title, original_title=imdb_title.original_title,
                                     is_adult=imdb_title.is_adult, start_year=imdb_title.start_year,
                                     end_year=imdb_title.end_year, runtime_minutes=imdb_title.runtime_minutes,
                                     genres=imdb_title.genres)
            except IntegrityError:
                print("Object exist")

        for index, row in names_data.iterrows():
            imdb_name = IMDBName(row)

            try:
                name = Name.objects.create(imdb_name_id=imdb_name.imdb_name_id, primary_name=imdb_name.primary_name,
                                           birth_year=imdb_name.birth_year, death_year=imdb_name.death_year,
                                           primary_profession=imdb_name.primary_profession)
            except IntegrityError:
                print("Object exist")

            for title_id in imdb_name.known_for_titles:
                try:
                    title = Title.objects.get(imdb_title_id=title_id)

                    title.author = name
                    title.save()
                except Title.DoesNotExist:
                    print(f'Title with {title_id} id does not exist')

        self.stdout.write(self.style.SUCCESS("Successfully imported data"))
