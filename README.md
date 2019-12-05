# SCOTUS-Embedding

This Project focuses on processing legal court decisions and is part of on-going research at New York University. This code is in development and is not ready for public release. Initially, we are using github as a version-control and development tool.

## Description
There are 4 task in general we need to do:
  1. without citation
  2. citation with two class (legislation and case)
  3. citation with entry_type
  4. citation with specific case (global_level_id in .NYU_IE4 file)
  
## TODO

- Analyze the scotus online dataset. Try to download the label, and map them to local text.
- Replace the citation in the document with new word/tag, and build a new dictionary accordingly.
- Task 2/3: Train a word embedding using new dictionary (fastText)
- Use embedding to train classification model in different task



## Work
1. Incorporate paragraph citation information.

## Port Forwarding

- Connect to NYU access server first.
- ```
  ssh -L 7000:localhost:3000 grice.cs.nyu.edu     # Now we go to the grice server.
  screen                                          # You must execute this line first then change the location.
  cd /misc/grice1/yijun/SCOTUS-Embedding
  jupyter notebook --ip='*' --no-browser          # Then we can access jupyter by typing 'localhost:8000' in laptop.
  ```



