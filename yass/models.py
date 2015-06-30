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


import re
import time

from pyquery import PyQuery

from yass.helpers import without_duplicates


__all__ = ['PluginBase']


class PluginMeta(type):
    """
    Metaclass for all plugins
    """
    class Options(object):
        """
        Plugin options with default values
        """
        def __init__(self, meta=None):
            # Default attribute-value pairs
            self.search_url = None

            self.query_param = 'q'

            self.include_param = 'site%3A'
            self.exclude_param = '-site%3A'

            self.subdomains_selector = None

            self.request_delay = .250

            # Custom values
            if meta:
                for obj_name, obj in meta.__dict__.iteritems():
                    if hasattr(self, obj_name):
                        setattr(self, obj_name, obj)

    def __new__(mcs, name, bases, attrs):
        super_new = super(PluginMeta, mcs).__new__

        # Ensure initialization is only performed for subclasses of PluginBase
        # (excluding PluginBase class itself).
        parents = [b for b in bases if isinstance(b, PluginMeta)]
        if not parents:
            return super_new(mcs, name, bases, attrs)

        # Create the class.
        module = attrs.pop('__module__')
        new_class = super_new(mcs, name, bases, {'__module__': module})
        attr_meta = attrs.pop('Meta', None)
        if not attr_meta:
            meta = getattr(new_class, 'Meta', None)
        else:
            meta = attr_meta
        base_meta = getattr(new_class, '_meta', None)

        setattr(new_class, '_meta', PluginMeta.Options(meta))
        if base_meta and not base_meta.abstract:
            # Non-abstract child classes inherit some attributes from their
            # non-abstract parents.
            for attr in base_meta.__dict__.keys():
                if not hasattr(meta, attr):
                    setattr(new_class._meta, attr, getattr(base_meta, attr))

        # Add all attributes to the class.
        for obj_name, obj in attrs.items():
            setattr(new_class, obj_name, obj)

        return new_class


def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    # This requires a bit of explanation: the basic idea is to make a dummy
    # metaclass for one level of class instantiation that replaces itself with
    # the actual metaclass.
    class metaclass(meta):
        def __new__(cls, name, this_bases, d):
            return meta(name, bases, d)

    return type.__new__(metaclass, 'temporary_class', (), {})


class PluginBase(with_metaclass(PluginMeta)):
    """Plugin base class"""

    def __init__(self, domain, *args, **kwargs):
        self.domain = domain
        # set options custom/default value
        self.exclude_subdomains = kwargs.pop('exclude_subdomains', None)
        if kwargs:
            raise AttributeError(
                "Unknown attributes in plugin initialization ({keys})".format(
                    keys=', '.join(kwargs.keys())
                )
            )

    @staticmethod
    def extract(elements):
        """
        Extract data from given HTML elements

        :param elements: HTML elements obtained with PyQuery execution
        :type elements: list[Element]
        :return: extracted data
        :rtype: list[str]
        """
        return [element.text_content() for element in elements]

    def clean(self, urls):
        """
        Clean subdomains URLs from noise

        :param urls: an ensamble of URLs to clean
        :type urls: list[str]
        :return: cleaned subdomains URLs
        :rtype: list[str]
        """
        subdomains = []
        regexp = re.compile(r'(.+://)?(?P<subdomain>(.+)\.{domain})([/\?].*)?'.format(domain=self.domain))
        for url in urls:
            match = regexp.match(url)
            if match and match.group('subdomain'):
                subdomains.append(match.group('subdomain'))
        return subdomains

    def url(self, exclude_subdomains=None):
        """
        Build the search query URL sring

        :param exclude_subdomains: subdomains to exclude from the search
        :type exclude_subdomains: list[str]
        :param page: results page to ask for
        :type page: int
        :return: URL to use as search query
        :rtype: str
        """
        meta = self._meta

        url = "{url}?{query_param}={include}{domain}".format(
            url=meta.search_url,
            query_param=meta.query_param,
            include=meta.include_param,
            domain=self.domain
        )

        excluded_subdomains = without_duplicates((exclude_subdomains or []) + (self.exclude_subdomains or []))

        if excluded_subdomains:
            url += '+' + '+'.join([
                "{exclude}{subdomain}".format(exclude=meta.exclude_param, subdomain=excluded_domain)
                for excluded_domain in excluded_subdomains
            ])

        return url

    def run(self):
        """
        Start plugin execution

        :return: collected subdomains one by one
        :rtype: __generator
        """
        meta = self._meta
        collected_subdomains = []

        while True:
            url = self.url(exclude_subdomains=collected_subdomains)

            pq = PyQuery(url=url)
            elements = pq(meta.subdomains_selector)

            subdomains = self.clean(self.extract(elements)) or []
            # Remove already collected subdomains
            subdomains = list(set(subdomains) - set(collected_subdomains))
            # Check if there is at least one result
            if subdomains:
                collected_subdomains += subdomains

                for subdomain in subdomains:
                    yield subdomain

                time.sleep(meta.request_delay)  # To avoid error 503 (Service Unavailable), or CAPTCHA
            else:
                break
