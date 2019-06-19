<template>
  <div class="hello">
    <v-layout row>
      <v-flex xs12 sm6 offset-sm3>
    
    <FilterForm v-bind:filter_size=array_filter_sizes v-bind:layers=array_marine_layers v-bind:tags=array_meta_tags v-on:filter_sent="filter_files" />
    <FileList v-bind:file_list=displayable_list />
      </v-flex>
    </v-layout>
    
  </div>
</template>

<script>
import FilterForm from './FilterForm.vue'
import FileList from './FileList.vue'

import json from '../assets/files_tara_terminal.json'

import json_filter_sizes from '../assets/filter_sizes.json'
import json_marine_layers from '../assets/marine_layers.json'
import json_meta_tags from '../assets/meta_tags.json'


export default {
  name: 'PageHandler',
  components:{
      FilterForm,
      FileList
  },
    data(){
        return{
            files: json,
            displayable_list: [],
            array_filter_sizes: json_filter_sizes,
            array_marine_layers: json_marine_layers,
            array_meta_tags: json_meta_tags
        }
    },
  computed: {
    /*
    computed_filter_sizes: function() {
        var sizes = []
        for (const something in this.files) {
          if (this.files.hasOwnProperty(something)) {
            const element = this.files[something];
            if (!sizes.includes(element.filter_size)) {
              sizes.push(element.filter_size)
            } 
          }
        }
        return sizes
    },
    computed_layers: function(){
      var layers = []
        for (const something in this.files) {
          if (this.files.hasOwnProperty(something)) {
            const element = this.files[something];
            if (!layers.includes(element.layer)) {
              layers.push(element.layer)
            } 
          }
        }
        return layers
    },
    computed_tags: function()
    {
      var tags = []
      for (const something in this.files) {
          if (this.files.hasOwnProperty(something)) {
            const element = this.files[something];

            let element_tags = element.tags
            element.tags.forEach(tag => {
              if(!tags.includes(tag)) {
                tags.push(tag)
              }
            });
          }
        }
      return tags
    }*/
  },
  methods: {
    filter_files: function(filtering_parameters)
    {
      console.log(filtering_parameters)
      var filtered_files = []
        for (const something in this.files) {
          if (this.files.hasOwnProperty(something)) {
            const element = this.files[something];
            if (filtering_parameters.filter_size.includes(element.filter_size) && 
                filtering_parameters.layer.includes(element.layer)) 
            {
              let found_tags = 0

              element.tags.forEach(tag => {
                if (filtering_parameters.tags.includes(tag)) {
                  found_tags = found_tags + 1
                }
              });
              if (found_tags > 0)
              {
                filtered_files.push(element)
              }
              
            } 
          }
        }
      this.displayable_list = filtered_files
    }
  },


}
</script>
<!-- 
Loads the json file with the data json object.
Has two components, form and display

listens for form events, on event filters data into a 'available_files' array
available-files displayed in display domponent


-->


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
