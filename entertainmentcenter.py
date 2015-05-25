import media
import fresh_tomatoes


# Create the instances of Movie class for different movies

toy_story = media.Movie("Toy Story",
                        "A story of boy and toys",
                        "http://www.impawards.com/1995/posters/toy_story_ver1.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

lawrense_arabia = media.Movie("Lawrence of Arabia",
                              "Story about Lawrence in arabia",
                              "http://www.impawards.com/1962/posters/lawrence_of_arabia_ver4_xlg.jpg",
                              "https://www.youtube.com/watch?v=zmr1iSG3RTA")


godfather = media.Movie("God Father",
                              "Story of a mob family",
                              "http://www.moviepostershop.com/the-godfather-movie-poster-1020243893.jpg",
                              "https://www.youtube.com/watch?v=sY1S34973zA")


gunsofnavarone = media.Movie("Guns of Navarone",
                              "WorldWar 2 story",
                              "http://meansheets.files.wordpress.com/2010/01/guns-of-navarone.jpg",
                              "https://www.youtube.com/watch?v=MhQvkPMNt70")


gravity = media.Movie("Gravity",
                              "Story about space",
                              "http://www.impawards.com/2013/posters/gravity.jpg",
                              "https://www.youtube.com/watch?v=OiTiKOy59o4")



starwars = media.Movie("Star Wars",
                              "Story about good vs evil",
                              "http://www.impawards.com/1999/posters/star_wars_episode_one_the_phantom_menace_ver2.jpg",
                              "https://www.youtube.com/watch?v=I6hOlI9cg4o")


lordoftherings = media.Movie("Lord of the Rings",
                              "Story about the ring",
                              "http://images.moviepostershop.com/lord-of-the-rings---trilogy-movie-poster-2003-1020187968.jpg",
                              "https://www.youtube.com/watch?v=Pki6jbSbXIY")


#Initialize the list of movies to pass to the fresh tomatoes python program
movies = [toy_story,lawrense_arabia,godfather,gunsofnavarone,gravity,starwars,lordoftherings]

#Invoke the method in fresh tomatoes to display the html page with the list of movies
#The html page will be opened in the browser.
fresh_tomatoes.open_movies_page(movies)
