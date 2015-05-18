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


import sys

from shortcuts import iter_plugins


def main():
    domain = sys.argv[1]
    subdomains = []
    try:
        subdomains = sys.argv[2:]
    except IndexError:
        pass

    for Plugin in iter_plugins():
        index = 1
        print "[INFO] Collecting subdomains with {plugin_name}".format(plugin_name=Plugin.__name__)

        try:
            for subdomain in Plugin(domain, exclude_subdomains=subdomains).run():

                if subdomain not in subdomains:
                    subdomains.append(subdomain)

                print "\t[{index}/{total}] Discovered subdomain: {subdomain}".format(
                    index=index,
                    total=len(subdomains),
                    subdomain=subdomain
                )
                index += 1

            print  # blank line

        except Exception as e:
            print "\t[ERR] Got an unexpected error during connection ({exc_type}: {message})\n" \
                  "\t\t[-] Aborting {plugin_name} execution".format(
                exc_type=e.__class__.__name__,
                message=e.message,
                plugin_name=Plugin.__name__
            )

    if subdomains:
        print "Collected {collected} subdomains: {subdomains}".format(
            collected=len(subdomains),
            subdomains=', '.join(subdomains)
        )
    else:
        print "No subdomain collected :("


if __name__ == '__main__':
    main()
