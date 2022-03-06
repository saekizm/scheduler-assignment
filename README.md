# CA216 CPU Scheduling

## Introduction
This is the repo for the C starter files.  Read the details below carefully.  Note: the details of the different algorithms required for both the solo and pairs versions of the project are [found in the project spec](https://loop.dcu.ie/mod/assign/view.php?id=1815150) Only implement the files for the project-type you are undertaking.


## What you need to do
You should follow the instructions below:
1. fork (do not clone) this repository.  Once you have forked it, make your own repository private and add both me (Graham Healy - @healygr) and Wandri Jooste (@joostew2) as "maintainer".
2. add all your source files to the `src` directory.
3. Add your files relating to the manual/help command to the `manual` directory.
4. Your `makefile` should build the binary and place it in the `bin` directory.


## Misc 
Completing this project will require writing the following C files (if implementing the pair project).

schedule_fcfs.c
schedule_sjf.c
schedule_rr.c
schedule_priority.c
schedule_priority_rr.c

The supporting files invoke the appropriate scheduling algorithm. 

For example, to build the FCFS scheduler, enter
```
make fcfs
```
which builds the fcfs executable file.

