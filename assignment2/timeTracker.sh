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
            # Set start-time and label, and declare that the program is tracking a task
            echo "START $(date +"%Y-%m-%d %T")" >> $LOGFILE 
            echo $2 >> $LOGFILE

            running=1 
        fi 

    # Stop
    elif [[ "$1" == "stop" ]]; then
        if [[ running -eq 0 ]]; then
            echo "There are currently no active tasks. Disregarding stop-command."; 
        else 
            # Set stop-time, and declare that the program is no longer tracking a task
            echo "END $(date +"%Y-%m-%d %T")" >> $LOGFILE
            echo "" >> $LOGFILE

            running=0 
        fi
    
    # Status
    elif [[ "$1" == "status" ]]; then
        if [[ running -eq 0 ]]; then
            echo "There are currently no active tasks."; 
        else 
            echo "We are currently tracking the task with label '$label'.";
        fi

    # Log
    elif [[ "$1" == "log" ]]; then
        if [[ ! -f "$LOGFILE" ]]; then
            echo "No tasks have been tracked. Disregarding log-command."
        else 
            lines=$(cat $LOGFILE) 
            for line in $lines; do 
                if [[$line == *"START"* ]]; then 
                    # Gjør noe
                fi 
            done 
        fi


    # Wrong command-name
    else 
        echo "There are no commands named '$1'. Disregarding command."
    fi
}


# TODO: gjøre så scriptet støtter en log-kommando, som displayer tid brukt på hver oppgave i formatet HH:MM:SS