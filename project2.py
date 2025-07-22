import csv

movies = [["John Wick: Chapter 4", "action", 7.6], 
        ["Cars 2", "family", 6.2], 
        ["Parasite", "thriller", 8.5],
        ["Avengers: Endgame", "action", 8.4]]

#stage 1 
'''
# #stage 1
# movies = [["John Wick: Chapter 4", "action", 7.6], 
#         ["Cars 2", "family", 6.2], 
#         ["Parasite", "thriller", 8.5],
#         ["Avengers: Endgame", "action", 8.4]]
# #print(movies[0][0])
# #movies([2][1]) = "Thriller/Comedy"
# movies.append(["Mission: Impossible", "thriller", 7.2])
'''

#bonus from stage 1 
'''
#bonus from day 1
# prompts = ["Please enter the movie title: ",
#           "Please enter the movie genre: ",
#           "Please enter the movie rating(1-10): "]
# inputs = []
# for i in range(len(prompts)):
#     if i <= 2:
#         inputs.append((input(prompts[i])))
#     else:
#         inputs.append((int(input(prompts[i]))))
# movies.append(inputs)

# print("--------------------------------------------------------------")
# for i in range(len(movies)):
#     print(movies[i])
'''

#stage 1 continued
'''
#stage one continued
#1.2
for i in range(len(movies)):
    if movies[i][2] >= 8:
        print("Great movie!")
    elif movies[i][2] > 5 and movies[i][2] < 7.9:
        print("Okay movie.")
    else:
        print("Not worth watching.")
#1.3
for i in range(len(movies)):
    print("Title:", movies[i][0])

ratings_sum = 0
for i in range(len(movies)):
    ratings_sum = ratings_sum + movies[i][2]
print("Sum of ratings:", ratings_sum)


#1.4
for i in range(len(movies)):
    print("'" + movies[i][0] + "'" + ":", movies[i][2])
'''

#stage 2
'''
#stage 2
def calculate_average_rating(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i][2]
    print("Average rating:", round(sum/len(list), 3))



def find_highest_rating(list):
    count = 0
    for i in range(len(list)):
        if list[i][2] > count:
            count = list[i][2]
    print("Highest rating:", count)



def filter_by_genre(list):
    filter_genre_movies = []
    filter_input = input("Please select the genre you would like to filter by: ")
    for i in range(len(list)):
        if list[i][1] == filter_input.lower():
            filter_genre_movies.append(list[i][0])

    for i in range(len(filter_genre_movies)):
        print(filter_input.capitalize() + ":", "'" + filter_genre_movies[i] + "'")



calculate_average_rating(movies)
find_highest_rating(movies)
#filter_by_genre(movies)
'''


#=================================================================================================================



#stage 3
headers = []
rows = []


#functions
def load_movies(filename):

    with open(filename, "r", encoding='utf-8') as file:
        reader = csv.reader(file)

        headers = next(reader)

        for x in reader:
            rows.append(x)
    #print(headers)
    #print(rows)


def calculate_average_rating(my_list):
    sum = 0
    for i in range(len(my_list)):
        if my_list[i][6] != '':
            sum = sum + float(my_list[i][6])
    
    avg = round(sum/len(my_list), 3)
    return avg


def find_highest_rating(my_list):
    count = 0
    best_title = " "
    for i in range(len(my_list)):
        if my_list[i][6] != '':
            if float(my_list[i][6]) > count:
                count = float(my_list[i][6])
                best_title = my_list[i][1]
    return count, best_title


def print_titles(my_list):
    for i in range(len(my_list)):
        print(my_list[i][1])


def movies_by_year(my_list):
    year_movies = []
    year_input = input("Please select the year you would like to filter by: ")
    for i in range(len(my_list)):
        if my_list[i][2] == year_input:
            year_movies.append(my_list[i][1])
    return year_input, year_movies


def movies_by_genre(my_list):
    genre_movies = []
    genre_input = input("Please select the genre you would like to filter by: ")
    for i in range(len(my_list)):
        if genre_input.capitalize() in my_list[i][5]:
            genre_movies.append(my_list[i][1])
    return genre_input, genre_movies


def find_movie(my_list):
    movie_data = []
    movie_input = input("Please enter the title of the movie you would like to find: ")
    for i in range(len(my_list)):
        if movie_input.lower() == my_list[i][1].lower():
            for j in range(len(my_list[i])):
                movie_data.append(my_list[i][j])
    return movie_input, movie_data


def save_analysis(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    print("Check the .txt file for your results!")




#load movies
load_movies("animation.csv")

#arrays that store stuff
saved_prompts = ["Average rating (A)",
    "Highest rating (B)",
    "Filter by year (C)",
    "Filter by genre (D)",
    "Movie finder (E)"
]
active_prompts = []
analysis_lines = []

#add prompts
for i in range(len(saved_prompts)):
    active_prompts.append(saved_prompts[i])





while True:
    #if all prompts/ tasks were performed
    if not active_prompts:
        print("--------------------------------------------")
        print("No more tasks available to perform.")
        break

    # load prompts
    print("--------------------------------------------")
    for i in range(len(active_prompts)):
        print(active_prompts[i])

    #input 
    big_input = input("Please select the task you would like to perform, enter STOP to see your results: ")

    #different scenarios 
    if big_input.upper() == "A":
        average_rating = calculate_average_rating(rows)
        analysis_lines.append(f"Average rating: {average_rating}\n\n")
        active_prompts.remove("Average rating (A)")

    elif big_input.upper() == "B":
        highest_rating, best_title = find_highest_rating(rows)
        analysis_lines.append(f"Highest rating: {highest_rating}  ('{best_title}')\n\n")
        active_prompts.remove("Highest rating (B)")

    elif big_input.upper() == "C":
        year, year_results = movies_by_year(rows)
        analysis_lines.append(f"Movies released in {year} ({len(year_results)} total):\n"
        + "\n".join(f"  - {x}" for x in year_results) + "\n\n\n")
        active_prompts.remove("Filter by year (C)")

    elif big_input.upper() == "D":
        genre, genre_results = movies_by_genre(rows)
        analysis_lines.append(f"{genre.capitalize()} movies ({len(genre_results)} total):\n"
        + "\n".join(f"  - {x}" for x in genre_results) + "\n\n\n")
        active_prompts.remove("Filter by genre (D)")

    elif big_input.upper() == "E":
        name, stats = find_movie(rows)
        analysis_lines.append(f" '{name.title()}' stats:\n"
        + "\n".join(f"  - {x}" for x in stats))
        active_prompts.remove("Movie finder (E)")

    elif big_input.upper() == "STOP":
        break

    else:
        print("Invalid choice")





#need, turn array back into a text block able to be used in save_analysis()
analysis_text = "\n".join(analysis_lines) + "\n"


#export results to text file
save_analysis(analysis_text, "Project_2_Analysis.txt")
