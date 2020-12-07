from nltk.stem import PorterStemmer


class Stemmer:
    def __init__(self):
        self.stemmer = PorterStemmer()

    def stem_term(self, text):
        """
        This function stem a token
        :param token: string of a token
        :return: stemmed token
        """
        for i in range(len(text)):
            text[i]=self.stemmer.stem(text[i])
        return text
