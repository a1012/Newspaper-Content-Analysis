
# coding: utf-8

# In[6]:

from matplotlib import pylab
from nltk.text import Text
from nltk.corpus import gutenberg
import csv


# In[29]:

def plot_word_freq_dist(text):
    fd = text.vocab()
    get_ipython().magic('matplotlib nbagg')
    samples = [item for item, _ in fd.most_common(50)]
    values = [fd[sample] for sample in samples]
    values = [sum(values[:i+1]) * 1000.0/fd.N() for i in range(len(values))]
    pylab.title(text.name)
    pylab.xlabel("words")
    pylab.ylabel("Frequencies")
    pylab.plot(values)
    pylab.xticks(range(len(samples)), [str(s) for s in samples], rotation=90)
    pylab.show()

def app():
    t1 = Text(gutenberg.words('filename.txt'))
    plot_word_freq_dist(t1)

if __name__ == '__main__':
    app()

__all__ = ['app']


# In[ ]:



