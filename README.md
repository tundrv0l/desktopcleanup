# desktopcleanup.py

My desktop can get very messy. This repository contains a simple script I use to cleanup particular files from my desktop. 

## Description

A script that utilizes the 'shutil' library in order to perform moving operations on particular files in my 'Desktop'/'Downloads' folder that I have designated (These file extentsions by deault are PDF, DOCX, DOC, TXT, XLSX). The script will check for every file with this extension in my Desktop/Downloads folders, and subsequently moves it to my 'Documents' folder. If the move operation fails (thrown by shutil), the error is logged to console (Generally, this is 'File Already Exists').

## How-To/Installation

I designed this program for use on my windows machines. I have yet to verify or test that it works in a Linux enviroment. That being said, here is how to use: 

```
$ git clone [https://](https://github.com/tundrv0l/desktopcleanup.git)
$ cd ../path/desktopcleanup
$ ./destkopcleanup
```
Once the script is installed, you can call it via command line, or you can throw it into Window's Task Scheduler. 
* Type 'Task Scheduler' into the Windows Search Bar.
* Click Actions>Create Task
* Name the Task
* From the task screen, click the 'Actions' Tab, Click 'New'. Ensure the 'Action' box is 'Start a Program'
* Find where your python executable is located and copy it. (Can be done by typing 'where python3' in the terminal).
* Copy the path to your python executable to the 'Program/script' box in the 'New Action' window.
* From where you cloned desktopcleanup: Copy the path to the repository.
* In the 'New Action' Window: Copy the path to the repository into 'Start in (Optional)', and in 'Add arguements (optional)' put 'desktopcleanup.py'. Click Ok
* Now that the task is set up, in the same window you can go to 'Triggers' > New to set up the event on which you would like the script to run; I have mine set up for every time the system starts up.


Please let me know what you think and enjoy!
