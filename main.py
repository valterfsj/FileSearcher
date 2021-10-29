#java -jar tika-server.jar --host=localhost --port=12345
from utils import searcher

search_str = ["goma","lavada","% etanol","MEV","SEM","quantidade","orgânicos","organicos","inorgânicos","inorganicos","caracterização","caracterizacão","caracterizaçao","depósitos","depositos","deposits","characterization","TGA" ]                
root_path = "./**/*/"
file_types = ['.pdf','.doc','.docx','.ppt','.pptx','.xls','.xlsx']

files_parsed = searcher(root_path,file_types,search_str)
with open('Parsed.txt','w',encoding="utf-8") as f:
    for line in files_parsed:
        f.write(line)
        f.write('\n')