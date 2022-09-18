# YASS - Yet Another Subdomainer Software

[![Build Status](https://travis-ci.org/mrnfrancesco/yass.svg?branch=master)](https://travis-ci.org/mrnfrancesco/yass)
[![Code Climate](https://codeclimate.com/github/mrnfrancesco/yass/badges/gpa.svg)](https://codeclimate.com/github/mrnfrancesco/yass)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-374/)
[![Release](https://img.shields.io/badge/release-v0.11.7-green.svg)](https://github.com/mrnfrancesco/yass/releases/tag/v0.11.7)

YASS is a plugin-powered search engine based subdomainer.
Its goal is to give you a tool to query whatever search engine you like and parse HTML response writing *less than 10 lines of code*.

## USAGE

    usage: yass [-g] [-d] [-l {debug,info,warning,error,critical}] [-c | -nc] [-h]
                [-u] [-v]
                DOMAIN [SUBDOMAIN [SUBDOMAIN ...]]
    
    positional arguments:
      DOMAIN                the domain to search for
      SUBDOMAIN             the list of subdomains to exclude
    
    Output arguments:
      -g, --grepable        output results in grepable format (default: False)
      -d, --debug           set output format to a more verbose one, for debugging
                            purpose (default: False)
      -l {debug,info,warning,error,critical}, --level {debug,info,warning,error,critical}
                            set output verbosity (default: info)
      -c, --color           use color in the output (default: True)
      -nc, --no-color       do not use color in the output
    
    Informations:
      -h, --help            show this help and exit
      -u, --usage           show the usage and exit
      -v, --version         show the framework version an exit


## Example output

```bash
$ yass microsoft.com

    ________________________________________________

    YASS - Yet Another Subdomainer Software (v0.11.7)
        by Francesco Marano (@mrnfrancesco)
    ________________________________________________


[INFO    ]	Collecting subdomains with Aol
[INFO    ]		(1/1) www.catalog.update.microsoft.com
[INFO    ]		(2/2) partner.microsoft.com
[INFO    ]		(3/3) docs.microsoft.com
[INFO    ]		(4/4) account.microsoft.com
[...]
[INFO    ]		(64/64) techcommunity.microsoft.com
[INFO    ]	Collecting subdomains with Ask
[INFO    ]		(1/65) imaginecup.microsoft.com
[INFO    ]		(2/66) office.microsoft.com
[INFO    ]		(3/67) customers.microsoft.com
[INFO    ]		(4/68) privacy.microsoft.com
[INFO    ]		(5/69) grv.microsoft.com
[INFO    ]		(6/70) channel9.microsoft.com
[INFO    ]		(7/71) datamigration.microsoft.com
[INFO    ]		(8/72) edusupport.microsoft.com
[INFO    ]		(9/73) forms.microsoft.com
[INFO    ]		(10/74) visualstudiogallery.msdn.microsoft.com
[INFO    ]	Collecting subdomains with Bing
[INFO    ]	Collecting subdomains with StartPage
[INFO    ]	Collecting subdomains with WebCrawler
[INFO    ]	Collecting subdomains with Yahoo
Collected 74 subdomains
academy.microsoft.com, account.microsoft.com, admin.manage.microsoft.com, admin.powerplatform.microsoft.com, answers.microsoft.com, apportal.microsoft.com, appsource.microsoft.com, azure.microsoft.com, bingads.microsoft.com, businessaccount.microsoft.com, businesscenter.mbs.microsoft.com, careers.microsoft.com, channel9.microsoft.com, client.dtmnebula.microsoft.com, cmat.tools.cp.microsoft.com, cmt3.research.microsoft.com, customers.microsoft.com, datamigration.microsoft.com, demos.microsoft.com, devblogs.microsoft.com, developer.microsoft.com, docs.microsoft.com, dotnet.microsoft.com, dynamics.microsoft.com, education.microsoft.com, edusupport.microsoft.com, einvoice.microsoft.com, events.microsoft.com, expertzone.microsoft.com, findtime.microsoft.com, flow.microsoft.com, forms.microsoft.com, formspro.microsoft.com, gallery.technet.microsoft.com, grv.microsoft.com, home.microsoft.com, imaginecup.microsoft.com, mail.exchange.microsoft.com, mbs.microsoft.com, mbspartner.microsoft.com, military.microsoft.com, mla.microsoft.com, mvp.microsoft.com, myinspire.microsoft.com, myprofile.microsoft.com, news.microsoft.com, nonprofit.microsoft.com, office.microsoft.com, partner.microsoft.com, partneruniversity.microsoft.com, paymentcentral.microsoft.com, plmt.microsoft.com, powerapps.microsoft.com, powerbi.microsoft.com, privacy.microsoft.com, referencesource.microsoft.com, register.ignite.microsoft.com, secure.bingads.microsoft.com, servicedesk.microsoft.com, serviceshub.microsoft.com, social.technet.microsoft.com, support.microsoft.com, teams.microsoft.com, techcommunity.microsoft.com, testconnectivity.microsoft.com, todo.microsoft.com, update.microsoft.com, visualstudio.microsoft.com, visualstudiogallery.msdn.microsoft.com, whiteboard.microsoft.com, windowsupdate.microsoft.com, www.catalog.update.microsoft.com, www.commerce.microsoft.com, www.microsoft.com
```

Yass can also be used in scripts with the `-g/--grepable` option:

```bash
$ yass -g microsoft.com
academy.microsoft.com|account.microsoft.com|admin.manage.microsoft.com|admin.powerplatform.microsoft.com|answers.microsoft.com|apportal.microsoft.com|appsource.microsoft.com|azure.microsoft.com|bingads.microsoft.com|businessaccount.microsoft.com|businesscenter.mbs.microsoft.com|careers.microsoft.com|channel9.microsoft.com|client.dtmnebula.microsoft.com|cmat.tools.cp.microsoft.com|cmt3.research.microsoft.com|customers.microsoft.com|datamigration.microsoft.com|demos.microsoft.com|devblogs.microsoft.com|developer.microsoft.com|docs.microsoft.com|dotnet.microsoft.com|dynamics.microsoft.com|education.microsoft.com|edusupport.microsoft.com|einvoice.microsoft.com|events.microsoft.com|expertzone.microsoft.com|findtime.microsoft.com|flow.microsoft.com|formspro.microsoft.com|gallery.technet.microsoft.com|grv.microsoft.com|home.microsoft.com|imaginecup.microsoft.com|mail.exchange.microsoft.com|mbs.microsoft.com|mbspartner.microsoft.com|military.microsoft.com|mla.microsoft.com|mvp.microsoft.com|myinspire.microsoft.com|myorder.microsoft.com|myprofile.microsoft.com|news.microsoft.com|nonprofit.microsoft.com|office.microsoft.com|partner.microsoft.com|partneruniversity.microsoft.com|paymentcentral.microsoft.com|plmt.microsoft.com|powerapps.microsoft.com|powerbi.microsoft.com|privacy.microsoft.com|referencesource.microsoft.com|register.ignite.microsoft.com|secure.bingads.microsoft.com|servicedesk.microsoft.com|serviceshub.microsoft.com|social.technet.microsoft.com|support.microsoft.com|teams.microsoft.com|techcommunity.microsoft.com|testconnectivity.microsoft.com|todo.microsoft.com|update.microsoft.com|visualstudio.microsoft.com|visualstudiogallery.msdn.microsoft.com|whiteboard.microsoft.com|windowsupdate.microsoft.com|www.catalog.update.microsoft.com|www.commerce.microsoft.com|www.microsoft.com
```

#### YASS Plugins
YASS comes with some pre-built plugins:

- Aol
- Ask
- Baidu
- Bing
- DuckDuckGo
- Google
- StartPage
- WebCrawler
- Yahoo
- Teoma
- Exaled

You can look at them in `yass/plugins.py`.

##### How to write a new YASS plugin

YASS plugins follow just a few rules:

1. All the plugins are stored in `yass/plugins.py` module.

2. Every plugin MUST subclass `yass.models.PluginBase` and define an inner class named `Meta` with the following attributes in it:

    - `search_url` [mandatory],  a string representing the base URL for the search engine
    - `query_param` [default: `'q'`], the parameter used to store the query
    - `include_param` [default: `'site%3A'`], the parameter to use in the search engine to search for a specific domain
    - `exclude_param` [default: `'-site%3A'`], the parameter to use in the search engine to exclude a specific domain from the results
    - `subdomains_selector` [mandatory], the jQuery selector (yes, jQuery) where to find the subdomains from the results page
    - `request_delay` [default: `.250`], the number of seconds to wait after every query before querying again

3. You can use the default plugin behaviour in most cases, but if you need to change it you could override these methods only:

    - `url(self, exclude_subdomain=None)`, it provide the query string based on `Meta` attributes
    - `extract(self, elements)`, it extract an URL string from an `Element` list of objects (look at `PyQuery` to know how it works)
    - `clean(self, urls)`, it remove useless parts from a list of URLs to get the subdomain string only

#### INSTALL

YASS is fully compatible with Python 3.7 and have just two requirements:

- PyQuery >= 1.2.9
- Colorama

To install YASS and its requirements:

```bash
$ git clone https://github.com/mrnfrancesco/yass.git  # or download and unzip release archive
$ cd yass
$ ./setup.py install
```

Or you can use Docker:

```bash
# Download YASS' Dockerfile
$ wget "https://raw.githubusercontent.com/mrnfrancesco/yass/master/Dockerfile"

# Build the latest version of YASS (use YASS_VERSION arg to build specific version)
$ docker build -t mrnfrancesco/yass:latest .

$ docker run --rm -ti mrnfrancesco/yass:latest /bin/sh

/yass # yass --version
YASS v0.11.7
```