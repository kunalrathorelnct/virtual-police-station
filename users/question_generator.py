import numpy as np 
from nltk.corpus import stopwords
import re
import scipy
import random

def load_model():
	with open('static/glove.6B.50d.txt') as f:
		content=f.readlines()
	model={}
	for line in content:
		splitLine=line.split()
		word=splitLine[0]
		embedding = np.array([float(val) for val in splitLine[1:]])
		model[word]=embedding

	return model

def preprocess(text):
	# keep only words
    letters_only_text = re.sub("[^a-zA-Z]", " ", text)

    # convert to lower case and split 
    words = letters_only_text.lower().split()

    # remove stopwords
    stopword_set = set(stopwords.words("english"))
    cleaned_words = list(set([w for w in words if w not in stopword_set]))

    return cleaned_words


def cosine_distance_between_two_words(word1, word2):
    return (1- scipy.spatial.distance.cosine(model[word1], model[word2]))


def cosine_distance_wordembedding_method(s1, s2,model):
    vector_1 = np.mean([model[word] for word in preprocess(s1)],axis=0)
    vector_2 = np.mean([model[word] for word in preprocess(s2)],axis=0)
    cosine = scipy.spatial.distance.cosine(vector_1, vector_2)
    #print('Our two sentences are similar to',round((1-cosine)*100,2),'%')
    return round((1-cosine)*100,2)

def load_crime():
	with open('static/crime/type_of_crime.txt') as file:
		content=file.readlines()

	return content

def crime_classifier(type_of_crime):
	model = load_model()
	content = load_crime()
	probability = []
	for ss in content:
		temp = cosine_distance_wordembedding_method(ss[:-1],type_of_crime,model)
		probability.append([temp,ss[:-1]])

	if max(probability)[0]>75:
		type_of_crime = max(probability)[1]
	else:
		type_of_crime = 'general'
	print(probability,type_of_crime)
	# with open('static/crime/'+str(type_of_crime)+'.txt') as f:
	# 	ques = f.readlines()
	# response = [] 
	# for i in ques:
	# 	response.append(i)

	return type_of_crime





