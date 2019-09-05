# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:06:16 2019

@author: Tamás


Custom Assertion functions for pandas
"""
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


from pandas.core.dtypes.common import (
    is_bool, is_categorical_dtype,is_number)


def AssertSimilarSeries(s1,s2,percent = 0,check_series_type=True,check_names=True,check_dtype=True):
    """
    Check that left and right Series are Equal, or similar with the given error rate.
    
    s1 Series
    s2 Series
    percent: int between 0 and 1 default 0
        the allowable limit of the errors between the series given in percentage/100
    check_series_type : bool, default True
        Whether to check the Series class is identical.
    check_names : bool, default True
    Whether to check the Series and Index names attribute.
    check_dtype : bool, default True
        Whether to check the Series dtype is identical.

    """
    _check_isinstance(s1, s2, pd.Series)
    #compare series type
    if check_series_type:
        assert isinstance(s1, type(s2))
    # length comparison
    if len(s1) != len(s2):
        msg1 = '{len}, {left}'.format(len=len(s1), left=s1.index)
        msg2 = '{len}, {right}'.format(len=len(s2), right=s2.index)
        msg = 'Series length are different'+ msg1+ msg2
        raise AssertionError(msg)
    # metadata comparison
    if check_names:
        assert_attr_equal('name', s1, s2)  
        
    if check_dtype:
        # We want to skip exact dtype checking when `check_categorical`
        # is False. We'll still raise if only one is a `Categorical`,
        # regardless of `check_categorical`
        if (is_categorical_dtype(s1) and is_categorical_dtype(s2)
#        and  not check_categorical
                ):
            pass
        else:
            assert_attr_equal('dtype', s1, s2)
#   count errors

#    c  = 0
#    for i in range(len(s1)):
#        if(s1[i]!=s2[i]):
#            c+=1
    c = (s1==s2).value_counts()[False]    
    err = c/len(s1)
    if(err>percent):
        raise AssertionError("Series are diferent in {err}% while the allowable limit is {percent}%".format(err = err*100,percent = percent*100))
    else:
        print("OK, error rate:{err}".format(err = err*100))

def Assert_Cos_Sim_Series(s1,s2,min_sim = 0):
    """
    Check that the cosine similarity between the elements of the two Series is bigger than the min_sim
    
    s1 Series
    s2 Series
    min_sim: int between 0 and 1 default 0(what means if there is at least one token has to be similar in each row)
    
        
    """
#TODO: Add check names etc.    
    
    
    
#TODO: Should it run throught all or raise eror at the first unnacceptable occurance??
    for i in range(len(s1)):
        corpus = [s1[i],s2[i]]
        TfidfVec = TfidfVectorizer()
        tfidf = TfidfVec.fit_transform(corpus)
        sim = cosine_similarity(tfidf[1],tfidf[0])[0][0]
        if(sim<min_sim):
            msg = 'on the {row}. row the similarity was less then the minimum: {min_sim}'.format(row=i,min_sim=min_sim)
            raise AssertionError(msg)
        else:
            print("OK")
    
          
    
def assert_attr_equal(attr, left, right):
    """checks attributes are equal. Both objects must have attribute.

    Parameters
    ----------
    attr : str
        Attribute name being compared.
    left : object
    right : object
    """
    __tracebackhide__ = True

    left_attr = getattr(left, attr)
    right_attr = getattr(right, attr)

    if left_attr is right_attr:
        return True
    elif (is_number(left_attr) and np.isnan(left_attr) and
          is_number(right_attr) and np.isnan(right_attr)):
        # np.nan
        return True

    try:
        result = left_attr == right_attr
    except TypeError:
        # datetimetz on rhs may raise TypeError
        result = False
    if not isinstance(result, bool):
        result = result.all()

    if result:
        return True
    else:
        msg = 'Attribute "{attr}" are different'.format(attr=attr)
        raise AssertionError(msg)


def _check_isinstance(left, right, cls):
    """
    Helper method for our assert_* methods that ensures that
    the two objects being compared have the right type before
    proceeding with the comparison.

    Parameters
    ----------
    left : The first object being compared.
    right : The second object being compared.
    cls : The class type to check against.

    Raises
    ------
    AssertionError : Either `left` or `right` is not an instance of `cls`.
    """

    err_msg = "{name} Expected type {exp_type}, found {act_type} instead"
    cls_name = cls.__name__

    if not isinstance(left, cls):
        raise AssertionError(err_msg.format(name=cls_name, exp_type=cls,
                                            act_type=type(left)))
    if not isinstance(right, cls):
        raise AssertionError(err_msg.format(name=cls_name, exp_type=cls,
                                            act_type=type(right)))
        