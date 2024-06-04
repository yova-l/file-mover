ALL_TEXT = {
    "SPA": {
        "app_desc": "Esta app es blablab"
    },
    "ENG": {
        "app_desc": "Esta app es blablab",
    }
}

def get_texts(language: str):
    if not language in ALL_TEXT:
        raise RuntimeError("Something unexpected happen")
    return ALL_TEXT[language]