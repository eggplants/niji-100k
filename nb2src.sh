#!/bin/bash

jupyter nbconvert --to script gen.ipynb
cat <<<"$(sed '/get_ipython()\.system(/d' gen.py)" >gen.py
