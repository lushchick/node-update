node-update
===========

Simple python script for updating node.js installation using [Node Version Manager](https://github.com/creationix/nvm). By default installs latest version available on [nodejs.org](http://nodejs.org/) website.

Usage:

```bash
    $ python node-update.py -v 0.10.21

    You are running node v0.10.20
    Fetching latest version from http://nodejs.org/...  v0.10.21
    Upgrading node to v0.10.21. Do you want to continue? (y/n): y
    Executing: source /Users/anlu/.nvm/nvm.sh && nvm install v0.10.21 && nvm copy-packages v0.10.20 && nvm alias default v0.10.21 && source /Users/anlu/.nvm/nvm.sh
    ...
    default -> v0.10.21
    All done. Please reopen a shell to use v0.10.21
```
Use --help to see more