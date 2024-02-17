import os
import sys
import zipfile
import requests
import toml

def find_venv_path(base_path):
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        scripts_path = os.path.join(item_path, 'Scripts')
        scripts_path_lower = os.path.join(item_path, 'scripts')
        if os.path.isdir(item_path) and (os.path.exists(scripts_path) or os.path.exists(scripts_path_lower)):
            return item_path
    return None

def download_file(url, dest_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(dest_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
    else:
        sys.exit("Error downloading file: " + url)

def extract_to_venv_lib(zip_path, venv_path):
    lib_path = os.path.join(venv_path, 'Scripts')
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(lib_path)

def main():
    # Read the IEDriverServer URL from pyproject.toml
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Adjust based on the script's location relative to pyproject.toml
    pyproject_path = os.path.join(project_dir, 'pyproject.toml')
    if not os.path.exists(pyproject_path):
        print("Error: pyproject.toml not found.")
        sys.exit(1)

    pyproject_data = toml.load(pyproject_path)
    iedriver_url = pyproject_data['tool']['hal-auto-check']['iedriver-url']
    driver_zip_filename = iedriver_url.split('/')[-1]

    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_script_dir)
    venv_path = find_venv_path(parent_dir)

    if not venv_path:
        print("No virtual environment found in the parent directory")
        print("Please make one python -m venv .")
        print(f"parent:{parent_dir}")
        sys.exit(1)

    driver_zip_path = os.path.join(current_script_dir, driver_zip_filename)

    print("Downloading IEDriverServer...")
    download_file(iedriver_url, driver_zip_path)

    print("Extracting IEDriverServer to the virtual environment...")
    extract_to_venv_lib(driver_zip_path, venv_path)
    #Remove the Zip Folder
    try:
        os.remove(driver_zip_path)
    except:
        pass
    print("IEDriverServer has been successfully installed in the virtual environment.")

if __name__ == "__main__":
    main()