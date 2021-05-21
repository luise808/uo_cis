import pandas as pd

import spacy

import en_core_web_md  #1M words in dictionary
nlp = en_core_web_md.load() 

def remove_list_item(*,the_list,the_item):#creates a new list w/o the item removing
  new_list = [item for item in the_list if item != the_item]
  return new_list

def plot_x_by_class_y(*, table, x_column, y_column):
  assert isinstance(table, pd.core.frame.DataFrame), f'table is not a dataframe but instead a {type(table)}'
  assert x_column in table.columns, f'unrecognized column: {x_column}. Check spelling and case.'
  assert y_column in table.columns, f'unrecognized column: {y_column}. Check spelling and case.'
  assert table[y_column].nunique()<=5, f'y_column must be of 5 categories or less but has {table[y_column].nunique()}'

  pd.crosstab(table[x_column], table[y_column]).plot(kind='bar', figsize=(15,8), grid=True, logy=True)
  return None

def mcc(*, tp, tn, fp, fn):
  mcc_score = (tp*tn-fp*fn)/((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn))**.5
  return mcc_score

def wrangle_text(*,essay): #essay needs to be a string
  doc = nlp(essay)
  essay_wrangle = [essay.text.lower() for essay in doc if not essay.is_stop and not essay.is_oov and essay.is_alpha]
  return essay_wrangle

def precision(*,tp,fp):
  pre = tp/(tp+fp)
  return pre

def recall(*,tp,fn):
  rec = tp/(tp,fn)
  
def accuracy(*,tp,fp,tn,fn):
  acc = (tp+tn)/(tp+tn+fp+fn)
  return acc
  
def f1(*, tp, fp, fn):
  f1_num = (2*tp)/(2*tp + fp + fn)
  return f1_num
