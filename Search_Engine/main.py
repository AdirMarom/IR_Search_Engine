import parser_module
import search_engine

if __name__ == '__main__':
    a = parser_module.Parse.Hashtags_parse("word world pip 5 percent sos #stay_At_Home")
    a=parser_module.Parse.Hashtags_parse("#stayAtHome")
    b=parser_module.Parse.percent_parse(" word world pip 5 percent sos")
    b = parser_module.Parse.percent_parse("5 percentage")
    b = parser_module.Parse.percent_parse("5%")
    b = parser_module.Parse.percent_parse("5 PERCENT")
    b = parser_module.Parse.percent_parse("5 PERCENTAGE")
    c=2
   ### search_engine.main()
