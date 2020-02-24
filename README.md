# SCOTUS-Embedding

This Project focuses on processing legal court decisions and is part of on-going research at New York University. This code is in development and is not ready for public release. Initially, we are using github as a version-control and development tool.

## Description
There are 4 task in general we need to do:
  1. embedding without citation
  2. embedding with citation divided into 2 class (legislation and case)
  3. embedding with citation divided by entry_type
  4. embedding with citation divided into specific case (global_level_id in .NYU_IE4 file)

----
Baseline paper: [A Comparative Study of Classifying Legal Documents with Neural Networks](https://www.researchgate.net/publication/327561122_A_Comparative_Study_of_Classifying_Legal_Documents_with_Neural_Networks)

## TODO

- Analyze the scotus online dataset. Try to download the label, and map them to local text.
- Replace the citation in the document with new word/tag, and build a new dictionary accordingly.
- Task 2/3: Train a word embedding using new dictionary (fastText)
- Use embedding to train a classification model in different task

## Dataset
```
Scotus (with NYU_IE4): /misc/grice1/meyers/appellate_courts/scotus_output

8k Washington (with case10 and legislation10): /misc/grice1/meyers/appellate_courts/UWash_scotus_output

citation dictionary: /home/meyers/Legal_Texts/scripts_2016/scotus_c_global_table_file.tsv

corresponding citation graph: /home/meyers/Legal_Texts/scripts_2016
```

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



