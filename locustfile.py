from locust import HttpLocust, TaskSet, task
import logging
import re
import json
import pprint
from html.parser import HTMLParser

class SampleTaskSet(TaskSet):
    def on_start(self):
        logging.info('start task')
        
    def on_stop(self):
        logging.info('stop task')
    
    @task
    def exec(self):
        self.client.get('/')
        response = self.client.get('/posts/create')
        pprint(response)
        csrftoken = re.search('input name="_token" value="(.+?)"', response.text)
        data = { 'title':'テストタイトル', 'body':'テストボディ', '_token':csrftoken }
        self.client.post('/posts', data)

class SampleTask(HttpLocust):
    task_set = SampleTaskSet
    min_wait = 5000
    max_wait = 9000
