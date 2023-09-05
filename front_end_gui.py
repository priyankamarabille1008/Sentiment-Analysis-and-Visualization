# -*- coding: utf-8 -*-
#http://www.tweepy.org/
import tweepy
import sys
import csv
from textblob import TextBlob
from tkinter.filedialog import askopenfilename
from tkinter import Tk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns

#Get your Twitter API credentials and enter them here
consumer_key = "IgM5R8xVMGNJBZuqQ42RbEHI5"
consumer_secret = "Myu6ernLGk2ODUrsBNWr6deZu01MzlnVMTkvz93JARFJVHuoqU"
access_key = "339802190-clJpgJofm8n6tXUPVwrmWDILUZFdEGvecKqynjbY"
access_secret = "qqOr9Fx5Sh3uIxS0nf8Y0ic1rnoK2HJhQg0uAIpEGL5fh"
data = []

class File_Pass:
    #positive_sentiment = 0
    #negative_sentiment = 0
    def __init__(self,name):
        self.name = name

    def Analysiz_Text(self):
        global positive_sentiment, negative_sentiment
        positive_sentiment = 0
        negative_sentiment = 0
        neutral_sentiment = 0
        try:
            with open(self.name, 'r') as UseFile:
                data = UseFile.readlines()
                list_text = data
                # print(list_text)
                for text in list_text:
                    # print("for")
                    obj = TextBlob(text)
                    if obj.sentiment.polarity > 0.3:
                        # print('-')
                        positive_sentiment += 1
                    elif obj.sentiment.polarity < -0.3:
                        # print('+')
                        negative_sentiment += 1
                    else:
                        neutral_sentiment += 1


        except FileNotFoundError:
            print("No file exists")


        return positive_sentiment, negative_sentiment, neutral_sentiment
