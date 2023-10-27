'''----------------- 
# Author: Parker Clark
# Date: 10/27/2023
# Description: A script that moves everything from the user's Desktop and Downloads folder to their Documents folder.
# Usage: Run the main script, can be used in a cron job or task scheduler to run at a specified time/event. 
-----------------'''

#--Imports--#
import os
import shutil


def main(): 

    #--Folder Paths--#
    desktop: str = os.path.expanduser(r'~\Desktop')
    documents: str = os.path.expanduser(r'~\Documents')
    downloads: str = os.path.expanduser(r'~\Downloads')

    directories: list[str] = [desktop, downloads] # Maintain a list of input directories to iterate through
    file_extensions: tuple[str] = ('.pdf', '.docx', '.doc', '.txt', '.xlsx') # Maintain a list of file extensions to move

    for directory in directories:
        for filename in os.listdir(directory): 
            if filename.endswith(file_extensions): 
                try:
                    shutil.move(os.path.join(directory, filename), documents)
                except shutil.Error as e: # Catch any errors that occur during the move
                    print(f'Error occured whilst attempting to move file: {e}')
                    continue


if __name__ == '__main__':
    main()
