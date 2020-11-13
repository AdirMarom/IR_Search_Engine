from urllib.parse import urlparse

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from document import Document
import re

class Parse:

    def __init__(self):
        self.stop_words = stopwords.words('english')

    def parse_sentence(self, text):
        """
        This function tokenize, remove stop words and apply lower case for every word within the text
        :param text:
        :return:
        """
        text_tokens = word_tokenize(text)
        text_tokens_without_stopwords = [w.lower() for w in text_tokens if w not in self.stop_words]
        return text_tokens_without_stopwords

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
        full_text=self.Hashtags_parse(full_text)
        full_text = self.percent_parse(full_text)
        retweet_url = self.parse_url(retweet_url)
        url = self.parse_url(url)
        quote_url = self.parse_url(quote_url)
        tokenized_text = self.parse_sentence(full_text)


        doc_length = len(tokenized_text)  # after text operations.

        for term in tokenized_text:
            if term not in term_dict.keys():
                term_dict[term] = 1
            else:
                term_dict[term] += 1

        document = Document(tweet_id, tweet_date, full_text, url, retweet_text, retweet_url, quote_text,
                            quote_url, term_dict, doc_length)
        return document

    def parse_url(url_string):
        """
        This function takes a  url_string from document and break it into to list of word :
        https://www.instagram.com/p/CD7fAPWs3WM/?igshid=o9kf0ugp1l8x ->[https, www, instagram.com, p, CD7fAPWs3WM, igshid, o9kf0ugp1l8x ]
        :param tag: Hashtag word from tweet.
        :return: list include spread world from the url .
        """
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

        return lst

    def is_tag(word):
        if (word.startswith('@') and len(word) > 1):
            return True
        return False




        def fix_number(sentence):
            """
                    This function change the representation of Number,10,000->10K ,10,123->10.123K
                                                                        1,123,000->1.123M
                                                                        1,123,000,000->1.123B
                    :param number:  num from tweet.
                    :return:string in Format  Number% .
                    """
            sentence = sentence.split(' ')
            for i in range(len(sentence)):
                if (re.search(r"\d", sentence[i])):
                    if (i + 1 != len(sentence) and sentence[i + 1] != "Thousand" and sentence[i + 1] != "Million" and
                            sentence[i + 1] != "Billion"):
                        num = sentence[i]
                        num = num.replace(',', '')
                        first_num = float(num)
                        if (num.isdigit()):
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
                            if (sentence[i][-2] == '0'):
                                sentence[i] = sentence[i][0:-2] + sentence[i][-1]
                                if (sentence[i][-2] == '0'):
                                    sentence[i] = sentence[i][0:-2] + sentence[i][-1]
                                    if (sentence[i][-2] == '0'):
                                        sentence[i] = sentence[i][0:-2] + sentence[i][-1]
                                        if (sentence[i][-2] == '.'):
                                            sentence[i] = sentence[i][0:-2] + sentence[i][-1]

                    if (i + 1 == len(sentence)):
                        break
                    else:
                        if (sentence[i + 1] == "Thousand"):
                            sentence[i] += "K"
                            sentence[i + 1] = ""
                        elif (sentence[i + 1] == "Million"):
                            sentence[i] += "M"
                            sentence[i + 1] = ""
                        elif (sentence[i + 1] == "Billion"):
                            sentence[i] += "B"
                            sentence[i + 1] = ""

            sentence = ' '.join(map(str, sentence))

    def Hashtags_parse(text):
        """
        This function takes a  Hashtag world from document and break it into to list of word
        :param tag: Hashtag word from tweet.
        :return: list include spread world and #tag .
        """
        lst=str.split(text," ")
        count=0
        for term in lst:
            count+=1
            tag=term
            if(tag[0]!='#'):
                continue
            strToParse=tag[1:]
            flag=strToParse.find('_')
            if flag>-1:
                parseList = re.sub(r"([^a-zA-Z])", r" \1", strToParse)
                parseList=str.replace(parseList,'_','')

            else:
                parseList = re.sub(r"([A-Z])", r" \1", strToParse)
            parseList = parseList.lower()
            split_tag= str.split(parseList, " ") + ['#' + strToParse]
        if(count==len(lst)):
            lst+=split_tag
        else:
            lst= lst[:count]+split_tag+lst[count]
        return ' '.join(map(str,lst))


    def percent_parse(strToParse):
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



