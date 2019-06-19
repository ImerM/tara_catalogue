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
filter_sizes = []
meta_tags = []
marine_layers = []

def split_into_lists(dir_meta):
    
    for entry in dir_meta:
        if entry["filter_size"] not in filter_sizes:
            filter_sizes.append(entry["filter_size"])
        if entry["layer"] not in marine_layers:
            marine_layers.append(entry["layer"])
        for tag in entry["tags"]:
            if tag not in meta_tags:
                meta_tags.append(tag)
   

def main():
    with open('files_tara_terminal.json', 'r') as f:
        files_dict = json.load(f)
    split_into_lists(files_dict)
    
    with open('filter_sizes.json', 'w') as json_file:  
        json.dump(filter_sizes, json_file)
    with open('meta_tags.json', 'w') as json_file:  
        json.dump(meta_tags, json_file)
    with open('marine_layers.json', 'w') as json_file:  
        json.dump(marine_layers, json_file)


if __name__ == '__main__':

    main()
