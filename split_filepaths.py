import os, pathlib, json

"""
open array
if array contains any "directory" nodes open those nodes
If no directory nodes encountered, then take all those files, put as content of parent folder. Do the metadata crap for the folder itself not for individual files.


Open array
Go through nodes
if has key with value "directroy" then open that directory
if no directory then add to "files" array.
Add metadata to file description, repeat for all files in array

Open array
Go through nodes
If node has no directories in it
add to array called terminal_nodes
if empty add a value to the node 'is_empty':true


"""
files_meta = []
terminal_nodes = []

def traverse_node(dir_meta):
    n_directories = 0
    n_files = 0
    for entry in dir_meta:
        if entry["type"] == "directory":
            n_directories = n_directories + 1
            traverse_node(entry["contents"])
        if entry["type"] == "file":
            n_files = n_files + 1
    if n_directories == 0 and len(dir_meta)!=0: #if no directories in this folder
        current_entry = {}
        current_entry['content'] = dir_meta
        current_entry['parent_dir'] = '/'.join(dir_meta[0]["name"].split("/")[:-1])
        current_entry['station_name'] = dir_meta[0]["name"].split("Release_1/")[1].split("/")[0]
        current_entry['station_id'] = dir_meta[0]["name"].split("Release_1/")[1].split("/")[0][7:]
        current_entry['layer'] = dir_meta[0]["name"].split("Release_1/")[1].split("/")[1]
        current_entry['filter_size'] = dir_meta[0]["name"].split("Release_1/")[1].split("/")[2]
        current_entry['tags'] = dir_meta[0]["name"].split("Release_1/")[1].split("/")[3:-1]
        if n_files == 0:

            current_entry['is_empty'] = "True"
        if 'Station' in current_entry['station_name']:
            terminal_nodes.append(current_entry)

        """
        if entry["type"] == "file" and "Release_1/" in entry["name"]:
            if len(entry["name"].split("Release_1/")[1].split("/")) > 3:                
                file = {
                    "type": "file",
                    "path": entry["name"],
                    "name": entry["name"].split("/").pop(),
                    "parent_dir": '/'.join(entry["name"].split("/")[:-1]),
                    "filatype": entry["name"].split(".").pop(),
                    
                }
                files_meta.append(file)
        """

def main():
    with open('tara_files.json', 'r') as f:
        files_dict = json.load(f)
    traverse_node(files_dict)
    
    with open('files_tara_terminal.json', 'w') as json_file:  
        json.dump(terminal_nodes, json_file)


if __name__ == '__main__':

    main()
