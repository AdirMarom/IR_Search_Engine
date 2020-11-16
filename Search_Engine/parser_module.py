from urllib.parse import urlparse

from nltk import pos_tag, RegexpParser
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from document import Document
import re
##import spacy

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
        if(word in contractions.keys()):
            return contractions[word]
        return word

    def find_entities(self,text):
        nlp = spacy.load("en_core_web_lg")
        doc = nlp(text)
        dict = {}
        for ent in doc.ents:
            string_name = str(ent)
            if string_name in dict.keys():
                dict[string_name] += 1
            else:
                dict[string_name] = 1
        lst = []
        for key in dict.keys():
            if (dict[key] >= 2):
                lst.append(key)
        return lst

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
           ## self.update_global_dict(term)

            #save word begin in @
            term_dict=self.save_as_tag(term,term_dict)
            #save numbers end with M K B
            term_dict=self.fix_number(term,term_dict)
            #save #tag
            term_dict = self.Hashtags_parse(term, term_dict)
            #save num%
            term_dict= self.percent_parse(term, term_dict)

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
                        self.global_dict[term.lower()]+= self.global_dict[term]+1
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

    def save_as_tag(self, word,term_dict):
        if (word.startswith('@') and len(word) > 1):
            self.update_global_dict(word)
            return self.update_doc_dict(term_dict,word)
        return term_dict

    def fix_number(self,sentence,term_dict):
            sentence=word_tokenize(sentence)
            #sentence = re.split(', |_|-|!|/| ', sentence)
            a=2
            lst_piece_num=[]
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
                    lst_piece_num.append(sentence[i])
                    term_dict=self.update_doc_dict(term_dict, sentence[i])
            for word in lst_piece_num:
                self.update_global_dict(word)
            ##sentence = ' '.join(map(str, sentence[i]))

            return term_dict

    def update_doc_dict(self,term_dict,word):
        if word not in term_dict.keys():
            term_dict[word] = 1
        else:
            term_dict[word] += 1
        return term_dict

    def update_global_dict(self, word):
        if word not in self.global_dict.keys():
            self.global_dict[word] = 1
        else:
            self.global_dict[word] += 1

    def Hashtags_parse(self,text,term_dict):
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
            flag=True
            if(len(tag)<=0 or tag[0]!='#'):
                continue
            parseList=tag[1:]
            parseList = str.replace(parseList, '_', '')
            parseList = re.sub(r"([A-Z])", r" \1", parseList)
            parseList = parseList.lower()
            secparseList= parseList.replace(' ','')
            split_tag= str.split(parseList, " ") + ['#' + secparseList]
            for word in split_tag:
                term_dict=self.update_doc_dict(term_dict,word)
                if(flag):
                    flag=False
                    self.update_global_dict(word)
        return term_dict

     ##       if(count==len(lst)):
     ##           lst=lst[:len(lst)-1]+split_tag
     ##       else:
     ##           lst= lst[:count]+split_tag+lst[count:]
     ##   lst= ' '.join(map(str,lst))
       ## return lst

    def percent_parse(self,sentence,term_dict):
        """
        This function change the representation of Number%,Number percent,Number percentage to Number%
        :param s:  word from tweet.
        :return:string in Format  Number% .
        """

        sentence_lst = word_tokenize(sentence)
        percent_op=[' percentage',' PERCENTAGE',' PERCENT',' percent']
        for i in range(0,len(sentence_lst)):
            if(str.isnumeric(sentence_lst[i] and i+1<len(sentence_lst)) and sentence_lst[i+1] in percent_op):
                term_dict=self.update_doc_dict(term_dict,sentence_lst[i]+'%')
                self.update_global_dict(sentence_lst[i]+'%')
        return term_dict

    def currency_parse(self, sentence, term_dict):
        """
              This function converting string currency to multiple ways to show it
              :param sentence:  thw sentece we look up for currency show
              :return:same sentence with extends, $-->$,usd,us dollar .
              """
        curr_lst=[]
        currency_dict = {
            'ALL': 'Albania Lek',
            'AFN': 'Afghanistan Afghani',
            'ARS': 'Argentina Peso',
            'AWG': 'Aruba Guilder',
            'AUD': 'Australia Dollar',
            'AZN': 'Azerbaijan New Manat',
            'BSD': 'Bahamas Dollar',
            'BBD': 'Barbados Dollar',
            'BDT': 'Bangladeshi taka',
            'BYR': 'Belarus Ruble',
            'BZD': 'Belize Dollar',
            'BMD': 'Bermuda Dollar',
            'BOB': 'Bolivia Boliviano',
            'BAM': 'Bosnia and Herzegovina Convertible Marka',
            'BWP': 'Botswana Pula',
            'BGN': 'Bulgaria Lev',
            'BRL': 'Brazil Real',
            'BND': 'Brunei Darussalam Dollar',
            'KHR': 'Cambodia Riel',
            'CAD': 'Canada Dollar',
            'KYD': 'Cayman Islands Dollar',
            'CLP': 'Chile Peso',
            'CNY': 'China Yuan Renminbi',
            'COP': 'Colombia Peso',
            'CRC': 'Costa Rica Colon',
            'HRK': 'Croatia Kuna',
            'CU': 'Cuba Peso',
            'CZK': 'Czech Republic Koruna',
            'DKK': 'Denmark Krone',
            'DOP': 'Dominican Republic Peso',
            'XCD': 'East Caribbean Dollar',
            'EGP': 'Egypt Pound',
            'SVC': 'El Salvador Colon',
            'EEK': 'Estonia Kroon',
            'EUR': 'Euro Member Countries',
            'FKP': 'Falkland Islands (Malvinas) Pound',
            'FJD': 'Fiji Dollar',
            'GHC': 'Ghana Cedis',
            'GIP': 'Gibraltar Pound',
            'GTQ': 'Guatemala Quetzal',
            'GGP': 'Guernsey Pound',
            'GYD': 'Guyana Dollar',
            'HNL': 'Honduras Lempira',
            'HKD': 'Hong Kong Dollar',
            'HUF': 'Hungary Forint',
            'ISK': 'Iceland Krona',
            'INR': 'India Rupee',
            'IDR': 'Indonesia Rupiah',
            'IRR': 'Iran Rial',
            'IMP': 'Isle of Man Pound',
            'ILS': 'Israel Shekel',
            'JMD': 'Jamaica Dollar',
            'JPY': 'Japan Yen',
            'JEP': 'Jersey Pound',
            'KZT': 'Kazakhstan Tenge',
            'KPW': 'Korea (North) Won',
            'KRW': 'Korea (South) Won',
            'KGS': 'Kyrgyzstan Som',
            'LAK': 'Laos Kip',
            'LVL': 'Latvia Lat',
            'LBP': 'Lebanon Pound',
            'LRD': 'Liberia Dollar',
            'LTL': 'Lithuania Litas',
            'MKD': 'Macedonia Denar',
            'MYR': 'Malaysia Ringgit',
            'MUR': 'Mauritius Rupee',
            'MXN': 'Mexico Peso',
            'MNT': 'Mongolia Tughrik',
            'MZN': 'Mozambique Metical',
            'NAD': 'Namibia Dollar',
            'NPR': 'Nepal Rupee',
            'ANG': 'Netherlands Antilles Guilder',
            'NZD': 'New Zealand Dollar',
            'NIO': 'Nicaragua Cordoba',
            'NGN': 'Nigeria Naira',
            'NOK': 'Norway Krone',
            'OMR': 'Oman Rial',
            'PKR': 'Pakistan Rupee',
            'PAB': 'Panama Balboa',
            'PYG': 'Paraguay Guarani',
            'PEN': 'Peru Nuevo Sol',
            'PHP': 'Philippines Peso',
            'PLN': 'Poland Zloty',
            'QAR': 'Qatar Riyal',
            'RON': 'Romania New Leu',
            'RUB': 'Russia Ruble',
            'SHP': 'Saint Helena Pound',
            'SAR': 'Saudi Arabia Riyal',
            'RSD': 'Serbia Dinar',
            'SCR': 'Seychelles Rupee',
            'SGD': 'Singapore Dollar',
            'SBD': 'Solomon Islands Dollar',
            'SOS': 'Somalia Shilling',
            'ZAR': 'South Africa Rand',
            'LKR': 'Sri Lanka Rupee',
            'SEK': 'Sweden Krona',
            'CHF': 'Switzerland Franc',
            'SRD': 'Suriname Dollar',
            'SYP': 'Syria Pound',
            'TWD': 'Taiwan New Dollar',
            'THB': 'Thailand Baht',
            'TTD': 'Trinidad and Tobago Dollar',
            'TRY': 'Turkey Lira',
            'TRL': 'Turkey Lira',
            'TVD': 'Tuvalu Dollar',
            'UAH': 'Ukraine Hryvna',
            'GBP': 'United Kingdom Pound',
            'USD': 'United States Dollar',
            'UYU': 'Uruguay Peso',
            'UZS': 'Uzbekistan Som',
            'VEF': 'Venezuela Bolivar',
            'VND': 'Viet Nam Dong',
            'YER': 'Yemen Rial',
            'ZWD': 'Zimbabwe Dollar'}
        sentence = word_tokenize(sentence)
        for i in range(len(sentence)):
            if (sentence[i] in currency_dict):
                cur=sentence[i]
                term_dict= self.update_doc_dict(term_dict,cur)
                term_dict=self.update_doc_dict(term_dict,currency_dict[cur])
                curr_lst.append(cur,currency_dict[cur])
                self.update_global_dict(cur)
                self.update_global_dict(currency_dict[cur])
            elif(sentence[i] in currency_dict.values()):
                cur = sentence[i]
                term_dict = self.update_doc_dict(term_dict, cur)
                term_dict = self.update_doc_dict(term_dict, currency_dict[cur])
                curr_lst.append(cur, currency_dict[cur])
                self.update_global_dict(cur)
                self.update_global_dict(currency_dict[cur])
        for word in curr_lst:
            self.update_global_dict(word)
