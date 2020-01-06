movies = {
                 "Lost Ark": [10,3],
                 "Star Wars": [10,3],
                 "Buster Scruggs": [18,3],
                 "Nemo": [10,3],
                 "Miami Vice": [18,3],
                 "Bat Man": [18,3]
                }
while True:

     choice = input("What movie would you like to watch?: ").strip().title()
     if choice in movies:
              age = int(input("What is your age?: ").strip())
              if age >= movies[choice][0]:
                 num_seats = movies[choice][1]
                 if num_seats > 0:
                        print("Enjoy the movie!")
                        movies[choice][1] = movies[choice][1] -1
                 else:
                      print("Sorry we are sold out at this time, please try later!")
              else:
                      print("Sorry you are not old enough to see this movie!")
     else:
               print("Sorry we don't have that movie!")
