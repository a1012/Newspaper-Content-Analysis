
# coding: utf-8

# In[2]:

from __future__ import division
import sys
import nltk
from nltk.corpus import wordnet as wn
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
#import pylab as plt
import pygraphviz
#from dask.dot import dot_graph
import matplotlib.pyplot as plt



# In[3]:

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
fp = open("/home/aayushi/projectdp/cleandata10.txt")
data = fp.read()

#to tokenize input text into sentences

print ('\n-----\n'.join(tokenizer.tokenize(data)))# splits text into sentences

#to tokenize the tokenized sentences into words

tokens = nltk.wordpunct_tokenize(data)
text = nltk.Text(tokens)
words = [w.lower() for w in text]  
print (words)     #to print the tokens

for a in words:
    syns = wn.synsets(a)
    print ("synsets:", syns)

   # for s in syns:
         #for l in s.lemmas:
             #print (l.name)
         #print (s.definition)
         #print (s.examples)


# In[6]:

get_ipython().magic('matplotlib nbagg')
def closure_graph(synset, fn):
    seen = set()
    graph = nx.DiGraph()
 
    def recurse(s):
        if not s in seen:
            seen.add(s)
            graph.add_node(s.name)
            for s1 in fn(s):
                graph.add_node(s1.name)
                graph.add_edge(s.name, s1.name)
                recurse(s1)
    recurse(synset)
    return graph
murder = wn.synset('murder.n.01')
graph = closure_graph(murder,lambda s: s.hypernyms())
pos = graphviz_layout(graph)
nx.draw_networkx_nodes(graph,pos,node_size=80,node_color='w',alpha=0.2)
nx.draw_networkx_edges(graph,pos,alpha=0.8,node_size=1,width=1,edge_color='b')

# Label style variables...
nx.draw_networkx_labels(graph,pos,fontsize=14)
font = {'fontname'   : 'Helvetica',
    'color'      : 'k',
    'fontweight' : 'bold',
    'fontsize'   : 14}
 
# Figure style variables...
plt.title("Visualizing WordNet relationships as graphs", font)
plt.axis('off')
plt.show()
 


# In[25]:


# Base code from randomhacks
def closure_graph(synset, fn):
    seen = set()
    graph = nx.DiGraph()
 
    def recurse(s):
        if not s in seen:
            seen.add(s)
            graph.add_node(s.name)
            for s1 in fn(s):
                graph.add_node(s1.name)
                graph.add_edge(s.name, s1.name)
                recurse(s1)
    recurse(synset)
    return graph
 
#My UI modifications
#try: 
    #input = raw_input
    #word = raw_input('reject.v.01')
    #print ("You entered: '%s'" % word)
 
word_synsets = []
try:
    wn_word = wn.synsets('reject.v.01')
    #print wn_word
    print ("Choose a Synset of your entry, '%s'" % (word,))
    for i,w in enumerate(wn_word):
        #import pdb; pdb.set_trace()
        print ("{0}) '{1}' -- definition: '{2}'".format(i,w.name,w.definition))
except Exception:
    print ('Please enter only one word')
    
   
 
# Store method call and description in one variable as a list of tuples...
sel_relation = [ 
    ('root_hypernyms','The most abstract/general containing class for A'),
    ('hyponyms','A is a hyponym of B iff B is a type of A'),
    ('member_holonyms','A is a member holonym of B iff B-type things are member of A-type things'),
    ('substance_holonyms','A is a substance holonym of B iff B-type things are constituted of A-type things'),
    ('part_holonyms','A is a part holonym of B iff B-type things are subparts of A-type things'),
    ('member_meronyms','A is a member meronym of B iff A-type things are members of B-type things'),
    ('substance_meronyms','A is a substance meronym of B iff A-type things are consisted of B-type things'),
    ('part_meronyms','A is a part meronym of B iff A-type things are parts of B-type things')
]
 
for j,z in enumerate(sel_relation):
    print ("%s) '%s' -- %s." % (j,z[0],z[1]))
    
try:
    try: input = raw_input
        jj = wn_word
        jj = raw_input('Your selection:reject.v.01 ')
        Basic form of the call generating the graph,
        graph = closure_graph(wn_word_s, lambda s: s.hypernyms())
        The rest of the code just works to manage the list of tuples...
        sel = sel_relation[int(jj)][0]
        print (sel)
        graph = closure_graph(wn_word_s, lambda s: s.hypernyms())
        except Exception:
            print ('Please enter only a number value from the list.')
 


# In[ ]:

""""

try:
   p = raw_input('Your selection:woman.n.01 ')
   wn_word = wn.synsets(word)[int(p)].name
   print (wn_word)    
   wn_word_s = wn.synset(wn_word)
except Exception:
   print ('Please enter only a number value from the list.')
   
   """"


# In[ ]:

# Here is the code to print the graph with correction for the bug...
from networkx.drawing.nx_agraph import graphviz_layout
pos = graphviz_layout(graph)
 
# Explicitly set some drawing variables:
# Notes and Edge style variables...
nx.draw_networkx_nodes(graph,pos,node_size=50,node_color='w',alpha=0.4)
nx.draw_networkx_edges(graph,pos,alpha=0.4,node_size=0,width=1,edge_color='m')
 
# Label style variables...
nx.draw_networkx_labels(graph,pos,fontsize=14)
font = {'fontname'   : 'Helvetica',
    'color'      : 'k',
    'fontweight' : 'bold',
    'fontsize'   : 14}
 
# Figure style variables...
plt.title("Visualizing WordNet relationships as graphs", font)
plt.axis('off')
 
plt.show()
 

