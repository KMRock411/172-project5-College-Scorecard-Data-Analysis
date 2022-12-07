import os
class Folder:
    def __init__(self,folder_name):
        self.folder_name = folder_name
        self.list_of_files = []
        folder_to_target = 'C:/Users/Rock2/PycharmProjects/172-project5-College-Scorecard-Data-Analysis/Resources/CSV/' + folder_name
            #change file path to where you downloaded it from github, up to /Resources/CSV/
        for file in os.listdir(folder_to_target): #get list of filenames in specified folder
            if file.endswith(".csv"):
                self.list_of_files.append(file)

    def __repr__(self):
        return self.folder_name

    def __str__(self):
        return self.folder_name

    def display_files(self):
        """:return: list of files in the targeted folder"""
        return self.list_of_files

    def select_file(self,filename):
        """:return: the filename without '.csv' on the end"""
        return filename
