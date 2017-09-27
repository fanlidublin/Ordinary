library(wordcloud)
library(tm)
wordcloud("May our children and our children's children to a thousand generations, continue to enjoy the benefits conferred upon us by a united country, and have cause yet to rejoice under those glorious institutions bequeathed us by Washington and his compeers.",colors=brewer.pal(6,"Dark2"),random.order=FALSE)


wordcloud("I am writing this file to test the function of word cloud package in practical 3 of the module text analytics. The module text analytics mainly talks about the techniques used in text analytics, which are commonly used to discover meaning in text nowadays. Now, try to repeat word: techniques, techniques, techniques, techniques, techniques.",colors=brewer.pal(6,"Dark2"),random.order=FALSE)

wordcloud("I am writing this file to test the function of word cloud package in practical 3 of the module text analytics. The module text analytics mainly talks about the techniques used in text analytics, which are commonly used to discover meaning in text nowadays. Now, try to repeat word: techniques, techniques, techniques, techniques, techniques.", minfreq=1, colors=brewer.pal(6,"Dark2"),random.order=TRUE)
