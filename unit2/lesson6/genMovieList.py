count = 0

word = ''

# Pre-processing
word = word.lower()
word = '' + word + ''

with open('movies.csv', 'r', encoding='utf-8') as movies:
	for line in movies:
		line = line.strip()
		line = line.split(',')
		try:
			movie = line[1]
			movie = ' ' + movie + ' '
			if word in movie.lower():
				movie = movie[1:-1]
				print(movie)
				count += 1
		except:
			pass

print('')
print(count)