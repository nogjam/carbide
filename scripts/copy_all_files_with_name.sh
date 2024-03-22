#!/usr/bin/env sh

DESCRIPTION="Copy all files with the given NAME from SOURCE dir to DEST dir as specified."

print_help() {
    echo "$DESCRIPTION"
    echo ""
    echo "${BASH_SOURCE[0]} NAME SOURCE DEST"
}

if [[ "$1" == "--help" ]]; then
    print_help
    exit 0
fi

# TODO: Fix this.
# I keep getting "bad substitution" error on this line.
find $2 -type f -name $1 | while read -r line; do echo ${$(dirname ${line})/"${2}"/"${3}"}; done # && cp $line ${line/./~\/linux-headers}

# find /usr/src/linux-headers-5.15.0-100/ -name sched.h | while read -r line; do mkdir -p ${$(dirname ${line})/./~\/linux-headers} && cp $line ${line/./~\/linux-headers}; done
