# etymology
find words with shared etymologies

## set up dev env
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## using the api locally
1. run the api from your virtual environment
```
python api.py
```

2. make requests to `localhost:4000`

## usage
### get word origins 
#### endpoint 
```
POST /origins
```

#### arguments
**word (required):** string

**language_code (required):** string, an iso 639-3 language code

#### example request
```
POST /origins
{
    "word": "coruscant",
    "language_code": "eng"
{
```

#### example response
```
{
    "results": [
        {
            "word": "coruscare",
            "language": "Latin",
            "language_code": "lat",
            "meaning": [
                {
                    "part_of_speech": "verb",
                    "text": [
                        "coruscāre",
                        "present active infinitive of coruscō"
                    ],
                    "related_words": [],
                    "examples": []
                }
            ]
        }
    ]
}
```

### get origin descendants 
#### endpoint 
```
POST /descendants
```

#### arguments
**word (required):** string

**language_code (required):** string, an iso 639-3 language code

#### example request
```
POST /descendants

{
    "word": "coruscare",
    "language_code": "lat"
}
```

#### example response
```
{
    "results": [
        {
            "word": "coruscant",
            "language": "English",
            "language_code": "eng",
            "meaning": [
                {
                    "part_of_speech": "adjective",
                    "text": [
                        "coruscant (comparative more coruscant, superlative most coruscant)",
                        "Emitting flashes of light; glittering."
                    ],
                    "related_words": [],
                    "examples": []
                }
            ]
        }
    ]
}
```
