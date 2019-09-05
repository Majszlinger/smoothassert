# smoothassert

This Package contains two custom Assertion methods to compare Pandas.Series objects.
1. AssertSimilarSeries
2. Assert_Cos_Sim_Series


## Install

Grab the package using `pip` (this could take a few minutes)
Try using one of the following:

     pip install pip install -i https://test.pypi.org/simple/ smoothassert

## Getting Started

Import the module

    import smoothassert.smoothassert

Or
Import the method what you want to use directly
```python
from smoothassert.smoothassert import AssertSimilarSeries
```

## Features

### 1. AssertSimilarSeries
The use of this method is to check that left and right Series are Equal, or similar with the given error rate.
The main usage of this method is to use it where you don't want or not able to make a code what works with 0% error rate i.e.: Machine learning models. Because the basic assertions in given in the common packages only have the AssertEqual methods what looks for 100% equality. If you have a Machine learning model what you want to have 80% precision then you can call this method to test it and its not going to raise Assertion error unless there is more error in the output stream.

```python
   import pandas as pd
from smoothassert.smoothassert import AssertSimilarSeries

A = pd.Series(['a','b','c','d','e'])
B = pd.Series(['b','b','c','d','e'])

AssertSimilarSeries(A,B)

Output:
AssertionError: Series are diferent in 20.0% while the allowable limit is 0%
```
But if we raise the error limitation:
```python
   import pandas as pd
from smoothassert.smoothassert import AssertSimilarSeries

A = pd.Series(['a','b','c','d','e'])
B = pd.Series(['b','b','c','d','e'])

AssertSimilarSeries(A,B,percent=0.2)

Output:
OK, error rate:20.0
```
Probably you going to use a unittest framework to test your code, what is perfectly fine and its going to work with it as well.
### 2. Assert_Cos_Sim_Series
## Documantation
1. AssertSimilarSeries
Check that left and right Series are Equal, or similar with the given error rate. 
+ s1 Series
+ s2 Series
+ percent: int between 0 and 1 default 0
the allowable limit of the errors between the series given in percentage/100
+ check_series_type : bool, default True
Whether to check the Series class is identical.
+ check_names : bool, default True
Whether to check the Series and Index names attribute.
+ check_dtype : bool, default True
        Whether to check the Series dtype is identical.

