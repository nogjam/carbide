#!/bin/bash

# ANSI Escape Sequences:
# https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797

echo_ansi() {
	local modes=()
	local fore=""
	local back=""
	local ansi=""
	local message=""

	while true; do
		case "$1" in
			bold)			modes+=("1"); shift ;;
			dim)			modes+=("2"); shift ;;
			italic)			modes+=("3"); shift ;;
			underline)		modes+=("4"); shift ;;
			strikethrough)	modes+=("9"); shift ;;
			*)				break ;;
		esac
	done

	case "$1" in
		black)			fore="30"; shift ;;
		red)			fore="31"; shift ;;
		green)			fore="32"; shift ;;
		yellow)			fore="33"; shift ;;
		blue)			fore="34"; shift ;;
		magenta)		fore="35"; shift ;;
		cyan)			fore="36"; shift ;;
		white)			fore="37"; shift ;;
		default)		fore="39"; shift ;;
		*)				;;
	esac

	case "$1" in
		black)			back="40"; shift ;;
		red)			back="41"; shift ;;
		green)			back="42"; shift ;;
		yellow)			back="43"; shift ;;
		blue)			back="44"; shift ;;
		magenta)		back="45"; shift ;;
		cyan)			back="46"; shift ;;
		white)			back="47"; shift ;;
		default)		back="49"; shift ;;
		*)				;;
	esac

	message="$1"

	if [ "${#modes[@]}" -ne 0 ]; then
		for x in "${modes[@]}"; do
			ansi="${ansi};${x}"
		done
	fi
	if [ -n "$mode" ]; then
		ansi="${mode}"
	fi
	if [ -n "$fore" ]; then
		ansi="${ansi};${fore}"
	fi
	if [ -n "$back" ]; then
		ansi="${ansi};${back}"
	fi

	if [[ "${ansi:0:1}" == ";" ]]; then
		ansi="${ansi:1}"
	fi

	echo -e "\e[${ansi}m${message}\e[0m"
}
