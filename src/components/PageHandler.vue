<template>
  <div class="hello">
    <v-layout row>
      <v-flex xs12 sm8 offset-sm2 md8 offset-md2>
        <FilterForm
          :localities="localities_list"
          :filter_size="array_filter_sizes"
          :layers="array_marine_layers"
          :tags_first="array_meta_tags_first"
          :tags_second="array_meta_tags_second"
          v-on:filter_sent="filter_files"
    />
        <v-switch
          v-model="show_map"
          :label="`Show map: ${show_map.toString()}`"
        ></v-switch>

        <v-content>
          <v-layout row>
            <v-flex xs12>
              <DataMap :toUseBombs=displayable_stations v-show="show_map" />
            </v-flex>
          </v-layout>
        </v-content>
        <FileList v-bind:file_list="displayable_list" />
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import FilterForm from "./FilterForm.vue";
import FileList from "./FileList.vue";
import DataMap from "./DataMap.vue";

import json from "../assets/files_tara_terminal.json";

import json_filter_sizes from "../assets/filter_sizes.json";
import json_marine_layers from "../assets/marine_layers.json";
import json_meta_tags_first from "../assets/meta_tags_first.json";
import json_meta_tags_second from "../assets/meta_tags_second.json";

import json_localities_geographic from "../assets/locality_geographic.json";
import json_localities_longhurst_2007_MRGID from "../assets/locality_longhurst_2007_MRGID.json";
import json_localities_longhurst_2007 from "../assets/locality_longhurst_2007.json";
import json_localities_ocean_regions from "../assets/locality_ocean_regions.json";

import json_stations_localities_geographic from "../assets/stations_locality_geographic.json";
import json_stations_localities_longhurst_2007_MRGID from "../assets/stations_locality_longhurst_2007_MRGID.json";
import json_stations_localities_longhurst_2007 from "../assets/stations_locality_longhurst_2007.json";
import json_stations_localities_ocean_regions from "../assets/stations_locality_ocean_regions.json";

export default {
  name: "PageHandler",
  components: {
    FilterForm,
    FileList,
    DataMap
  },
  data() {
    return {
      files: json,
      show_map: false,
      displayable_list: [],
      displayable_stations: [],
      array_filter_sizes: json_filter_sizes,
      array_marine_layers: json_marine_layers,
      array_meta_tags_first: json_meta_tags_first,
      array_meta_tags_second: json_meta_tags_second,

      localities_list: [
        
        {
          name: "Geographic",
          key: 'geographic',
          content: json_localities_geographic
        },
        
        {
          name: "Longhurst 2007",
          key: 'longhurst_2007',
          content: json_localities_longhurst_2007
        },
        
        {
          name: "Longhurst 2007 MRGID",
          key: 'longhurst_2007_MRGID',
          content: json_localities_longhurst_2007_MRGID
        },
        
        {
          name: "Ocean Regions",
          key: 'ocean_regions',
          content: json_localities_ocean_regions
        }
      ],
      locality_stations:{
        geographic: json_stations_localities_geographic,
        longhurst_2007: json_stations_localities_longhurst_2007,
        longhurst_2007_MRGID: json_stations_localities_longhurst_2007_MRGID,
        ocean_regions: json_stations_localities_ocean_regions
      }
    };
  },
  methods: {
    filter_files: function(filtering_parameters) {
      console.log('hello')
      var filtered_files = this.files;
      if (filtering_parameters.filter_size.length > 0) {
        filtered_files = filtered_files.filter(file => filtering_parameters.filter_size.includes(file.filter_size))
      }
      if (filtering_parameters.layer.length > 0) {
        filtered_files = filtered_files.filter(file => filtering_parameters.layer.includes(file.layer))
      }
      if (filtering_parameters.tags_first.length > 0)
      {
        filtered_files = filtered_files.filter(file => {
          var tgs = file.tags
          if (tgs.filter(tag => filtering_parameters.tags_first.includes(tag)).length > 0)
          {
            return true
          }
          }) 
      }

      if (filtering_parameters.tags_second.length > 0)
      {
        filtered_files = filtered_files.filter(file => {
          var tgs = file.tags
          if (tgs.filter(tag => filtering_parameters.tags_second.includes(tag)).length > 0)
          {
            return true
          }
          }) 
      }
      
      if (filtering_parameters.locality.length > 0){
        let possible_stations = this.locality_stations[filtering_parameters.locality_type_selected].filter(region => filtering_parameters.locality.includes(region.name))
        let possible_stations_array = possible_stations[0].stations
        
        filtered_files = filtered_files.filter(file => possible_stations[0].station_names.includes(file.station_name))
        let stations_kept = filtered_files.map(a => a.station_name)
        let usable_stations = possible_stations_array.filter(station => stations_kept.includes(station.name))
        this.displayable_stations = usable_stations
      }
      this.displayable_list = filtered_files;
    }
  }
};
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
