import sys,os,json

def verify_entry(entry: dict[str,str])->bool:
    return entry.keys() == {'_id','cast','year','genres','title'}
def main(argv : list[str])->None:
    data = json.loads(open(argv[1],'r').read())
    for movie in data:
        try:
            (movie["genres"])
        except KeyError:
            movie["genres"] = []
        movie["id"] = movie["_id"]["$oid"]
        movie.pop("_id")

    actors = {actor for movie in data for actor in movie['cast'] if verify_entry(movie)}
    genres = {genre for movie in data for genre in movie['genres'] if verify_entry(movie)}

    json.dump({
        "movies": data,
        "actors": [{"id":i,"name" : actor} for i,actor in enumerate(actors)],
        "genres": [{"id":i,"genre" : genre} for i,genre in enumerate( genres)]
        },open(argv[1].split('/')[0]+'/data.json','w+'))

    
if __name__ == '__main__':
    main(sys.argv)