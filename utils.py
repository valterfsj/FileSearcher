
import glob, os
#import time
from tika import parser
import tika

def searcher(root_path = None , file_types = None,search_str=None):
    if root_path is not None and file_types is not None and search_str is not None:
        files_list = []
        for ftype in file_types:
            print('------------------------------------------------------------------------------------')
            print('Parsing for '+ftype+' documents')
            print('------------------------------------------------------------------------------------')
            for fname in glob.glob(root_path+'*'+ftype,recursive=True):
                aux = 0
                tika.TikaClientOnly = True
                try:
                    document = parser.from_file(fname)
                    document_text = document['content']
                    document_text = document_text.lower()
                except:
                   print('Corrupted File: '+ str(fname))
                   aux = -1
                if aux == 0:   
                    for word in search_str:
                        if aux == 0:
                            if word in document_text:
                               files_list.append(str(os.path.abspath(fname))+',')
                               print(word + ' Found in '+ fname)
                               aux = 1
        print('End of parse')
        return files_list
    else:
        print('Not Enought Arguments')
        return -1
