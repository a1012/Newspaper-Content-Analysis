# Newspaper Content analysis:
Scraping the contents of the front pages of the newspaper "The Hindu." This
project aims to obtain the text in the front pages of this newspaper from
the years 2006 to 2016. More specifically, in the first phase, it fetches
only the front page contents of papers dated Jan1 for eleven  
consecutive years - 2006 to 2016.

# DataSet:
The exercise is to analyze the text content and find the word frequencies,
categorize the words, and determine the visceral feel of the contents of
front pages of this newspaper.
One can access the front page HTML with the URLs formed in the following manner:
http://www.thehindu.com/todays-paper/tp-index/?date=2006-01-01
...
http://www.thehindu.com/todays-paper/tp-index/?date=2014-01-01
http://www.thehindu.com/todays-paper/tp-index/?date=2015-01-01
http://www.thehindu.com/todays-paper/tp-index/?date=2016-01-01

Notice that these URLS vary only in their 'date' argument.One may use 'curl' to access the Web page content.
# Tools:
Curl-for extracting the  given URLs.
Python
Mysql
D3-for visualization.



