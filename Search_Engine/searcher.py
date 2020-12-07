import json
import math
from parser_module import Parse
from ranker import Ranker

class Searcher:

    def __init__(self):
        """
        :param inverted_index: dictionary of inverted index
        """
        self.parser = Parse()
        self.ranker = Ranker()
        self.num_of_docs=0

    def set_num_of_docs(self,num):
        self.num_of_docs=num

    def relevant_docs_from_posting(self, query):
        """
        this function collect a data for rank the documents ,do it by posting dicts and inverted dicts
        :param query:
        :return: terms dictionary, of relevant documents with correct data to ranker (tf,idf,numOfshowsInQuery).
        """
        query_count={}
        query_dict = {}
        letters_lst=[]
        for term in query:
            if term.lower() not in query_count:
                query_count[term.lower()]=1
            else:
                query_count[term.lower()] += 1
            if term[0].lower() not in letters_lst:
                letters_lst.append(term[0].lower())
        if 'a' in letters_lst:
            query_dict_a=self.open_relevant_dict("a\\a0_posting_dict.json","a\\a0_inverted_idx.json",query)
            query_dict=self.Merge(query_dict,query_dict_a)
        if 'b' in letters_lst or 'c' in letters_lst:
            query_dict_bc = self.open_relevant_dict("bc\\bc0_posting_dict.json","bc\\bc0_inverted_idx.json",query)
            query_dict = self.Merge(query_dict, query_dict_bc)
        if 'd' in letters_lst:
            query_dict_d = self.open_relevant_dict("d\\d0_posting_dict.json","d\\d0_inverted_idx.json",query)
            query_dict = self.Merge(query_dict, query_dict_d)
        if 'e' in letters_lst:
            query_dict_e = self.open_relevant_dict("e\\e0_posting_dict.json","e\\e0_inverted_idx.json",query)
            query_dict = self.Merge(query_dict, query_dict_e)
        if 'f' in letters_lst or 'g' in letters_lst:
            query_dict_fg = self.open_relevant_dict("fg\\fg0_posting_dict.json","fg\\fg0_inverted_idx.json",query)
            query_dict = self.Merge(query_dict, query_dict_fg)
        if 'h' in letters_lst:
            query_dict_h = self.open_relevant_dict("h\\h0_posting_dict.json","h\\h0_inverted_idx.json",query)
            query_dict = self.Merge(query_dict, query_dict_h)
        if 'i' in letters_lst:
            query_dict_i = self.open_relevant_dict("i\\i0_posting_dict.json","i\\i0_inverted_idx.json",query)
            query_dict = self.Merge(query_dict, query_dict_i)
        if 'j' in letters_lst or 'k' in letters_lst or 'l' in letters_lst or 'm' in letters_lst:
            query_dict_jm = self.open_relevant_dict("jm\\jm0_posting_dict.json","jm\\jm0_inverted_idx.json",query)
            query_dict = self.Merge(query_dict, query_dict_jm)
        if 'n' in letters_lst:
            query_dict_n = self.open_relevant_dict("n\\n0_posting_dict.json","n\\n0_inverted_idx.json",query)
            query_dict = self.Merge(query_dict, query_dict_n)
        if 'o' in letters_lst:
            query_dict_o = self.open_relevant_dict("o\\o0_posting_dict.json","o\\o0_inverted_idx.json",query)
            query_dict = self.Merge(query_dict, query_dict_o)
        if 'p' in letters_lst or 'q' in letters_lst:
            query_dict_pq = self.open_relevant_dict("pq\\pq0_posting_dict.json","pq\\pq0_inverted_idx.json",query)
            query_dict = self.Merge(query_dict, query_dict_pq)
        if 'r' in letters_lst:
            query_dict_r = self.open_relevant_dict("r\\r0_posting_dict.json","r\\r0_inverted_idx.json",query)
            query_dict = self.Merge(query_dict, query_dict_r)
        if 's' in letters_lst:
            query_dict_s = self.open_relevant_dict("s\\s0_posting_dict.json","s\\s0_inverted_idx.json",query)
            query_dict = self.Merge(query_dict, query_dict_s)
        if 't' in letters_lst:
            query_dict_t = self.open_relevant_dict("t\\t0_posting_dict.json","t\\t0_inverted_idx.json",query)
            query_dict = self.Merge(query_dict, query_dict_t)
        if 'u' in letters_lst:
            query_dict_u = self.open_relevant_dict("u\\u0_posting_dict.json","u\\u0_inverted_idx.json",query)
            query_dict = self.Merge(query_dict, query_dict_u)
        if 'v' in letters_lst or 'w' in letters_lst or 'x' in letters_lst or 'y' in letters_lst or 'z' in letters_lst:
            query_dict_vz = self.open_relevant_dict("vz\\vz0_posting_dict.json","vz\\vz0_inverted_idx.json",query)
            query_dict = self.Merge(query_dict, query_dict_vz)
        query_dict_else = self.open_relevant_dict("else\\else0_posting_dict.json","else\\else0_inverted_idx.json",query)
        query_dict = self.Merge(query_dict, query_dict_else)

        sum_Wiq=0
        for term in query_count:
            sum_Wiq+=query_count[term]**2
        return (query_dict,sum_Wiq,query_count) # term: tweet_ID,freq_in_tweet,tf,num_of_docs_term_shown


    def Merge(self,dict1, dict2):
        '''
        this function execute mergung of two dicts
        :param dict1:
        :param dict2:
        :return: merged dict
        '''
        if(dict1!=None and dict2!=None):
            for term in dict2:
                dict1[term]=dict2[term]
        return dict1


    def open_relevant_dict(self,post_name,inverted_name,query):
        '''
        this function searching words from the query in the dicts, and collect from them information
        :param post_name: the path to the posting file in the disk
        :param inverted_name: the path to the inverted file in the disk
        :param query:
        :return: terms dictionary with information about the docs they are shown
        '''
        dict={}
        with open("post_dicts\\"+post_name) as infile:
            post_dict = json.load(infile)
        with open("inv_dicts\\"+inverted_name) as infile1:
            inverted_dict=json.load(infile1)
        for term1 in query:
            term=term1.lower()
            if (term in post_dict):
                if term not in dict:
                    try:
                        num_of_shows = len(post_dict[term])
                    except:
                        num_of_shows=inverted_dict[term.upper()]
                    idf=math.log2(self.num_of_docs/num_of_shows)
                    lst=[]
                    for doc in post_dict[term]:
                        lst.append([doc[0],doc[2],idf])
                    dict[term]=lst #term: ([tweetID,tf,idf],[tweetID,tf,idf]...])
        file_dict=None
        return dict


