# YASS, Yet Another Subdomainer Software
# Copyright 2015-2019 Francesco Marano (@mrnfrancesco) and individual contributors.
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


from yass.models import PluginBase


class Aol(PluginBase):
    class Meta:
        search_url = 'https://search.aol.com/aol/search'
        subdomains_selector = 'span.fz-ms.fw-m.fc-12th.wr-bw.lh-17'


class Ask(PluginBase):
    class Meta:
        search_url = 'https://www.ask.com/web'
        subdomains_selector = 'div.PartialSearchResults-item-url'


class Baidu(PluginBase):
    class Meta:
        search_url = 'https://www.baidu.com/s'
        query_param = 'wd'
        subdomains_selector = 'div.result div.c-row span'
        request_delay = 1


class Bing(PluginBase):
    class Meta:
        search_url = 'https://www.bing.com/search'
        subdomains_selector = '#b_results li.b_algo cite'


class DuckDuckGo(PluginBase):
    class Meta:
        search_url = 'https://html.duckduckgo.com/html/'
        subdomains_selector = 'a.result__url'


# Blocked by CAPTCHA
# class Google(PluginBase):
#     class Meta:
#         search_url = 'https://www.google.com/search'
#         subdomains_selector = '#search div.g cite'
#         request_delay = 1


class StartPage(PluginBase):
    class Meta:
        search_url = 'https://startpage.com/do/search'
        subdomains_selector = 'span.search-item__url'


class WebCrawler(PluginBase):
    class Meta:
        search_url = 'https://www.webcrawler.com/serp'
        subdomains_selector = 'div.resultDisplayUrl'
        include_param = ''
        exclude_param = '-'


class Yahoo(PluginBase):
    class Meta:
        search_url = 'https://search.yahoo.com/search'
        query_param = 'p'
        subdomains_selector = 'ol.searchCenterMiddle li div > span'




class Exalead(PluginBase):
    class Meta:
        search_url = 'https://www.exalead.com/search/web/results'
        subdomains_selector = 'li.media a.ellipsis'
