import parser_module
import search_engine

from IR_Search_Engine.Search_Engine.parser_module import Parse

if __name__ == '__main__':
    par=Parse()
    a = par.Hashtags_parse("word world pip 5 percent sos #stay_At_Home")
    c=2
    search_engine.main()
