# etymology
find words with shared etymologies

## set up dev env
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## usage
### get word origins 
#### endpoint 
```
GET /origins/<language_code>/<word>
```

#### example request
```
GET /origins/eng/anthology
```

#### example response
```
{
    'results': [
        {
            'word': 'anthère',
            'language': 'French',
            'language_code': 'fra',
            'meaning': {}
        },
        {
            'word': 'ἀνθηρός',
            'language': 'Ancient Greek (to 1453)',
            'language_code': 'grc',
            'meaning': {}
        }
    ]
}

```

### get origin descendants 
#### endpoint 
```
GET /descendants/<language_code>/<word> 
```

#### example request
```
GET /descendants/fra/anthère
```

#### example response
```
{
    'results': [
        {
            'word': 'anther',
            'language': 'English',
            'language_code': 'eng',
            'meaning': {
                'Noun': ['the part of the stamen that...']
            }
        },
        {
            'word': 'antheroid',
            'language': 'English',
            'language_code': 'eng',
            'meaning': {}
        }
    ]
}
```
