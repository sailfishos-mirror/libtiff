#!/bin/sh

retval=0

set -x

autoreconf --install --force || retval=$?

# The config/config.guess and config/config.sub files used to be
# updated by this script, but the repository used no longer contains
# the latest files, and the 'cgit' interface to retrieve individual
# files from a git repository no longer works.
#
# The latest 'gitlog-to-changelog', 'config.guess', and 'config.sub'
# files are in the git repository at
# 'https://git.savannah.gnu.org/git/gnulib.git' and may be found in
# its 'build-aux' subdirectory.
#
# Check-out gnulib adjacent to this source tree so this script can
# update the build-aux files.
#   e.g. git clone https://git.savannah.gnu.org/git/gnulib.git
# Then make sure that the gnulib clone is updated prior to running this script.

build_aux=../gnulib/build-aux
if [ -d ${build_aux} ] ; then
    printf "%s\n" "Updating build-aux files..."
    for f in config.guess config.sub
    do
        cp -p ${build_aux}/${f} config/
    done
else
    printf "%s\n" "Use 'git clone https://git.savannah.gnu.org/git/gnulib.git' above this directory to get latest build-aux files."
fi

exit $retval
