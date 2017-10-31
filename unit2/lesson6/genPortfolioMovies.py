import pyperclip
moviesList = []

with open('movies.csv', 'r', encoding='utf-8') as movies:
	for line in movies:
		try:
			line = line.strip()
			line = line.split(',')
			movie = line[1]
			print(movie)
			if movie[0] == '\"':
				movie = movie[1:-1]
			moviesList.append(movie)
		except:
			pass

pyperclip.copy(str(moviesList))