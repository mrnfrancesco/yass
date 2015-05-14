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


from yass.helpers import without_duplicates
from yass.shortcuts import iter_plugins


def main():
    domain = 'microsoft.com'
    subdomains = []

    for Plugin in iter_plugins():
        subdomains = without_duplicates(subdomains + Plugin(domain, exclude_subdomains=subdomains).run())

    print  # blank line

    if subdomains:
        print "Collected {collected} subdomains: {subdomains}".format(
            collected=len(subdomains),
            subdomains=', '.join(subdomains)
        )
    else:
        print "No subdomain collected :("


if __name__ == '__main__':
    main()