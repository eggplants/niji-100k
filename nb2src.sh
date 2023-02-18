#!/bin/bash

jupyter nbconvert --to script gen.ipynb
cat <<<"$(sed '/get_ipython()\.system(/d' gen.py)" >gen.py

awk '$0 == "# In[ ]:"{print"# In["a++"]"}$0 != "# In[ ]:"{print$0}' gen.py > _
mv _ gen.py
