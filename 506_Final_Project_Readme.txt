506 Final Project Readme- Ali Mourad


1. Describe your project in 1-4 sentences. Include the basic summary of what it does, and the output that it should generate/how one can use the output and/or what question the output answers. 


The program makes use of the OMDB Api to retrieve rating, genre, and the poster image url from IMDB. The poster image url is run through the Microsoft Cognitive Services Emotion Api to retrieve values of facial emotions that include anger, contempt, disgust, fear, happiness, neutral, sadness, and surprise. The averages of facial emotion scores for all the different faces on a poster image are aggregated to determine the top scoring emotion of a show and this is compared to the TV show rating. in different genres to make an analysis about how the poster emotion score compares to the top rankings.


2. Instructions to Run

First run python final.py
cached data is in the required files: cached_imdb_results.txt and cached_emotion_results.txt. You should have a new file in your directory afterward, ImdbEmotion_scores.csv, which contains data ordered by the imdb rating followed with the top emotion and its average score.

3. All Files and Description:

final.py: The main program that executes and produces csv output.
506_Final_Project_Readme.txt: Description of the program and project.
cached_imdb_results.txt: Cached results from the Omdb api.
cached_emotion_results: Cached results from the Microsoft Emotion api.
ImdbEmotion_scores.csv: Output produced

4. Python packages/modules that must be installed in order to run 
requests,json, unittest, pickle

5. API sources

Emotion Api
https://www.microsoft.com/cognitive-services/en-us/emotion-api
Uses computer vision to detect faces in an image and produce numerical values for the detected emotions.

Omdb Api
https://www.omdbapi.com/
Retrieves data about tv shows from the Internet Movie Database(IMDB)

6. Approximate line numbers in Python file to find the following mechanics requirements:

- Sorting with a key function: 177, 204
- Use of list comprehension OR map OR filter: 202
- Class definition beginning 1: 34
- Class definition beginning 2: 86
- Creating instance of one class: 83
- Creating instance of a second class: 199
- Calling any method on any class instance (list all approx line numbers where this happens, or line numbers where there is a chunk of code in which a bunch of methods are invoked):

>Calling topEmotion() and topEmotionScore() on line 202
>Calling the total() methods on lines 116,124,132,140,148,156,164,172
>Calling all the average methods on lines 157 and 184

- (If applicable) Beginnings of function definitions outside classes:  48, 56
- Beginning of code that handles data caching/using cached data: 17, 61
- Test cases: 214 

