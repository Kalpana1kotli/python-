#develop a pgm for backing up a given folder into a zip file by using relevant modules and suitable methods. 
 import os 
 import zipfile 
  
 def backup_folder_to_zip(source_folder,zip_filename): 
   if not os.path.exists(source_folder): 
     print(f"Error: source folder '{source_folder}' does not exist.") 
   zipf = zipfile.ZipFile(zip_filename, 'w') 
   for foldername, subfolders, filenames in os.walk(source_folder): 
     for filename in filenames in os.walk(source_folder): 
       file_path = os.path.join(foldername, filename) 
       zipf.write(file_path, os.path.relpath(file_path, source_folder)) 
       print(f"Zipping:{file_path}") 
   zipf.close() 
   print(f"backup sucessful: '{source_folder}' has been backed up to '{zip_file}'") 
 folder_to_backup = input("enter the name of the folder to backup (in the current working directory)") 
 zip_filename = f"{folder_to_backup}.zip" 
 backup_folder_to_zip(folder_to_backup, zip_filename)
