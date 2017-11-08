import pyperclip

class Movie(object):
	def __init__(self,title,genres):
		self.title = title
		self.genres = genres

def genMovieDict():
	moviesDict = []
	with open('movies.csv', 'r', encoding='utf-8') as movies:
		for line in movies:
			try:
				line = line.strip()
				line = line.split(',')
				title = line[1]
				genres = line[2].split('|')
				movie = Movie(title,genres)
				movie = {'title' : movie.title, 'genres' : movie.genres}
				#print(movie)
				moviesDict.append(movie)
			except:
				pass
	return moviesDict

def queryDict(word, moviesDict):
	count = 0
	for movie in moviesDict:
		try:
			if word in movie['genres']:
				print(movie['title'])
				count += 1
		except:
			pass
	print('\nThere are {} {} movies in the list.'.format(count,word))

def getGenres(moviesDict):
	genres = set()
	for movie in moviesDict:
		try: 
			# print(set(movie['genres']))
			movieSet = set(movie['genres'])
			genres = genres.union(movieSet)
			print(genres)
		except:
			pass
	try:
		for genre in genres:
			print(genre)
	except:
		pass

moviesDict = genMovieDict()
queryDict('Sci-Fi',moviesDict)
# getGenres(moviesDict)



