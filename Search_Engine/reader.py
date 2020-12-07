import os
import pandas as pd
from pathlib import Path

class ReadFile:
    def __init__(self, corpus_path):
        self.corpus_path = corpus_path

    def read_file(self, file_name):
        """
        This function is reading a parquet file contains several tweets
        The file location is given as a string as an input to this function.
        :param file_name: string - indicates the path to the file we wish to read.
        :return: a dataframe contains tweets.
        """
        full_path = os.path.join(self.corpus_path, file_name)
        df = pd.read_parquet(full_path, engine="pyarrow")
        return df.values.tolist()

    def find_paths(self):
        doc_list=[]
        entries = Path(self.corpus_path)
        for entry in entries.iterdir():
            if (entry.is_dir()):
                for inner_entry in entry.iterdir():
                    if (Path(inner_entry).suffix == '.parquet'):
                        doc_list.append(inner_entry.parent.name+"\\"+inner_entry.name)

        return doc_list