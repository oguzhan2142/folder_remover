import os


def is_flutter_project(path):
    is_yaml_exist = os.path.exists(os.path.join(path, "pubspec.yaml"))
    is_lib_exist = os.path.exists(os.path.join(path, "lib"))
    is_main_dart_exist = os.path.exists(os.path.join(path, "lib", "main.dart"))
    
    return is_yaml_exist and is_lib_exist and is_main_dart_exist


def is_nodejs_project(path):
    is_package_json_exist = os.path.exists(os.path.join(path, "package.json"))
    is_at_least_one_js_file_exist = False
    
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".js"):
                is_at_least_one_js_file_exist = True
                break
    
    return is_package_json_exist and is_at_least_one_js_file_exist
