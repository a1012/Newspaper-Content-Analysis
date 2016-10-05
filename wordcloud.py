
# coding: utf-8

# In[7]:

#!/usr/bin/env python
import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import random

from wordcloud import WordCloud, STOPWORDS


# In[20]:

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):

    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

d = path.dirname('__filename__')

# open the file containing the the text
text = open(path.join(d, "filename.txt")).read()


# adding category specific stopwords
stopwords = set(STOPWORDS)

wc = WordCloud(max_words=1000, stopwords=stopwords, margin=10,
               random_state=6).generate(text)

# store default colored image
default_colors = wc.to_array()
plt.title("Custom colors")
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3))
wc.to_file("filename.png")
plt.axis("off")
plt.figure()
plt.title("Default colors")
plt.imshow(default_colors)
plt.axis("off")
plt.show()


# In[ ]:



