#!/usr/bin/env bash
#
# NAME
#   color_picker.sh
#
# SYNOPSIS
#   ./color_picker.sh RED GREEN BLUE
#
# DESCRIPTION
#   Helps you pick terminal colors according to ANSI escape sequences.
#
#   -g, --generate-command
#       Generate echo command with ANSI escape sequences for producing the color
#   -h, --help
#       Show this help message and exit

parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" || exit 1 ; pwd -P )
. "${parent_path}/common_utilities.sh"

print_help() {
    generate_usage -ndt "$0"
}

print_synopsis() {
    generate_usage "$0"
}

# Process parameters
if ! params=$(getopt \
        --options gh \
        --longoptions generate-command,help \
        --name "$0" \
        -- "$@"
); then
    error "Usage errors! Please address them and try again."
    exit 1
fi

eval set -- "$params"
unset params

COLORS=()
GENERATE_COMMAND=0

parse_parameters() {
    while true; do
        case $1 in
            -g | --generate-command)
                GENERATE_COMMAND=1
                shift
                ;;
            -h | --help)
                print_help
                exit
                ;;
            --)
                shift
                if [ -z "${1:-}" ]; then
                    print_help
                    exit
                fi
                COLORS=("${@}")
                if [ "${#COLORS[@]}" -lt 3 ]; then
                    error "Less than three color components specified"
                    exit 1
                elif [ "${#COLORS[@]}" -gt 3 ]; then
                    error "More than three color components specified"
                    exit 1
                fi
                break
                ;;
        esac
    done
}

do_main() {
    parse_parameters "$@"

    if [ $GENERATE_COMMAND -eq 1 ]; then
        command_for_user="echo -e \"--> \\e[38;2;${COLORS[0]};${COLORS[1]};${COLORS[2]}m\" \"${COLORS[*]}\" \"\\e[0m <--\""
        echo "$command_for_user"
    else
        echo -e "--> \e[38;2;${COLORS[0]};${COLORS[1]};${COLORS[2]}m" "${COLORS[@]}" "\e[0m <--"
    fi
}

do_main "$@"
