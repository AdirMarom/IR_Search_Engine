import json
import os

class Indexer:

    def __init__(self, config):
        self.config = config
        self.inv_count = 0 #num for file inverted
        self.post_count = 0  #num for file post

        ## 17 dict for inverted index
        self.a_inverted_idx = {}
        self.bc_inverted_idx = {}
        self.d_inverted_idx = {}
        self.e_inverted_idx = {}
        self.fg_inverted_idx = {}
        self.h_inverted_idx = {}
        self.i_inverted_idx = {}
        self.jm_inverted_idx = {}
        self.n_inverted_idx = {}
        self.o_inverted_idx = {}
        self.pq_inverted_idx = {}
        self.r_inverted_idx = {}
        self.s_inverted_idx = {}
        self.t_inverted_idx = {}
        self.u_inverted_idx = {}
        self.vz_inverted_idx = {}
        self.else_inverted_idx = {}

        ## 17 dict for posting index
        self.a_post_dict = {}
        self.bc_post_dict = {}
        self.d_post_dict = {}
        self.e_post_dict = {}
        self.fg_post_dict = {}
        self.h_post_dict = {}
        self.i_post_dict = {}
        self.jm_post_dict = {}
        self.n_post_dict = {}
        self.o_post_dict = {}
        self.pq_post_dict = {}
        self.r_post_dict = {}
        self.s_post_dict = {}
        self.t_post_dict = {}
        self.u_post_dict = {}
        self.vz_post_dict = {}
        self.else_post_dict = {}


    def load_curr_dict(self, name, type):
        """
        name: the letter that the dict start
        type: inverted / posting
        return: the correct dict
        """

        if (name == 'a'):
            if (type == 'inverted'):
                return self.a_inverted_idx
            return self.a_post_dict
        elif (name == 'bc'):
            if (type == 'inverted'):
                return self.bc_inverted_idx
            return self.bc_post_dict
        elif (name == 'd'):
            if (type == 'inverted'):
                return self.d_inverted_idx
            return self.d_post_dict
        elif (name == 'e'):
            if (type == 'inverted'):
                return self.e_inverted_idx
            return self.e_post_dict
        elif (name == 'fg'):
            if (type == 'inverted'):
                return self.fg_inverted_idx
            return self.fg_post_dict
        elif (name == 'h'):
            if (type == 'inverted'):
                return self.h_inverted_idx
            return self.h_post_dict
        elif (name == 'i'):
            if (type == 'inverted'):
                return self.i_inverted_idx
            return self.i_post_dict
        elif (name == 'jm'):
            if (type == 'inverted'):
                return self.jm_inverted_idx
            return self.jm_post_dict
        elif (name == 'n'):
            if (type == 'inverted'):
                return self.n_inverted_idx
            return self.n_post_dict
        elif (name == 'o'):
            if (type == 'inverted'):
                return self.o_inverted_idx
            return self.o_post_dict
        elif (name == 'pq'):
            if (type == 'inverted'):
                return self.pq_inverted_idx
            return self.pq_post_dict
        elif (name == 'r'):
            if (type == 'inverted'):
                return self.r_inverted_idx
            return self.r_post_dict
        elif (name == 's'):
            if (type == 'inverted'):
                return self.s_inverted_idx
            return self.s_post_dict
        elif (name == 't'):
            if (type == 'inverted'):
                return self.t_inverted_idx
            return self.t_post_dict
        elif (name == 'u'):
            if (type == 'inverted'):
                return self.u_inverted_idx
            return self.u_post_dict
        elif (name == 'vz'):
            if (type == 'inverted'):
                return self.vz_inverted_idx
            return self.vz_post_dict
        elif (name == 'else'):
            if (type == 'inverted'):
                return self.else_inverted_idx
            return self.else_post_dict

    def update_global_inverted_dict(self, name):
        '''
        this function get some terms and save data about the terms in inverted index
        :param dict: dictionary with limited number of terms
        :return:
        '''
        local_dict = self.load_curr_dict(name, "inverted")
        file_name = "inv_dicts\\" + name + "\\" + name + str(self.inv_count) + '_inverted_idx.json'
        file_letter = "inv_dicts\\" + name
        file_inv = 'inv_dicts'
        if len(local_dict) < 1:
            return
        if not os.path.isdir(file_inv):
            os.mkdir(file_inv)
        if not os.path.isdir(file_letter):
            os.mkdir(file_letter)
        with open(file_name, 'w') as outfile:
            json.dump(local_dict, outfile)
        local_dict.clear()
        return

    def update_locals_inverted_dicts(self, dict):
        """
        dict: key : term : # number of doc
        for all term save in the correct dit
        """
        for dict_term in dict:
            if len(dict_term) < 1:
                continue
            if (dict_term.isalpha() == False):
                self.else_inverted_idx[dict_term] = dict[dict_term]
                continue
            if 'a' == dict_term[0].lower():
                inv_dict = self.a_inverted_idx
            elif 'b' <= dict_term[0].lower() <= 'c':
                inv_dict = self.bc_inverted_idx
            elif 'd' == dict_term[0].lower():
                inv_dict = self.d_inverted_idx
            elif 'e' == dict_term[0].lower():
                inv_dict = self.e_inverted_idx
            elif 'f' <= dict_term[0].lower() <= 'g':
                inv_dict = self.fg_inverted_idx
            elif 'h' == dict_term[0].lower():
                inv_dict = self.h_inverted_idx
            elif 'i' == dict_term[0].lower():
                inv_dict = self.i_inverted_idx
            elif 'j' <= dict_term[0].lower() <= 'm':
                inv_dict = self.jm_inverted_idx
            elif 'n' == dict_term[0].lower():
                inv_dict = self.n_inverted_idx
            elif 'o' == dict_term[0].lower():
                inv_dict = self.o_inverted_idx
            elif 'p' <= dict_term[0].lower() <= 'q':
                inv_dict = self.pq_inverted_idx
            elif 'r' == dict_term[0].lower():
                inv_dict = self.r_inverted_idx
            elif 's' == dict_term[0].lower():
                inv_dict = self.s_inverted_idx
            elif 't' == dict_term[0].lower():
                inv_dict = self.t_inverted_idx
            elif 'u' == dict_term[0].lower():
                inv_dict = self.u_inverted_idx
            elif 'v' <= dict_term[0].lower() <= 'z':
                inv_dict = self.vz_inverted_idx

            term = dict_term
            if str.isupper(dict_term[0]):
                inv_dict[term.upper()] = dict[dict_term]
            else:
                inv_dict[term.lower()] = dict[dict_term]

    def update_locals_posting_dicts(self, dict):
        """
        dict: key : term : data about the term
        for all term save in the correct dict
        """
        for dict_term in dict:
            if len(dict_term) < 1:
                continue
            if (dict_term.isalpha() == False):
                self.else_post_dict[dict_term.lower()] = dict[dict_term]
                continue
            if 'a' == dict_term[0].lower():
                post_dict = self.a_post_dict
            elif 'b' <= dict_term[0].lower() <= 'c':
                post_dict = self.bc_post_dict
            elif 'd' == dict_term[0].lower():
                post_dict = self.d_post_dict
            elif 'e' == dict_term[0].lower():
                post_dict = self.e_post_dict
            elif 'f' <= dict_term[0].lower() <= 'g':
                post_dict = self.fg_post_dict
            elif 'h' == dict_term[0].lower():
                post_dict = self.h_post_dict
            elif 'i' == dict_term[0].lower():
                post_dict = self.i_post_dict
            elif 'j' <= dict_term[0].lower() <= 'm':
                post_dict = self.jm_post_dict
            elif 'n' == dict_term[0].lower():
                post_dict = self.n_post_dict
            elif 'o' == dict_term[0].lower():
                post_dict = self.o_post_dict
            elif 'p' <= dict_term[0].lower() <= 'q':
                post_dict = self.pq_post_dict
            elif 'r' == dict_term[0].lower():
                post_dict = self.r_post_dict
            elif 's' == dict_term[0].lower():
                post_dict = self.s_post_dict
            elif 't' == dict_term[0].lower():
                post_dict = self.t_post_dict
            elif 'u' == dict_term[0].lower():
                post_dict = self.u_post_dict
            elif 'v' <= dict_term[0].lower() <= 'z':
                post_dict = self.vz_post_dict

            post_dict[dict_term.lower()] = dict[dict_term]

    def update_global_posting_dicts(self, name):
        '''
        this function get some terms and save data about the terms in posting dict
        :param dict: dictionary with limited number of terms
        :return:
        '''
        local_dict = self.load_curr_dict(name, "post")
        full_file_name = "post_dicts\\" + name + "\\" + name + str(self.post_count) + '_posting_dict.json'
        file_letter= "post_dicts\\" + name
        file_post='post_dicts'
        # if (post_dict == None):
        if len(local_dict) < 1:
            return
        if not os.path.isdir(file_post):
            os.mkdir(file_post)
        if not os.path.isdir(file_letter):
            os.mkdir(file_letter)
        with open(full_file_name, 'w') as outfile:
            json.dump(local_dict, outfile)
        local_dict.clear()
        return

    def update_index_data(self, invert_dict, post_dict):
        """
         activate the update func for post and inv
        """
        if len(invert_dict) > 0:
            self.update_locals_inverted_dicts(invert_dict)
        if len(post_dict) > 0:
            self.update_locals_posting_dicts(post_dict)
        letter_lst = ["a", "bc", "d", "e", "fg", "h", "i", "jm", "n", "o", "pq", "r", "s", "t", "u", "vz", "else"]
        for letter in letter_lst:
            self.update_global_inverted_dict(letter)
            self.update_global_posting_dicts(letter)
        self.inv_count += 1
        self.post_count += 1

    def merge(self, A, B, f):
        # Start with symmetric difference; keys either in A or B, but not both
        merged = {k: A.get(k, B.get(k)) for k in A.keys() ^ B.keys()}
        # Update with `f()` applied to the intersection
        merged.update({k: f(A[k], B[k]) for k in A.keys() & B.keys()})
        return merged

    def merge_post_dicts(self, name):
        """
        name: the first char of the post dictionary
        marge every two dict two one
        """
        files_names = []
        for i in range(self.post_count):
            file_name = "post_dicts\\" + name + "\\" + name + str(i) + '_posting_dict.json'
            files_names.append(file_name)
        while (len(files_names) > 1):
            tmp_lst = []
            tmp_dict_1 = {}
            tmp_dict_2 = {}
            for i in range(0, len(files_names) - 1, 2):
                if i % 2 == 0:
                    tmp_lst.append(files_names[i])
                try:
                    with open(files_names[i]) as infile:
                        tmp_dict_1 = json.load(infile)
                    with open(files_names[i + 1]) as infile:
                        tmp_dict_2 = json.load(infile)
                    os.remove(files_names[i])
                    os.remove(files_names[i + 1])
                except:
                    return None

                tmp = self.merge(tmp_dict_1, tmp_dict_2, lambda a, b: a + b)
                with open(files_names[i], 'w') as outfile:
                    json.dump(tmp, outfile)
            if len(files_names) % 2 == 1:
                tmp_lst.append(files_names[-1])
            files_names = tmp_lst

    def merge_inv(self, A, B, f):
        # Start with symmetric difference; keys either in A or B, but not both
        merged = {k: A.get(k, B.get(k)) for k in A.keys() ^ B.keys()}
        upper_term = [term for term in merged if term.isupper()]
        for term in upper_term:
            if term.lower() in merged:
                merged[term.lower()] += merged[term]
                del merged[term]
        merged.update({k: f(A[k], B[k]) for k in A.keys() & B.keys()})
        return merged

    def merge_inv_dicts(self, name):
        """
        name: the first char of the inv dictionary
        marge every two dict two one

        """
        files_names = []
        for i in range(self.inv_count):
            file_name = "inv_dicts\\" + name + "\\" + name + str(i) + '_inverted_idx.json'
            files_names.append(file_name)
        while (len(files_names) > 1):
            tmp_lst = []
            tmp_dict_1 = {}
            tmp_dict_2 = {}
            for i in range(0, len(files_names) - 1, 2):
                if i % 2 == 0:
                    tmp_lst.append(files_names[i])
                try:
                    with open(files_names[i]) as infile:
                        tmp_dict_1 = json.load(infile)
                    with open(files_names[i + 1]) as infile:
                        tmp_dict_2 = json.load(infile)
                    os.remove(files_names[i])
                    os.remove(files_names[i + 1])
                except:
                    return None

                tmp = self.merge_inv(tmp_dict_1, tmp_dict_2, lambda a, b: a + b)
                with open(files_names[i], 'w') as outfile:
                    json.dump(tmp, outfile)
            if len(files_names) % 2 == 1:
                tmp_lst.append(files_names[-1])
            files_names = tmp_lst

    def merge_all_posts_dict(self):
        """
        active the the curr merge function for inverted dict and for posting dict
        """
        dict_name = ['a', 'bc', 'd', 'e', 'else', 'fg', 'h', 'i', 'jm', 'n', 'o', 'pq', 'r', 's', 't', 'u', 'vz']
        for name in dict_name:
            self.merge_post_dicts(name)
            self.merge_inv_dicts(name)
        self.post_count = 1
        self.inv_count = 1









