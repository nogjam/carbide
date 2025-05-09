#!/bin/bash

parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" || exit 1 ; pwd -P )
. "${parent_path}/echo_ansi.sh"

echo_style_literally() {
    local all_args=""
    IFS=" " all_args="$*"
    echo_ansi "$@" "$all_args"
}

echo_style_literally default default
echo_style_literally red default
echo_style_literally green default
echo_style_literally yellow default
echo_style_literally blue default
echo_style_literally magenta default
echo_style_literally cyan default
echo_style_literally white black
echo_style_literally black white
echo_style_literally bold yellow default
echo_style_literally dim yellow default
echo_style_literally italic yellow default
echo_style_literally underline yellow default
echo_style_literally strikethrough yellow default
echo_style_literally bold italic underline yellow blue
