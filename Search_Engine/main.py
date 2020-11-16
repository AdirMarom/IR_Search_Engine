import parser_module
import search_engine

from IR_Search_Engine.Search_Engine.parser_module import Parse

if __name__ == '__main__':
    par=Parse()
    #a = par.Hashtags_parse("word world pip 5 percent sos #stay_At_Home")
    a=par.parse_sentence("word world pip 5 percent sos #stay_At_Home")
    D = par.parse_sentence("word world pip 5% sos #stay_At_Home")
    Z = par.parse_sentence("word orld pip 5 Percent sos #stay_At_Home")
    c=2
    b="abc_".isalpha()
    b = "abc1".isalpha()
    b = "!abc1".isalpha()
    search_engine.main()
