import media
import os
import fresh_tomatoes
thor_ragnarok = media.Movie("Thor Ragnarok",
                            "Imprisoned on the other side of the universe, the mighty Thor finds himself in a deadly gladiatorial contest that pits him against the Hulk, his former ally and fellow Avenger. Thor's quest for survival leads him in a race against time to prevent the all-powerful Hela from destroying his home world and the Asgardian civilization.",
                            "https://in.bmscdn.com/iedb/movies/images/website/poster/large/thor-ragnarok-et00028937-17-04-2017-17-54-12.jpg",                    
                            "https://www.youtube.com/watch?v=ue80QwXMRHg"
                            )
#print(thor_ragnarok.story_line)
#thor_ragnarok.show_trailer()
black_panther = media.Movie("Black Panther",
                            "Black Panther (Chadwick Boseman) springs into action when an old enemy threatens the fate of his nation and the world.",
                            "http://cdn2-www.superherohype.com/assets/uploads/gallery/black-panther_1/blackpantherposter.jpg",
                            "https://www.youtube.com/watch?v=dxWvtMOGAhw"
                            )






movies = [thor_ragnarok,black_panther]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.valid_ratings)
