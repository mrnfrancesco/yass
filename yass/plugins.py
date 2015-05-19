# YASS, Yet Another Subdomainer Software
# Copyright 2015 Francesco Marano (@mrnfrancesco) and individual contributors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from models.plugin import PluginBase


class Aol(PluginBase):
    class Meta:
        search_url = 'search.aol.com/aol/search'
        subdomains_selector = 'span[property="f:durl"]'


class Ask(PluginBase):
    class Meta:
        search_url = 'http://www.ask.com/web'
        subdomains_selector = 'p.durl'


class Baidu(PluginBase):
    class Meta:
        search_url = 'https://www.baidu.com/s'
        query_param = 'wd'
        subdomains_selector = 'span.g'


class Bing(PluginBase):
    class Meta:
        search_url = 'http://www.bing.com/search'
        subdomains_selector = '#b_results li.b_algo cite'


class Google(PluginBase):
    class Meta:
        search_url = 'https://www.google.com/search'
        subdomains_selector = 'li.g cite'
        request_delay = 1


class StartPage(PluginBase):
    class Meta:
        search_url = 'https://startpage.com/do/search'
        subdomains_selector = 'span.url'


class WebCrawler(PluginBase):
    class Meta:
        search_url = 'http://www.webcrawler.com/search/web'
        subdomains_selector = 'div.resultDisplayUrl'

class Yahoo(PluginBase):
    class Meta:
        search_url = 'https://search.yahoo.com/search'
        query_param = 'p'
        subdomains_selector = 'div.compTitle div span'
