import json
from itertools import permutations
from typing import Dict

import enchant
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

enchanted_dict = enchant.Dict('en_US')


@app.post('/words')
def get_words(word: str, length: int, positions: Dict):
    word_list = list(word)
    permuted_words = set([''.join(w) for w in permutations(word_list, length)])
    possible_words = []
    for permuted_word in permuted_words:
        if enchanted_dict.check(permuted_word):
            for letter, position in positions.items():
                if permuted_word[position] != letter: continue
            possible_words.append(permuted_word)
    return json.dumps(possible_words)


@app.get('/')
async def root():
    return {"message": "Welcome to wordscapes!"}
