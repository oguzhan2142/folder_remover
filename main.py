import os

import delete_folder
import detect_project
import print_utils
from size import find_size_in_mb

folder = "/Users/oguzhan/Developer/Junk"


projects = [{
    "name":"flutter",
    "folders":["build"]
}]



def get_target_folders(project_name):
    for project in projects:
        if project["name"] == project_name:
            return project["folders"]
    return []


def to_mb_str(size):
    return f"{size:.2f} mb"


targets = []
print("Scanning folders...")
paths_in_dir =  os.listdir(folder)



for path in paths_in_dir:
    full_path = os.path.join(folder, path)
    folder_name = os.path.basename(full_path)
    if not os.path.isdir(full_path):
        
        continue
        
    project_name = ""
    if detect_project.is_flutter_project(full_path):
        project_name = "flutter"
    elif detect_project.is_nodejs_project(full_path):
        project_name = "nodejs"
    
    if project_name == "":
        continue
    project_total_size = find_size_in_mb(full_path)
    target = {
        "name": folder_name,
        "project": project_name,
        "size": project_total_size,
        "folders": [],
    }
    
    
    target_folders = get_target_folders(project_name)
    

    
    for target_folder in target_folders:
        target_path = os.path.join(full_path, target_folder)

        if not os.path.exists(target_path):
            continue
        target_folder_size = find_size_in_mb(target_path)



        target["folders"].append({
            "folder": target_folder,
            "path": target_path,
            "size": target_folder_size,
        })
        
    targets.append(target)
    print_utils.print_progress_bar(len(targets), len(paths_in_dir))



for target in targets:
    print("-------------------")
    print("")
    folder_name = target["name"]
    project_name = target["project"]
    project_total_size = target["size"]
    print(folder_name + ":")
    print(f"{project_name} - {to_mb_str(project_total_size)}")
    for folder in target["folders"]:
        path = folder["path"]
        name = folder["folder"]
        folder_size = folder["size"]
        print(f"-> {name} - {to_mb_str(folder_size)}")
    print("")


total_deleted_folders = 0
total_deleted_size = 0
for target in targets:
    for folder in target["folders"]:
        path = folder["path"]
        size = folder["size"]
        total_deleted_size += size
        total_deleted_folders += 1
        delete_folder.delete(path)
        print(f"Deleted: {path}")
        



print("-------------------")
print(f"total deleted folders: {total_deleted_folders}")
print(f"Total deleted size: {to_mb_str(total_deleted_size)}")


    




    
    
    
    
        

    
    
    

    
    
    
    

    

    




