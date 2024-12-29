import pandas as pd
myList = pd.Series([6,7,8,9,10])
print(myList)


#if we don't want to show the index then we can use just a list 

import pandas as pd
myList = list(pd.Series([6,7,8,9,10]))
print(myList)