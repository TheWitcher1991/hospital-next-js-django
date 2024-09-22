#!/usr/bin/env bash

# https://github.com/vishnubob/wait-for-it

TIMEOUT=15
QUIET=0
HOST=""
PORT=""
WAITFORIT_cmd=""
WAITFORIT_wait_localhost=0
WAITFORIT_wait_timeout=15

usage() {
    echo "Usage: $0 host:port [-t timeout] [-- command args]"
    echo " -q | --quiet       Don't output any status messages"
    echo " -t TIMEOUT         Timeout in seconds, zero for no timeout"
    echo " -- COMMAND ARGS    Execute command with args after the test finishes"
    exit 1
}

parse_args() {
    while [[ $# -gt 0 ]]; do
        case "$1" in
            *:* )
            HOST=$(echo "$1" | cut -d : -f 1)
            PORT=$(echo "$1" | cut -d : -f 2)
            shift 1
            ;;
            -q | --quiet)
            QUIET=1
            shift 1
            ;;
            -t)
            TIMEOUT="$2"
            if [[ $TIMEOUT == "" ]]; then break; fi
            shift 2
            ;;
            --)
            shift
            WAITFORIT_cmd="$*"
            break
            ;;
            *)
            usage
            ;;
        esac
    done

    if [[ "$HOST" == "" || "$PORT" == "" ]]; then
        echo "Error: you need to provide a host and port to test."
        usage
    fi
}

wait_for_it() {
    if [[ $QUIET -eq 0 ]]; then
        echo "Waiting for $HOST:$PORT..."
    fi

    for i in $(seq 1 $TIMEOUT); do
        nc -z "$HOST" "$PORT" > /dev/null 2>&1

        if [[ $? -eq 0 ]]; then
            if [[ $QUIET -eq 0 ]]; then
                echo "$HOST:$PORT is available after $i seconds."
            fi
            return 0
        fi

        sleep 1
    done

    if [[ $QUIET -eq 0 ]]; then
        echo "Timeout reached, $HOST:$PORT is still not available."
    fi

    return 1
}

run_command() {
    if [[ $WAITFORIT_cmd != "" ]]; then
        if [[ $QUIET -eq 0 ]]; then
            echo "Executing command: $WAITFORIT_cmd"
        fi
        exec $WAITFORIT_cmd
    fi
}

parse_args "$@"
wait_for_it
run_command