# import statements
import unittest
import json
import requests
import pickle
#list of Tv Shows
tvShows=["Last Week Tonight with John Oliver", "firefly", "It's Always Sunny in Philadelphia",  "Game of Thrones", "The Sopranos", "Seinfeld", "Sherlock", "Dexter", "Nathan for you", "Mad Men", "Parks and Recreation", "John Adams", "Atlanta", "Late Night with Conan O'Brien", "The Daily Show", "The Colbert Report", "The Thick of It", "Battlestar Galactica", "Anger Management", "Late Night with Seth Meyers", "Banshee", "Top Gear", "Pride and Prejudice", "Modern Family", "Spartacus: War of the Damned", "Suits", "The Office", "Bates Motel", "Hannibal", "IZombie", "Mr. Robot", "The X-Files"]

cache_fname = "cached_emotion_results.txt"
try:
    fobj = open(cache_fname, 'r')
    saved_cache = pickle.load(fobj)
    fobj.close()
except:
    saved_cache = {}

def get_emotion_with_caching(img_url, cache_diction, cache_fname, maxNumRetries = 10, data = None, params = None):
    if img_url in cache_diction:
        return cache_diction[img_url]
    else:
        _url = 'https://api.projectoxford.ai/emotion/v1.0/recognize'
        _key = '662c62d274804b1187f2db523d5b0d8b'        
        headers = dict()
        headers['Ocp-Apim-Subscription-Key'] = _key
        headers['Content-Type'] = 'application/json' 
        json = { 'url': img_url } 
        response = requests.request( 'post', _url, json = json, data = data, headers = headers, params = params )
        cache_diction[img_url] = response.text
        fobj = open(cache_fname, "w")
        pickle.dump(cache_diction, fobj)
        fobj.close()
        return response.text

class tvShow():
    def __init__(this, d):
        this.title = d['Title']
        this.imdbRating = d['imdbRating']
        this.Genre = d['Genre']
        this.PosterUrl = d['Poster']

cache_Iname = "cached_imdb_results.txt"
try:
    Iobj = open(cache_Iname, 'r')
    saved_imdb_cache = pickle.load(Iobj)
    Iobj.close()
except:
    saved_imdb_cache = {}

def canonical_order(d):
    alphabetized_keys = sorted(d.keys())
    res = []
    for k in alphabetized_keys:
        res.append((k, d[k]))
    return res

def requestURL(baseurl, params = {}):
    req = requests.Request(method = 'GET', url = baseurl, params = canonical_order(params))
    prepped = req.prepare()
    return prepped.url

def get_imdb_with_caching(params_diction ,cache_diction, cache_Iname):
    base_url = 'http://www.omdbapi.com/'
    full_url = requestURL(base_url, params_diction)
    if full_url in cache_diction:
        return cache_diction[full_url]
    else:
        response = requests.get(base_url, params=params_diction)
        cache_diction[full_url] = response.text
        Iobj = open(cache_Iname, "w")
        pickle.dump(cache_diction, Iobj)
        Iobj.close()
        return response.text

tvShow_instances = []
for i in tvShows:
    d = dict(
    apikey='475999e3',
    t=i,
    r='jsons',
    )
    result = get_imdb_with_caching(d, saved_imdb_cache, cache_Iname)
    result = json.loads(result) 
    newtvShow = tvShow(result)
    tvShow_instances.append(newtvShow)

class TvEmotion():
    def __init__(this, title, genre, d, imdbRating, PosterUrl):
        this.title = title
        this.imdbRating = imdbRating
        this.genre = genre
        this.posterUrl = PosterUrl
        this.sadness = d[0]['scores']['sadness']
        this.d = d
        this.sadnessList=[]
        [this.sadnessList.append(n['scores']['sadness']) for n in this.d]
        this.happinessList=[]
        [this.happinessList.append(n['scores']['happiness']) for n in this.d]
        this.angerList=[]
        [this.angerList.append(n['scores']['anger']) for n in this.d]
        this.contemptList=[]
        [this.contemptList.append(n['scores']['contempt']) for n in this.d]
        this.disgustList=[]
        [this.disgustList.append(n['scores']['disgust']) for n in this.d]     
        this.fearList=[]
        [this.fearList.append(n['scores']['fear']) for n in this.d]     
        this.neutralList=[]
        [this.neutralList.append(n['scores']['neutral']) for n in this.d]     
        this.surpriseList=[]
        [this.surpriseList.append(n['scores']['surprise']) for n in this.d]
    def totalSadness(this):
    	total=0
    	for i in this.sadnessList:
    		total+=i
    	return total
    def avgSadness(this):
    	avg= this.totalSadness()/len(this.sadnessList)
    	return avg
    def totalHappiness(this):
    	total=0
    	for i in this.happinessList:
    		total+=i
    	return total
    def avgHappiness(this):
    	avg= this.totalHappiness()/len(this.happinessList)
    	return avg
    def totalAnger(this):
    	total=0
    	for i in this.angerList:
    		total+=i
    	return total
    def avgAnger(this):
    	avg= this.totalAnger()/len(this.angerList)
    	return avg
    def totalContempt(this):
    	total=0
    	for i in this.contemptList:
    		total+=i
    	return total
    def avgContempt(this):
    	avg= this.totalContempt()/len(this.contemptList)
    	return avg
    def totalDisgust(this):
    	total=0
    	for i in this.disgustList:
    		total+=i
    	return total
    def avgDisgust(this):
    	avg= this.totalDisgust()/len(this.disgustList)
    	return avg
    def totalFear(this):
    	total=0
    	for i in this.fearList:
    		total+=i
    	return total
    def avgFear(this):
    	avg= this.totalFear()/len(this.fearList)
    	return avg
    def totalNeutral(this):
    	total=0
    	for i in this.neutralList:
    		total+=i
    	return total
    def avgNeutral(this):
    	avg= this.totalNeutral()/len(this.neutralList)
    	return avg
    def totalSurprise(this):
    	total=0
    	for i in this.surpriseList:
    		total+=i
    	return total
    def avgSurprise(this):
    	avg= this.totalSurprise()/len(this.surpriseList)
    	return avg
    def topEmotion(this):
    	emotiondict={'Sadness':this.avgSadness(), 'Happiness':this.avgHappiness(), 'Anger':this.avgAnger(), 'Contempt':this.avgContempt(), 'Disgust':this.avgDisgust(), 'Fear':this.avgFear(), 'Surprise':this.avgSurprise(), 'Neutral':this.avgNeutral()}
    	emotiondict=emotiondict.items()
    	top_emotion = sorted(emotiondict, key=lambda x: x[1], reverse=True)
    	if top_emotion[0][0] =='Neutral':
			top_emotion = str(top_emotion[1][0])+ 'Neutral'
			return top_emotion
    	else:
    		return top_emotion[0][0]
    def topEmotionScore(this):
    	emotiondict={'Sadness':this.avgSadness(), 'Happiness':this.avgHappiness(), 'Anger':this.avgAnger(), 'Contempt':this.avgContempt(), 'Disgust':this.avgDisgust(), 'Fear':this.avgFear(), 'Surprise':this.avgSurprise()}#, 'Neutral':this.avgNeutral()
    	emotiondict=emotiondict.items()
    	top_emotion = sorted(emotiondict, key=lambda x: x[1], reverse=True)
    	if top_emotion[0][0] =='Neutral':
			top_emotionScore = top_emotion[1][1]
			return top_emotionScore
    	else:
    		return top_emotion[0][1]

emotion_Instances=[]

for i in tvShow_instances:
	result_text = get_emotion_with_caching(i.PosterUrl, saved_cache, cache_fname)
	res = json.loads(result_text)
	if len(res) !=0:
		emotionInstance=TvEmotion(i.title,i.Genre, res, i.imdbRating, i.PosterUrl)
		emotion_Instances.append(emotionInstance)

arrayofdata=[(i.imdbRating, i.topEmotion(), i.topEmotionScore()) for i in emotion_Instances]

arrayofdata= sorted(arrayofdata,key=lambda tup: tup[0], reverse=True)

ifile = open('ImdbEmotion_scores.csv', 'w')
ifile.write('"IMDB Rating","Emotion","Emotion Score"\n')

for i in arrayofdata:
    ifile.write('{}, {}, {}\n'.format(i[0],i[1],i[2]))
ifile.close()


class IMDB_tvShow_Tests(unittest.TestCase):
    def setUp(self):
		singleJsonIMDBResponse='{"Title":"Last Week Tonight with John Oliver","Year":"2014\u2013","Rated":"TV-MA","Released":"27 Apr 2014","Runtime":"30 min","Genre":"Comedy, News, Talk-Show","Director":"N/A","Writer":"N/A","Actors":"John Oliver, David Kaye","Plot":"Former Daily Show host and correspondent John Oliver brings his persona to this new weekly news satire program.","Language":"English","Country":"USA","Awards":"Won 4 Primetime Emmys. Another 13 wins & 19 nominations.","Poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BNDAwMDY0NjA2Ml5BMl5BanBnXkFtZTgwMTA1NTI3NzE@._V1_SX300.jpg","Metascore":"N/A","imdbRating":"9.1","imdbVotes":"41,571","imdbID":"tt3530232","Type":"series","totalSeasons":"3","Response":"True"}'
		sample_imdb_data=json.loads(singleJsonIMDBResponse)
		self.newtvShow = tvShow(sample_imdb_data)
    def test_title_101(self):
		self.assertEqual(self.newtvShow.title, 'Last Week Tonight with John Oliver')
    def test_imdbRating_102(self):
		self.assertEqual(self.newtvShow.imdbRating, '9.1')	
    def test_Genre_103(self):
		self.assertEqual(self.newtvShow.Genre, 'Comedy, News, Talk-Show')
    def test_PosterUrl_104(self):
		self.assertEqual(self.newtvShow.PosterUrl, 'https://images-na.ssl-images-amazon.com/images/M/MV5BNDAwMDY0NjA2Ml5BMl5BanBnXkFtZTgwMTA1NTI3NzE@._V1_SX300.jpg')

class TvEmotion_Instantiation_Tests(unittest.TestCase):
	def setUp(self):
		singleJsonIMDBResponse='{"Title":"Last Week Tonight with John Oliver","Year":"2014\u2013","Rated":"TV-MA","Released":"27 Apr 2014","Runtime":"30 min","Genre":"Comedy, News, Talk-Show","Director":"N/A","Writer":"N/A","Actors":"John Oliver, David Kaye","Plot":"Former Daily Show host and correspondent John Oliver brings his persona to this new weekly news satire program.","Language":"English","Country":"USA","Awards":"Won 4 Primetime Emmys. Another 13 wins & 19 nominations.","Poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BNDAwMDY0NjA2Ml5BMl5BanBnXkFtZTgwMTA1NTI3NzE@._V1_SX300.jpg","Metascore":"N/A","imdbRating":"9.1","imdbVotes":"41,571","imdbID":"tt3530232","Type":"series","totalSeasons":"3","Response":"True"}'
		sample_imdb_data=json.loads(singleJsonIMDBResponse)
		self.newtvShow = tvShow(sample_imdb_data)
		result_text = get_emotion_with_caching(self.newtvShow.PosterUrl, saved_cache, cache_fname)
		res = json.loads(result_text)
		if len(res) !=0:
			self.emotionInstance=TvEmotion(self.newtvShow.title, self.newtvShow.Genre, res, self.newtvShow.imdbRating, self.newtvShow.PosterUrl)
		else:
			return 'No Emotion Instance due to no emotion Json Response'
	def test_title_201(self):
		self.assertIn(self.emotionInstance.title,'Last Week Tonight with John Oliver', "Title not successfully passed to Emotion Instance")		
	def test_genre_202(self):
		self.assertIn(self.emotionInstance.genre,'Comedy, News, Talk-Show', "Genre not successfully passed to Emotion Instance")		
	def test_imdbRating_203(self):
		self.assertIn(self.emotionInstance.imdbRating,'9.1', "imdbRating not successfully passed to Emotion Instance")		
	def test_PosterUrl_204(self):
		self.assertIn(self.emotionInstance.posterUrl,"https://images-na.ssl-images-amazon.com/images/M/MV5BNDAwMDY0NjA2Ml5BMl5BanBnXkFtZTgwMTA1NTI3NzE@._V1_SX300.jpg", "PosterUrl not successfully passed to Emotion Instance")		

class TvEmotion_Methods_Tests(unittest.TestCase):
	def setUp(self):
		singleJsonIMDBResponse='{"Title":"Last Week Tonight with John Oliver","Year":"2014\u2013","Rated":"TV-MA","Released":"27 Apr 2014","Runtime":"30 min","Genre":"Comedy, News, Talk-Show","Director":"N/A","Writer":"N/A","Actors":"John Oliver, David Kaye","Plot":"Former Daily Show host and correspondent John Oliver brings his persona to this new weekly news satire program.","Language":"English","Country":"USA","Awards":"Won 4 Primetime Emmys. Another 13 wins & 19 nominations.","Poster":"https://images-na.ssl-images-amazon.com/images/M/MV5BNDAwMDY0NjA2Ml5BMl5BanBnXkFtZTgwMTA1NTI3NzE@._V1_SX300.jpg","Metascore":"N/A","imdbRating":"9.1","imdbVotes":"41,571","imdbID":"tt3530232","Type":"series","totalSeasons":"3","Response":"True"}'
		sample_imdb_data=json.loads(singleJsonIMDBResponse)
		self.newtvShow = tvShow(sample_imdb_data)
		result_text = get_emotion_with_caching(self.newtvShow.PosterUrl, saved_cache, cache_fname)
		res = json.loads(result_text)
		if len(res) !=0:
			self.emotionInstance=TvEmotion(self.newtvShow.title, self.newtvShow.Genre, res, self.newtvShow.imdbRating, self.newtvShow.PosterUrl)
		else:
			return 'No Emotion Instance due to no emotion Json Response'
	def test_Sadness_301(self):
		self.assertIn(str(self.emotionInstance.totalSadness()),'0.028296655', "totalSadness is not accurate")
		self.assertIn(str(self.emotionInstance.avgSadness()),'0.028296655', "avgSadness is not accurate")
	def test_Happiness_302(self):
		self.assertIn(str(self.emotionInstance.totalHappiness()),'0.001290715', "totalHappiness is not accurate")
		self.assertIn(str(self.emotionInstance.avgHappiness()),'0.001290715', "avgHappiness is not accurate")
	def test_Anger_303(self):
		self.assertIn(str(self.emotionInstance.totalAnger()),'1.16888614e-05', "totalAnger is not accurate")
		self.assertIn(str(self.emotionInstance.avgAnger()),'1.16888614e-05', "avgAnger is not accurate")
	def test_Contempt_304(self):
		self.assertIn(str(self.emotionInstance.totalContempt()),'0.00205081562', "totalContempt is not accurate")
		self.assertIn(str(self.emotionInstance.avgContempt()),'0.00205081562', "avgContempt is not accurate")
	def test_Disgust_305(self):
		self.assertIn(str(self.emotionInstance.totalDisgust()),'3.995938e-05', "totalDisgust is not accurate")
		self.assertIn(str(self.emotionInstance.avgDisgust()),'3.995938e-05', "avgDisgust is not accurate")
	def test_Fear_306(self):
		self.assertIn(str(self.emotionInstance.totalFear()),'1.03496168e-05', "totalFear is not accurate")
		self.assertIn(str(self.emotionInstance.avgFear()),'1.03496168e-05', "avgFear is not accurate")
	def test_Neutral_307(self):
		self.assertIn(str(self.emotionInstance.totalNeutral()),'0.9677991', "totalNeutral is not accurate")
		self.assertIn(str(self.emotionInstance.avgNeutral()),'0.9677991', "avgNeutral is not accurate")
	def test_Surprise_308(self):
		self.assertIn(str(self.emotionInstance.totalSurprise()),'0.000500713941', "totalSurprise is not accurate")
		self.assertIn(str(self.emotionInstance.avgSurprise()),'0.000500713941', "avgSurprise is not accurate")
	def test_topEmotion_309(self):
		self.assertIn(str(self.emotionInstance.topEmotion()), 'SadnessNeutral', "topEmotion is incorrect")
	def test_topEmotionScore_310(self):
		print self.emotionInstance.topEmotionScore()
		self.assertIn(str(self.emotionInstance.topEmotionScore()), '0.028296655', "topEmotionScore is incorrect")

unittest.main(verbosity=2)
