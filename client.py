# -*- coding: utf-8 -*-
from .sql_suggest import SQLSuggest

ENDPOINTS = {
    'sql_suggest': 'https://api.a3rt.recruit-tech.co.jp/sql_suggest/v1/predict',
}

class SQLSuggestClient(object):

    def __init__(self, apikey):
        self.apikey = apikey
        self.endpoint = ENDPOINTS['sql_suggest']

    def sql_suggest(self, text, model_id='default'):
        endpoint = self.endpoint
        apikey = self.apikey
        return SQLSuggest.request(endpoint, apikey, model_id, text)