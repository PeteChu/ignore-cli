# -*- coding: utf-8 -*-

import os
import sys
import requests


class Ignore():

    __url = 'https://api.github.com/repos/dvcs/gitignore/contents/templates'
    __gitignore = '.gitignore'

    def __init__(self):
        self.load_templates()

    def gitignore_existed(self):
        current_directory = os.getcwd()
        return self.__gitignore in os.listdir(current_directory)

    def create_gitignore(self):
        f = open(self.__gitignore, 'w')
        f.close()

    def update_gitignore(self, template_name):
        if template_name not in self.templates:
            return

        url = self.templates[template_name]
        data = self.get_templates_content(url)
        template_content = data.content

        f = open(self.__gitignore, 'a+')
        f.write('##### Gitignore for {} #####'.format(template_name))
        for i in template_content:
            f.writelines(i)
        f.write('\n')
        f.close()

    def load_templates(self):
        r = requests.get(url=self.__url)
        resp = r.json()
        self.templates = {template['name'].split('.')[0].lower(): template['download_url']
                          for template in resp}

    def get_templates_content(self, url):
        r = requests.get(url=url)
        return r
