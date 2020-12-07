import math
class Ranker:
    def __init__(self):
        pass

    @staticmethod
    def rank_relevant_doc(relevant_doc,query_len=0):
        """
        this function rank the relavant docs by cosSim method
        :param relevant_doc: a tuple with data about the terms in the query
        :param query_len: the length of the query
        :return: sorted list of tweetID ,sorted by rank--> cosSim
        """
        docs_dict = {}
        sum_Wiq = relevant_doc[1]
        count_terms = relevant_doc[2]
        relevant_doc=relevant_doc[0]
        for term in relevant_doc:
            numShowsInQuery = count_terms[term.lower()]
            for tweet in relevant_doc[term]:
                numTweet=tweet[0]
                tf=tweet[1]
                idf=tweet[2]
                if (numTweet not in docs_dict):
                    docs_dict[numTweet] = [tf * idf * numShowsInQuery, (tf * idf) ** 2]
                else:
                    docs_dict[numTweet] = [docs_dict[numTweet][0] + (tf * idf*numShowsInQuery),
                                   docs_dict[numTweet][1] + ((tf * idf) ** 2)]

        doc_lst = []
        for doc in docs_dict:
            cosSim = (docs_dict[doc][0]) / (math.sqrt(docs_dict[doc][1] * sum_Wiq))
            doc_lst.append((doc, cosSim))
        return sorted(doc_lst, key=lambda x: x[1] ,reverse=True)


    @staticmethod
    def retrieve_top_k(sorted_relevant_doc, k=1):
        """
        return a list of top K tweets based on their ranking from highest to lowest
        :param sorted_relevant_doc: list of all candidates docs.
        :param k: Number of top document to return
        :return: list of relevant document
        """
        return sorted_relevant_doc[:k]



