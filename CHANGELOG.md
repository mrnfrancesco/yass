# 0.7.3 (2019-07-11)

## Python3 support

Due to recent Python2 deprecation, yass has been edited to fully support Python3 (tested on version 3.7.4)

## Plugins update

- Fix plugin meta to match new website HTML structure
- Disabled Baidu plugin due to unresponsive website
- Disabled Google plugin due to some new anti-bot tricks. Need to find some evasion to make it works again.


# 0.6.4 (2015-06-09)

#### Implemented enhancements:

- Added logger
- Added some options:
    - `-g`, `--grepable`        output results in grepable format (default: False)
    - `-d`, `--debugging`       set output format to a more verbose one, for debugging purpose (default: False)
    - `-l {debug,info,warning,error,critical}`, `--level {debug,info,warning,error,critical}` set output verbosity (default: info)
    - `-c`, `--color`           use color in the output (default: True)
    - `-nc`, `--no-color`       do not use color in the output
- Changed domain options usage:
    - `-d`, `--domain`      changed to be first positional argument
    - `-e`, `--exclude`     changed to be second positional argument

# 0.4.3 (2015-05-29)

First beta release