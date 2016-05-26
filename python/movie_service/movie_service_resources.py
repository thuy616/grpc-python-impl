import json
import movie_service_pb2


def read_movie_service_database():
    movies_list = []
    with open("movie_service_db.json") as data:
        for item in json.load(data)["movies"]:
            movie = movie_service_pb2.Movie(
                adult=item["adult"],
                backdrop_path=item["backdrop_path"] if item["backdrop_path"] is not None else "",
                budget=item["budget"],
                genres=[],
                homepage=item["homepage"] if item["homepage"] is not None else "",
                id=item["id"],
                imdb_id=item["imdb_id"],
                original_language=item["original_language"],
                original_title=item["original_title"],
                overview=item["overview"],
                popularity=item["popularity"],
                poster_path=item["poster_path"] if item["poster_path"] is not None else "",
                production_companies=[],
                production_countries=[],
                release_date=item["release_date"],
                revenue=item["revenue"],
                runtime=item["runtime"],
                spoken_languages=[],
                status=item["status"],
                tagline=item["tagline"],
                title=item["title"],
                video=item["video"],
                vote_average=item["vote_average"],
                vote_count=item["vote_count"]
            )

            if item["belongs_to_collection"] is not None:
                c = movie.belongs_to_collection
                c.id = item["belongs_to_collection"]["id"]
                c.name = item["belongs_to_collection"]["name"]
                if item["belongs_to_collection"]["poster_path"] is not None:
                    c.poster_path = item["belongs_to_collection"]["poster_path"]
                if item["belongs_to_collection"]["backdrop_path"] is not None:
                    c.backdrop_path = item["belongs_to_collection"]["backdrop_path"]


            for genre in item["genres"]:
                g = movie.genres.add()
                g.id = genre["id"]
                g.name = genre["name"]

            for company in item["production_companies"]:
                c = movie.production_companies.add()
                c.name = company["name"]
                c.id = company["id"]

            for country in item["production_countries"]:
                c = movie.production_countries.add()
                c.iso_3166_1 = country["iso_3166_1"]
                c.name = country["name"]

            for language in item["spoken_languages"]:
                l = movie.spoken_languages.add()
                l.iso_639_1 = language["iso_639_1"]
                l.name = language["name"]

            movies_list.append(movie)
        data.close()

    return movies_list
