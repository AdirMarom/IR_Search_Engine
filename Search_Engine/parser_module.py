from urllib.parse import urlparse

from nltk import pos_tag, RegexpParser
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from document import Document
import re
import spacy

class Parse:

    def __init__(self):
        self.stop_words = stopwords.words('english')
        self.global_dict={}
        self.garbage=[]



    def parse_sentence(self, text):
        """
        This function tokenize, remove stop words and apply lower case for every word within the text
        :param text:
        :return:
        """

        text_tokens = word_tokenize(text)
        text_tokens_without_stopwords = [w for w in text_tokens if w not in self.stop_words]
        text_tokens_without_stopwords_ = [self.extand_contractions(w.lower()) for w in text_tokens if w not in self.stop_words]
        for text in text_tokens_without_stopwords: text= self.extand_contractions(text)
        return text_tokens_without_stopwords

    def extand_contractions(self,word):
        '''
         function extand contraction and Common Acronyms in Twitter
        :param word:
        :return:
        '''
        contractions = {
            "ain't": "am not / are not",
            "aren't": "are not / am not",
            "can't": "cannot",
            "can't've": "cannot have",
            "'cause": "because",
            "could've": "could have",
            "couldn't": "could not",
            "couldn't've": "could not have",
            "didn't": "did not",
            "doesn't": "does not",
            "don't": "do not",
            "hadn't": "had not",
            "hadn't've": "had not have",
            "hasn't": "has not",
            "haven't": "have not",
            "he'd": "he had / he would",
            "he'd've": "he would have",
            "he'll": "he shall / he will",
            "he'll've": "he shall have / he will have",
            "he's": "he has / he is",
            "how'd": "how did",
            "how'd'y": "how do you",
            "how'll": "how will",
            "how's": "how has / how is",
            "i'd": "I had / I would",
            "i'd've": "I would have",
            "i'll": "I shall / I will",
            "i'll've": "I shall have / I will have",
            "i'm": "I am",
            "i've": "I have",
            "isn't": "is not",
            "it'd": "it had / it would",
            "it'd've": "it would have",
            "it'll": "it shall / it will",
            "it'll've": "it shall have / it will have",
            "it's": "it has / it is",
            "let's": "let us",
            "ma'am": "madam",
            "mayn't": "may not",
            "might've": "might have",
            "mightn't": "might not",
            "mightn't've": "might not have",
            "must've": "must have",
            "mustn't": "must not",
            "mustn't've": "must not have",
            "needn't": "need not",
            "needn't've": "need not have",
            "o'clock": "of the clock",
            "oughtn't": "ought not",
            "oughtn't've": "ought not have",
            "shan't": "shall not",
            "sha'n't": "shall not",
            "shan't've": "shall not have",
            "she'd": "she had / she would",
            "she'd've": "she would have",
            "she'll": "she shall / she will",
            "she'll've": "she shall have / she will have",
            "she's": "she has / she is",
            "should've": "should have",
            "shouldn't": "should not",
            "shouldn't've": "should not have",
            "so've": "so have",
            "so's": "so as / so is",
            "that'd": "that would / that had",
            "that'd've": "that would have",
            "that's": "that has / that is",
            "there'd": "there had / there would",
            "there'd've": "there would have",
            "there's": "there has / there is",
            "they'd": "they had / they would",
            "they'd've": "they would have",
            "they'll": "they shall / they will",
            "they'll've": "they shall have / they will have",
            "they're": "they are",
            "they've": "they have",
            "to've": "to have",
            "wasn't": "was not",
            "we'd": "we had / we would",
            "we'd've": "we would have",
            "we'll": "we will",
            "we'll've": "we will have",
            "we're": "we are",
            "we've": "we have",
            "weren't": "were not",
            "what'll": "what shall / what will",
            "what'll've": "what shall have / what will have",
            "what're": "what are",
            "what's": "what has / what is",
            "what've": "what have",
            "when's": "when has / when is",
            "when've": "when have",
            "where'd": "where did",
            "where's": "where has / where is",
            "where've": "where have",
            "who'll": "who shall / who will",
            "who'll've": "who shall have / who will have",
            "who's": "who has / who is",
            "who've": "who have",
            "why's": "why has / why is",
            "why've": "why have",
            "will've": "will have",
            "won't": "will not",
            "won't've": "will not have",
            "would've": "would have",
            "wouldn't": "would not",
            "wouldn't've": "would not have",
            "y'all": "you all",
            "y'all'd": "you all would",
            "y'all'd've": "you all would have",
            "y'all're": "you all are",
            "y'all've": "you all have",
            "you'd": "you had / you would",
            "you'd've": "you would have",
            "you'll": "you shall / you will",
            "you'll've": "you shall have / you will have",
            "you're": "you are",
            "you've": "you have",
            "AFK": "Away From Keyboard",
            "BBIAB": "Be Back In A Bit",
            "BBL": "Be Back Later",
            "BBS ":"Be Back Soon",
            "BEG" : "Big Evil Grin",
            "BRB" : "Be Right Back",
            "BTW": "By The Way",
            "EG":"Evil Grin",
            "FISH" : "First In, Still Here",
            "IDK" : "I Don't Know",
            "IMO" : "In My Opinion",
            "IRL" :"In Real Life",
            "KISS":"Keep It Simple,Stupid",
            "LMK" :"Let Me Know",
            "LOL" :"Laughing Out Loud",
            "NYOB":" None of Your Business",
            "OFC ":"Of Course",
            "OMG ":"Oh My God",
            "PANS":"Pretty Awesome New Stuff",
            "PHAT":"Pretty, Hot, And Tempting",
            "POS ":"Parents Over Shoulder",
            "ROFL": "Rolling On the Floor Laughing",
            "SMH ":"Shaking My Head",
            "TTYL":"Talk To You Later",
            "YOLO": "You Only Live Once",
            "WTH ":"What The Heck",
        }
        if(word in contractions):
            return contractions[word.lower()]
        return word

    def parse_doc(self, doc_as_list):
        """
        This function takes a tweet document as list and break it into different fields
        :param doc_as_list: list re-preseting the tweet.
        :return: Document object with corresponding fields.
        """
        tweet_id = doc_as_list[0]
        tweet_date = doc_as_list[1]
        full_text = doc_as_list[2]
        url = doc_as_list[3]
        retweet_text = doc_as_list[4]
        retweet_url = doc_as_list[5]
        quote_text = doc_as_list[6]
        quote_url = doc_as_list[7]
        term_dict = {}
        retweet_url = self.parse_url(retweet_url)
        url = self.parse_url(url)
        quote_url = self.parse_url(quote_url)
        full_text=self.advance_parse(full_text)
        tokenized_text = self.parse_sentence(full_text)
        doc_length = len(tokenized_text)  # after text operations.


        for term in tokenized_text:
            self.upper_lower_case(term)

        for term in tokenized_text:
            self.update_global_dict(term)
       #     term1=term.lower()
       #     if(term1 in self.global_dict.keys()):
       #         term=term.lower()
       #         if(self.global_dict[term][1]==0):
       #             term=term.lower()
       #         else:
       #             term=term.upper()
            if term not in term_dict.keys():
                term_dict[term] = 1
            else:
                term_dict[term] += 1

        document = Document(tweet_id, tweet_date, full_text, url, retweet_text, retweet_url, quote_text,
                            quote_url, term_dict, doc_length)
        return document

    def update_global_dict(self,term):
        if(term.isalpha()):
            if term in self.global_dict.keys():
                if str.isupper(term[0]):
                    if term.lower() in self.global_dict.keys():
                        print(term.lower() +':'+str(self.global_dict[term.lower()]))
                        print(term + ':' + str(self.global_dict[term]))
                        self.global_dict[term.lower()]+= self.global_dict[term]+1
                        print(term.lower() + ':' +str(self.global_dict[term.lower()]))
                        del self.global_dict[term]
                    else:
                        self.global_dict[term]+=1
                else:
                    self.global_dict[term]=self.global_dict[term]+1
            else:
                self.global_dict[term]=1
        else:
            self.garbage.append(term)


    def advance_parse(self,full_text):
        full_text=self.Hashtags_parse(full_text)
        full_text = self.percent_parse(full_text)
        full_text=self.fix_number(full_text)
        return full_text

    def upper_lower_case(self,word):
        if (word[0].isalpha()==False):
            return
        word_status=(0,0)
        if(word[0].isupper()):
            word_status=(word,1)
        else:
            word_status=(word,0)
        word=word.lower()

    #   if(word not in self.global_dict.keys()):
    #           self.global_dict[word]=word_status
    #   else:
    #       if (word_status[1]==1 and self.dict[word][1]==0):
    #           self.dict[word][1]=0
    #       elif(word_status[1]==0 and self.dict[word][1]==1):
    #           self.dict[word] = 0

    def parse_url(self,url_string):
        """
        This function takes a  url_string from document and break it into to list of word :
        https://www.instagram.com/p/CD7fAPWs3WM/?igshid=o9kf0ugp1l8x ->[https, www, instagram.com, p, CD7fAPWs3WM, igshid, o9kf0ugp1l8x ]
        :param tag: Hashtag word from tweet.
        :return: list include spread world from the url .
        """
        if(url_string is None or url_string is ''):
            return
        lst = []
        o = urlparse(url_string)
        scheme = o.scheme
        lst.append(scheme)
        netloc = re.split(', |_|-|!', o.netloc)[0]
        if ("www." in netloc):
            netloc1 = netloc[0:3]
            netloc2 = netloc[4:]
            lst.append(netloc1)
            lst.append(netloc2)
        else:
            lst.append(netloc)
        path = re.split(', |_|-|!|/', o.path)
        for i in range(len(path)):
            if (path[i] != ''):
                lst.append(path[i])

        query = re.split(', |_|-|!|=', o.query)
        for j in range(len(query)):
            if (query[j] != ''):
                lst.append(query[j])

        return ' '.join(map(str, lst))

    def is_tag(self,word):
        if (word.startswith('@') and len(word) > 1):
            return True
        return False

    def fix_number(self,sentence):
            sentence=word_tokenize(sentence)
            #sentence = re.split(', |_|-|!|/| ', sentence)
            a=2
            for i in range(len(sentence)):
                if (re.search(r"\d", sentence[i])):
                    if (i + 1 != len(sentence) and sentence[i + 1] != "Thousand" and sentence[i + 1] != "Million" and
                            sentence[i + 1] != "Billion"):
                        num = sentence[i]
                        num = num.replace(',', '')
                        if(num.isnumeric()==False):
                            continue
                        flag=False
                        for digit in range(len(num)):
                            if(num[digit].isdigit()==False):
                                flag=True;
                        if(flag):
                            continue

                        if (num.isnumeric()):
                            num = float(num)
                            if (1000 <= num < 1000000):
                                num = num / 1000
                                sentence[i] = "%.3f" % num + "K"

                            elif (1000000 <= num < 1000000000):
                                num = num / 1000000
                                sentence[i] = "%.3f" % num + "M"
                            elif (num > 1000000000):
                                sentence[i] = num / 1000000000
                                sentence[i] = "%.3f" % num + "B"
                            if (len(sentence[i]) >=2 and sentence[i][-2] == '0'):
                                sentence[i] = sentence[i][0:-2] + sentence[i][-1]
                                if (len(sentence[i]) >=2 and sentence[i][-2] == '0'):
                                    sentence[i] = sentence[i][0:-2] + sentence[i][-1]
                                    if (len(sentence[i]) >=2 and sentence[i][-2] == '0'):
                                        sentence[i] = sentence[i][0:-2] + sentence[i][-1]
                                        if (len(sentence[i]) >=2 and sentence[i][-2] == '.'):
                                            sentence[i] = sentence[i][0:-2] + sentence[i][-1]

                    if (i + 1 == len(sentence)):
                        break
                    else:
                        if (sentence[i + 1] == "Thousand" or sentence[i + 1] == "thousand"):
                            sentence[i] += "K"
                            sentence[i + 1] = ""
                        elif (sentence[i + 1] == "Million" or sentence[i + 1] == "million"):
                            sentence[i] += "M"
                            sentence[i + 1] = ""
                        elif (sentence[i + 1] == "Billion" or sentence[i + 1] == "billion"):
                            sentence[i] += "B"
                            sentence[i + 1] = ""

            sentence = ' '.join(map(str, sentence))
            sentence.replace("Thousand","1K")
            sentence.replace("thousand", "1K")
            sentence.replace("Million", "1M")
            sentence.replace("million", "1M")
            sentence.replace("Billion", "1B")
            sentence.replace("billion", "1B")
            return sentence

    def Hashtags_parse(self,text):
        """
        This function takes a  Hashtag world from document and break it into to list of word
        :param tag: Hashtag word from tweet.
        :return: list include spread world and #tag .
        """
        text=text.replace("/n",'')
        lst=str.split(text," ")
        if(lst.__contains__('')):
            lst.remove('')
        count=0
        parseList=''
        for term in lst:
            count+=1
            tag=term
            if(len(tag)<=0 or tag[0]!='#'):
                continue
            parseList=tag[1:]
            parseList = str.replace(parseList, '_', '')
            parseList = re.sub(r"([A-Z])", r" \1", parseList)
            parseList = parseList.lower()
            secparseList= parseList.replace(' ','')
            split_tag= str.split(parseList, " ") + ['#' + secparseList]
            if(count==len(lst)):
                lst=lst[:len(lst)-1]+split_tag
            else:
                lst= lst[:count]+split_tag+lst[count:]
        lst= ' '.join(map(str,lst))
        return lst

    def percent_parse(self,strToParse):
        """
        This function change the representation of Number%,Number percent,Number percentage to Number%
        :param s:  word from tweet.
        :return:string in Format  Number% .
        """
        #check if the number only in digit
        strToParse = str.replace(strToParse, ' percentage', '%')
        strToParse = str.replace(strToParse, ' PERCENTAGE', '%')
        strToParse = str.replace(strToParse, ' PERCENT', '%')
        strToParse = str.replace(strToParse, ' percent', '%')
        return strToParse

