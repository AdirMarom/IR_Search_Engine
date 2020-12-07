import json
import pickle


def save_obj(obj, name):
    """
    This function save an object as a pickle.
    :param obj: object to save
    :param name: name of the pickle file.
    :return: -
    """
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    """
    This function will load a pickle file
    :param name: name of the pickle file
    :return: loaded pickle file
    """
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

def load_inverted_index(output_path=False):
    files_names=['else','a',"bc",'d','e','fg','h','i','jm','n','o','pq','r','s','t','u','vz']
    dict={}
    try:
        for word in files_names:
            inv_dict=open_inverted(word+'\\'+word+'0_inverted_idx.json')
            for term in inv_dict:
                dict[term]=inv_dict[term]
    except:
        print("can't open a inverted file in utils")
    return dict


def open_inverted(path):
    with open("inv_dicts\\" + path) as infile:
        inv_dict = json.load(infile)
    return inv_dict