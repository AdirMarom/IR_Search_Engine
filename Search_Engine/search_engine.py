import csv
import datetime
import os
import shutil
from pathlib import Path
from reader import ReadFile
from configuration import ConfigClass
from parser_module import Parse
from indexer import Indexer
from searcher import Searcher
import utils
from Glove import Glove


def run_engine(corpus_path,output_path,stemming):
    '''
    this function doing parsing to the data and index the data
    :param corpus_path: the path of the corpus
    :param output_path: the path that inverted dict will be save
    :param stemming:  boolean who determine to activate stemmer or not
    :return:
    '''
    number_of_documents = 0
    config = ConfigClass()
    r = ReadFile(corpus_path)
    p = Parse()
    indexer = Indexer(config)
    doc_list=r.find_paths()
    for i in range (len(doc_list)):
        tmp_list=r.read_file(file_name=doc_list[i])
        for idx, document in enumerate(tmp_list):
            number_of_documents += 1
            parsed_document = p.parse_doc(document,stemming)
            if(number_of_documents%1000000==0):
                p.get_entity_dict()
                indexer.update_index_data(p.get_global_dict(), p.get_posting_dict())
    if(len(p.global_dict)>0):
        p.get_entity_dict()
        indexer.update_index_data(p.get_global_dict(), p.get_posting_dict())
    indexer.merge_all_posts_dict()

    global num_of_tweets
    num_of_tweets=number_of_documents


def load_index():
    return utils.load_inverted_index()


def search_and_rank_query(query, k):
    '''
    :param query:
    :param k:
    :return:  k most relevent docs about the query
    '''
    p = Parse()
    query_as_list = p.tokenized_parse(query)
    searcher = Searcher()
    searcher.set_num_of_docs(num_of_tweets)
    relevant_docs = searcher.relevant_docs_from_posting(query_as_list)
    ranked_docs = searcher.ranker.rank_relevant_doc(relevant_docs,len(query_as_list))
    return searcher.ranker.retrieve_top_k(ranked_docs, k)


def read_query_txt(queries_path):
    '''
    this function extract the queries from text
    :param queries_path:
    :return: list of queries
    '''
    f = open(queries_path, encoding="utf8")
    lst = []
    for line in f.readlines():
        if len(line) > 0:
            line = line[3:]
            line = line.replace("\n", '')
            if(len(lst)>=1):
                lst.append(line)
    lst.remove('')
    return lst

def move_to_output(output):
    '''
    this function move the posting dicts to the output path
    :param output:
    :return:
    '''
    source_dir = 'post_dicts'
    target_dir = output
    entries = Path(source_dir)
    for entry in entries.iterdir():
        if (entry.is_dir()):
            for inner_entry in entry.iterdir():
                try:
                    shutil.move(os.path.join(inner_entry), target_dir)
                except:
                    os.remove(target_dir+'\\'+inner_entry.name)
                    shutil.move(os.path.join(inner_entry), target_dir)


def main(corpus_path, output_path, stemming, queries, num_docs_to_retrieve):
    '''
    corpus_path - the path to the corpus
    output_path - the path of the posting files will be save
    stemming - True if user want stemming , otherwise False
    queries- can be list with the queries inside or can be a text file with the queries
    num_docs_to_retrieve .
    '''
    run_engine(corpus_path,output_path,stemming)
    data_list=[]
    if(type(queries)!=list):
        queries=read_query_txt(queries)
    for i in range(len(queries)):
        for doc_tuple in search_and_rank_query(queries[i],num_docs_to_retrieve):
            print('Tweet id: {} Score: {}'.format({doc_tuple[0]}, {doc_tuple[1]}))
            data_list.append(["query: "+str(i),doc_tuple[0],doc_tuple[1]])
        with open('results.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerows(data_list)
    move_to_output(output_path)








