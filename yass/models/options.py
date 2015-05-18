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


class Options(object):
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