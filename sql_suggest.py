# -*- coding: utf-8 -*-
import requests

class SQLSuggest:

    @staticmethod
    def request(endpoint, apikey, model_id, text):
        params = {'apikey': apikey,
                  'model_id': model_id,
                  'text': text,
                  }

        response = requests.post(endpoint, params)

        return response.json()