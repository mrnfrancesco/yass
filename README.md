# YASS
YASS - Yet Another Subdomainer Software

YASS is a plugin-based subdomainer.
Its goal is to give you a tool to query whatever search engine you like and parse HTML response writing *less than 10 lines of code*.

#### YASS Plugins
YASS comes with two pre-installed plugins: `Google` and `Bing`. You can look at them in `yass/plugins.py`.

##### How to write a new YASS plugin

YASS plugins follow just a few rules:

1. All the plugins are stored in `yass/plugins.py` module.

2. Every plugin MUST subclass `models.plugin.PluginBase` and define an inner class named `Meta` with the following attributes in it:

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

YASS depends on:

- Python <= 2.7.9

and have just a requirement:

- PyQuery >= 1.2.9

To install YASS and its requirements:

    git clone https://github.com/mrnfrancesco/yass.git
    cd yass
    sudo pip2 install -r requirements.txt