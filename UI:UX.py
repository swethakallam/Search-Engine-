#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 16:17:22 2019

@author: ankithamadduri
"""

#!/usr/bin/env python
import pandas as pd
import numpy as np

from flask import Flask, render_template,request

# Create the application.
APP = Flask(__name__)


@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return render_template('home.html')

@APP.route('/dashboard', methods=['POST'])
def foo():
    # grab reddit data and write to csv
    if request.method == 'POST':
        query = request.form['searchtxt']
        results = tfidf(query)
        if results:
            has_data = "true"
        else:
            has_data = "false"
        return render_template('dashboard.html', userdata  = results, condition = has_data)
    
def tfidf(query):
    data_df = pd.read_csv("scrapped.csv")
    data_df['name'] = data_df['name'].str.lower()
    data_df['brand'] = data_df['brand'].str.lower()
    data_df['name'] = data_df['name'].str.replace('[^a-zA-Z]', ' ')
    data_df['brand'] = data_df['brand'].str.replace('[^a-zA-Z]', ' ')
    data = np.array(data_df)
    
    from collections import defaultdict
    import math
    dicD = defaultdict(lambda: defaultdict(int))
    dataarr = list()
    wordsD = defaultdict(set)
    output = defaultdict(list)
    for doc, desc, brand, image, price in data:
         desc = desc + " " +brand
         descWords = desc.split()
         for word in descWords:
            word = word.strip()
            if word not in dicD[word]:
                dicD[doc][word]+=1
                wordsD[word].add(doc)
         output[doc].append(image)
         output[doc].append(price)
         output[doc].append(desc)
         output[doc].append(brand)
         
    query = query.strip().split()     
    score = defaultdict(float)
    for word in query:
        word=word.strip()
        for doc, word_value in dicD.items():
            if word in word_value.keys():
                tf = word_value[word] / len(word_value.keys())
                if doc in wordsD[word]:
                    idf = math.log(len(dicD)/len(wordsD[word]))    
                else:
                    idf = 0
                score[doc] = score[doc] + (tf * idf)
            else:
                z = 1
                
    sorted_d = sorted(score.items(), key=lambda x: x[1], reverse=True)
    top = 0
    for doc, value in sorted_d:
        if top == 30:
            break
        dataarr.append({"url": doc, "link": output[doc][0],"price" : output[doc][1], "name": output[doc][2], "brand": output[doc][3]})
        top+=1      
    return dataarr


if __name__ == '__main__':
    APP.debug=True
    APP.run()