# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def IMDBabove(string):
    for i in movies:
        if i["name"] == string:
            if i["imdb"] > 5.5:
                return True
    return False

print(IMDBabove("We Two"))


def IMDBlist():
    goodmovies = []
    for i in movies:
        if i["imdb"] > 5.5:
            goodmovies.append(i)
    return goodmovies

print(IMDBlist())


def Category(str):
    categorymovies = []
    for i in movies:
        if i["category"] == str:
            categorymovies.append(i)
    return categorymovies

print(Category("Romance"))


def Average(list):
    cnt = 0
    for i in list:
        for j in movies:
            if j["name"] == i:
                cnt+=j["imdb"]
                break
    return float(cnt/len(list))
        
        
print(Average(["Dark Knight","Exam","Detective","AlphaJet","Usual Suspects"]))


def CategoryAverage(str):
    cnt = 0
    num = 0
    for i in movies:
        if i["category"] == str:
            cnt+=i["imdb"]
            num+=1
    return float(cnt/num)

print(CategoryAverage("Romance"))