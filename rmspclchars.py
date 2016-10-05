
# coding: utf-8

# In[30]:

import re


# In[31]:


string = open('filename.txt').read()
new_str = re.sub('[^a-zA-Z0-9\n\.]', ' ', string)
open('filename.txt', 'w').write(new_str)


# In[ ]:



