#!/bin/bash

# This program tracks the time spent on a task, and stores it in a logfile

declare -i running=0
#"~/.local/share"
LOGFILE=".timer_logfile"

function track {
    # Start
    if [[ "$1" == "start" ]]; then
        if [[ $# -lt 2 ]]; then
            echo "Missing a label. Correct way to use the start-command is: track start <'label'>."; 
        elif [[ running -eq 1 ]]; then
            echo "A task is already running. Disregarding start-command with label '$2'."; 
        else 
            startTime=$(date +"%Y-%m-%d %T")
            label=$2
            running=1 
        fi 

    # Stop
    elif [[ "$1" == "stop" ]]; then
        if [[ running -eq 0 ]]; then
            echo "There are currently no active tasks. Disregarding stop-command."; 
        else 
            stopTime=$(date +"%Y-%m-%d %T")
            running=0 # Declare that there are no programs running
            # Save file
            ( 
                echo START $startTime
                echo LABEL $label
                echo END $stopTime
                echo ""
            ) >> $LOGFILE
        fi
    
    # Status
    elif [[ "$1" == "status" ]]; then
        if [[ running -eq 0 ]]; then
            echo "There are currently no active tasks."; 
        else 
            echo "We are currently tracking the task with label '$label'.";
        fi

    # Wrong command-name
    else 
        echo "There are no commands named '$1'. Disregarding command."
    fi
}


# TODO: Sette variabelen LOGFILE i test-miljøet 

#start "This is task 1"
#status
#start "This is task 2"
#status
#stop
#status 
#stop 
#start "This is task 3"
#status


# TODO: gjøre så scriptet støtter en log-kommando, som displayer tid brukt på hver oppgave i formatet HH:MM:SS