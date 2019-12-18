# etymology
find words with shared etymologies

## set up dev env
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## inspect etymology data
```
# enter repl
python 
# look up direct etymology for dynamic (can recurse down provided direct etymologies)
import ety.data
ety.data.etyms['eng']['dynamic']

# look up word in dictionary
from PyDictionary import PyDictionary 
d = PyDictionary()
d.meaning('anther') 
```
