import os
import shutil




class FileOrganizer:
    def __init__(self, directory):
        self.directory = directory


    def organize_files(self):
        # Creates folders for each file type and Move files to correct folders
            for filename in os.listdir(self.directory):

                if os.path.isfile(os.path.join(self.directory, filename)):

                    file_extension = os.path.splitext(filename)[1]
                    destination_folder = self.get_destination_folder(file_extension)

                    if not os.path.exists(destination_folder):

                        os.makedirs(destination_folder)

                    shutil.move(os.path.join(self.directory, filename),
                            os.path.join(destination_folder, filename))
                


    def get_destination_folder(self,file_extension):

        if file_extension == "":
            return os.path.join(self.directory,"other")
        else:
            return os.path.join(self.directory, file_extension[1:].capitalize())
        

if __name__ == "__main__":
    directory = input("Enter the directory to organize: ")
    organizer = FileOrganizer(directory)
    organizer.organize_files()
    print("Files organized successfully.")
else:
    print("Invalid directory path.")


