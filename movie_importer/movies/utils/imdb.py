class IMDBName:
    def __init__(self, data):
        self.data = data

    @property
    def imdb_name_id(self):
        return self.data['nconst']

    @property
    def primary_name(self):
        return self.data['primaryName']

    @property
    def birth_year(self):
        return int(self.data['birthYear']) if self.data['birthYear'] != "\\N" else None

    @property
    def death_year(self):
        return int(self.data['deathYear']) if self.data['birthYear'] != "\\N" else None

    @property
    def primary_profession(self):
        return self.data['primaryProfession']

    @property
    def known_for_titles(self):
        return self.data['knownForTitles']


class IMDBTitle:
    def __init__(self, data):
        self.data = data

    @property
    def imdb_title_id(self):
        return self.data['tconst']

    @property
    def type(self):
        return self.data['titleType']

    @property
    def primary_title(self):
        return self.data['primaryTitle']

    @property
    def original_title(self):
        return self.data['originalTitle']

    @property
    def is_adult(self):
        return self.data['isAdult'] == 1

    @property
    def start_year(self):
        return self.data['startYear']

    @property
    def end_year(self):
        return int(self.data['endYear']) if self.data['endYear'] != "\\N" else None

    @property
    def runtime_minutes(self):
        return self.data['runtimeMinutes']

    @property
    def genres(self):
        return self.data['genres']
