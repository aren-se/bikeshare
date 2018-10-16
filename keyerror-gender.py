#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SEE READ ME FILE FIRST
"""


*** Most Popular Stations and Trip:
* Columbus Circle / Union Station was the most common starting station.
* Jefferson Dr & 14th St SW was the most common ending station.
*** Trip Duration:
* The total travel time for all trips in the selected data was
   *    8,613,095.218999999 minutes
   * or 5,981.0 days
   * or 16.0 years

* The mean travel time per trip for all trips in the selected data was 20 hours 16 minutes.
---------------------------------------- 


*** Bikeshare User Stats:
* Of 7,079 trips:
   * 5,286 (74%) were purchased by subscribers, and
   * 1,793 (25%) were purchased by non-subscribing customers.
Traceback (most recent call last):

  File "<ipython-input-7-f55e6e03c1f0>", line 1, in <module>
    runfile('/Users/arenhomefolder/Documents/DataAnalystnanodegree/2.x bikeshare-2/bikeshare_main_with_functions.py', wdir='/Users/arenhomefolder/Documents/DataAnalystnanodegree/2.x bikeshare-2')

  File "/Users/arenhomefolder/anaconda3/lib/python3.6/site-packages/spyder/utils/site/sitecustomize.py", line 705, in runfile
    execfile(filename, namespace)

  File "/Users/arenhomefolder/anaconda3/lib/python3.6/site-packages/spyder/utils/site/sitecustomize.py", line 102, in execfile
    exec(compile(f.read(), filename, 'exec'), namespace)

  File "/Users/arenhomefolder/Documents/DataAnalystnanodegree/2.x bikeshare-2/bikeshare_main_with_functions.py", line 499, in <module>
    user_stats(df) # info about bikeshare users

  File "/Users/arenhomefolder/Documents/DataAnalystnanodegree/2.x bikeshare-2/bikeshare_main_with_functions.py", line 423, in user_stats
    gender_count = df['Gender'].count()

  File "/Users/arenhomefolder/anaconda3/lib/python3.6/site-packages/pandas/core/frame.py", line 2685, in __getitem__
    return self._getitem_column(key)

  File "/Users/arenhomefolder/anaconda3/lib/python3.6/site-packages/pandas/core/frame.py", line 2692, in _getitem_column
    return self._get_item_cache(key)

  File "/Users/arenhomefolder/anaconda3/lib/python3.6/site-packages/pandas/core/generic.py", line 2486, in _get_item_cache
    values = self._data.get(item)

  File "/Users/arenhomefolder/anaconda3/lib/python3.6/site-packages/pandas/core/internals.py", line 4115, in get
    loc = self.items.get_loc(item)

  File "/Users/arenhomefolder/anaconda3/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 3065, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))

  File "pandas/_libs/index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc

  File "pandas/_libs/index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc

  File "pandas/_libs/hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item

  File "pandas/_libs/hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item

KeyError: 'Gender'