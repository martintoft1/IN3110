## Task 2.1: move.sh

### Functionality

Moves the files from one directory to another. If one of the directories don't exist, the program simply prints out an error-message and then terminates.

### Usage

To make the script executable the user need to run the following command

```bash
chmod a+x ./move.sh
```

To move files from directory1 to directory2 the user needs to run the following command

```bash
./move.sh directory1 directory2
```

## Task 2.2 and 2.3: timeTracker.sh

### Functionality 

Tracks one task at a time. When a task is started, it's timestamp for when it was started, as well as it's label is added to a logfile. After a task is stopped, it's timestamp for when it was stopped is added to the same logfile. Its possible to check the status of the tasks in order to see if there are any tasks running, and in that case which one. Its also possible to see how much time that've been spent on each of the tasks. 

### Usage

To make the script executable the user need to run the following command

```bash
chmod a+x ./timeTracker.sh
```

To be able to use the script's commands from the terminal the user needs to run the following command

```bash
source timeTracker.sh
```

To start tracking a task with a given label the user needs to run the following command

```bash
track start "label"
```

To stop tracking the current task the user needs to run the following command

```bash
track stop
```

To get the status of the current task the user needs to run the following command

```bash
track status
```

To print out the time spent on each task the user needs to run the following command

```bash
track log
```