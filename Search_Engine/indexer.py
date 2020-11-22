
class Indexer:

    def __init__(self, config):

        self.inverted_idx={}
        self.postingDict={}
        self.config = config

    def add_new_doc(self, document,dict):
        """
        This function perform indexing process for a document object.
        Saved information is captures via two dictionaries ('inverted index' and 'posting')
        :param document: a document need to be indexed.
        :return: -
        """
        self.inverted_idx = dict
        document_dictionary = document.term_doc_dictionary
        # Go over each term in the doc
        terms=document_dictionary.keys()
        count=0
        for term in terms:
          # Update inverted index and posting
          self.update_posting_file(term, count,document.tweet_id)
          count+=1



    def update_posting_file(self, term, idx, tweet_id):
            """
            this function updating the posting file with new data about the term
            :param term: the term we want to update
            :idx: the index of the term in the twit
            :return:
            """
            if (term not in  self.inverted_idx):
                return

            if term in self.postingDict:
                details_lst = self.postingDict[term]
                for i in details_lst:
                    if details_lst[i][0] == tweet_id:
                        details_lst[i][1] += 1
                        details_lst[i][2].append(idx)
                        self.postingDict[term] = details_lst
            else:
                self.postingDict[term] = [tweet_id, 1, [idx]]
