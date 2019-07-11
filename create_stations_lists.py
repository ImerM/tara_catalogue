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
{
    "station": "Station1",
    "latitude": 44.415,
    "longitude": -9.833,
    "locality_longhurst_2007": "Westerlies Biome",
    "locality_ocean_regions": "(NAO) North Atlantic Ocean [MRGID:1912]",
    "locality_longhurst_2007_MRGID": "(NADR) North Atlantic Drift Province [MRGID:21453]",
    "locality_geographic": "(ESP) Spain"
  },

"""
locality_longhurst_2007 = []
locality_ocean_regions = []
locality_longhurst_2007_MRGID = []
locality_geographic = []

stations_locality_longhurst_2007 = []
stations_locality_ocean_regions = []
stations_locality_longhurst_2007_MRGID = []
stations_locality_geographic = []

def split_into_lists(dir_meta):
    
    for entry in dir_meta:
        if entry["locality_longhurst_2007"] not in locality_longhurst_2007:
            locality_longhurst_2007.append(entry["locality_longhurst_2007"])

        if entry["locality_ocean_regions"] not in locality_ocean_regions:
            locality_ocean_regions.append(entry["locality_ocean_regions"])

        if entry["locality_longhurst_2007_MRGID"] not in locality_longhurst_2007_MRGID:
            locality_longhurst_2007_MRGID.append(entry["locality_longhurst_2007_MRGID"])

        if entry["locality_geographic"] not in locality_geographic:
            locality_geographic.append(entry["locality_geographic"])
        
def assign_stations(dict_meta, localities_array, locality_name):
    locality_set = []

    for locality in localities_array:
        locality_stations = []
        locality_station_names = []
        for entry in dict_meta:
            if entry[locality_name] == locality:
                locality_stations.append(
                    {
                        'name' : entry["station"],
                        'latitude' : entry["latitude"],
                        'longitude' : entry["longitude"],
                        'radius': 10,
                        'fillKey': 'Malaspina'
                    })
                locality_station_names.append(entry["station"])
        locality_set.append(
            {
                'name' : locality,
                'stations' : locality_stations,
                'station_names': locality_station_names
            }
        )
    return locality_set


def main():
    with open('stations_meta.json', 'r') as f:
        stations_dict = json.load(f)
    split_into_lists(stations_dict)

    stations_locality_longhurst_2007 = assign_stations(stations_dict, locality_longhurst_2007, 'locality_longhurst_2007')
    stations_locality_ocean_regions = assign_stations(stations_dict, locality_ocean_regions, 'locality_ocean_regions')
    stations_locality_longhurst_2007_MRGID = assign_stations(stations_dict, locality_longhurst_2007_MRGID, 'locality_longhurst_2007_MRGID')
    stations_locality_geographic = assign_stations(stations_dict, locality_geographic, 'locality_geographic')

    with open('stations_locality_longhurst_2007.json', 'w') as json_file:  
        json.dump(stations_locality_longhurst_2007, json_file)
    with open('stations_locality_ocean_regions.json', 'w') as json_file:  
        json.dump(stations_locality_ocean_regions, json_file)
    with open('stations_locality_longhurst_2007_MRGID.json', 'w') as json_file:  
        json.dump(stations_locality_longhurst_2007_MRGID, json_file)
    with open('stations_locality_geographic.json', 'w') as json_file:  
        json.dump(stations_locality_geographic, json_file)



    with open('locality_longhurst_2007.json', 'w') as json_file:  
        json.dump(locality_longhurst_2007, json_file)
    with open('locality_ocean_regions.json', 'w') as json_file:  
        json.dump(locality_ocean_regions, json_file)
    with open('locality_longhurst_2007_MRGID.json', 'w') as json_file:  
        json.dump(locality_longhurst_2007_MRGID, json_file)
    with open('locality_geographic.json', 'w') as json_file:  
        json.dump(locality_geographic, json_file)


if __name__ == '__main__':

    main()
