#!/usr/bin/env python

import optparse, urllib2, re, logging, sys, os, subprocess

NODE_WEBSITE = 'http://nodejs.org/'

def get_latest_node_version():
    res = urllib2.urlopen(NODE_WEBSITE).read()
    match = re.search(r'Current Version: ([v\d\.]+)', res)
    if (match):
        return match.group(1)
    
    return None

def install(version):
    # check if nvm present or not
    nvmPath = '%s/.nvm/nvm.sh' % os.path.expanduser('~')

    if not os.path.exists(nvmPath):
        print 'ERROR: file does not exist %s.\nDo you have nvm installed? If not - here\'s the command:\ncurl https://raw.github.com/creationix/nvm/master/install.sh | sh' % nvmPath
        return

    installedVersion = subprocess.Popen("source %s && nvm_version" % nvmPath, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()
    print 'You are running node %s' % installedVersion

    if version == None:
        print 'Fetching latest version from %s... ' % NODE_WEBSITE,
        version = get_latest_node_version()
        print version
        if version == None:
            print 'ERROR: Could not fetch node version'
            return
    else:
        version = 'v' + version

    if (installedVersion == version):
        print 'You are running the latest version'
        return

    print 'Upgrading node to %s. Do you want to continue? (y/n):' % version,
    if (raw_input() != 'y'):
        print 'Ok then'
        return
    
    command = "source %(nvmPath)s && nvm install %(version)s && nvm copy-packages %(installedVersion)s && nvm alias default %(version)s && source %(nvmPath)s" % locals()
    print "Executing: %s" % command
    proc = subprocess.Popen(command, shell=True, stdout=sys.stdout).communicate()
    print 'All done. Please reopen a shell to use %s' % version

def main():
    # auto-flush the buffer to stdout
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    # CLI options parser
    parser = optparse.OptionParser(description="Update your node.js installation and packages, using nvm")
    parser.add_option('--version', '-v', help="Version of node to install")
    options, arguments = parser.parse_args()
    install(options.version)

if __name__ == '__main__':
    main()
