<template>
  <div class="hello">
    <v-select
      :items="filter_size"
      multiple
      chips
      label="Filter Size"
      v-model="selected_filter_size"
    >
      <v-list-tile slot="prepend-item" ripple @click="toggle_all_filter">
        <v-list-tile-title><div v-if="this.selected_filter_size.length == 0">Select All</div><div v-if="this.selected_filter_size.length > 0">Deselect All</div></v-list-tile-title>
      </v-list-tile>
      <v-divider slot="prepend-item" class="mt-2"/>
    </v-select>
    <v-select :items="layers" multiple chips label="Layer" v-model="selected_layer">
      <v-list-tile slot="prepend-item" ripple @click="toggle_all_layers">
        <v-list-tile-title><div v-if="this.selected_layer.length == 0">Select All</div><div v-if="this.selected_layer.length > 0">Deselect All</div></v-list-tile-title>
      </v-list-tile>
      <v-divider slot="prepend-item" class="mt-2"/>
    </v-select>
    <v-select :items="tags" multiple chips label="Tag" v-model="selected_tags">
      <v-list-tile slot="prepend-item" ripple @click="toggle_all_tags">
        <v-list-tile-title><div v-if="this.selected_tags.length == 0">Select All</div><div v-if="this.selected_tags.length > 0">Deselect All</div></v-list-tile-title>
      </v-list-tile>
      <v-divider slot="prepend-item" class="mt-2"/>
    </v-select>
    <v-btn depressed v-on:click="send_filter_parameters()">Filter</v-btn>
  </div>
</template>

<script>
export default {
  name: "FilterForm",
  props: ["filter_size", "layers", "tags"],
  mounted() {
    console.log("filtered mouted");
  },
  data() {
    return {
      selected_filter_size: [],
      selected_layer: [],
      selected_tags: []
    };
  },
  methods: {
    toggle_all_filter: function(){
      if (this.selected_filter_size.length > 0) {
        this.selected_filter_size = []
      }
      else{
        this.selected_filter_size = this.filter_size
      }
    },
    toggle_all_layers: function()
    {
      if (this.selected_layer.length > 0) {
        this.selected_layer = []
      }
      else{
        this.selected_layer = this.layers
      }
    },
    toggle_all_tags: function(){
      if (this.selected_tags.length > 0) {
        this.selected_tags = []
      }
      else{
        this.selected_tags = this.tags
      }
    },
    send_filter_parameters: function() {
      let send_filter_parameters = {
        filter_size: this.selected_filter_size,
        layer: this.selected_layer,
        tags: this.selected_tags
      };
      this.$emit("filter_sent", send_filter_parameters);
    }
  }
};
</script>
<!-- 
Loads the json file with the data json object.
Has two components, form and display

listens for form events, on event filters data into a 'available_files' array
available-files displayed in display domponent


-->


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.select-css {
  display: block;
  font-size: 16px;
  font-family: sans-serif;
  font-weight: 700;
  color: #444;
  line-height: 1.3;
  padding: 0.6em 1.4em 0.5em 0.8em;
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
  margin: 0;
  border: 1px solid #aaa;
  box-shadow: 0 1px 0 1px rgba(0, 0, 0, 0.04);
  border-radius: 0.5em;
  -moz-appearance: none;
  -webkit-appearance: none;
  appearance: none;
  background-color: #fff;
  background-image: url("data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%23007CB2%22%20d%3D%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%2F%3E%3C%2Fsvg%3E"),
    linear-gradient(to bottom, #ffffff 0%, #e5e5e5 100%);
  background-repeat: no-repeat, repeat;
  background-position: right 0.7em top 50%, 0 0;
  background-size: 0.65em auto, 100%;
}
.select-css::-ms-expand {
  display: none;
}
.select-css:hover {
  border-color: #888;
}
.select-css:focus {
  border-color: #aaa;
  box-shadow: 0 0 1px 3px rgba(59, 153, 252, 0.7);
  box-shadow: 0 0 0 3px -moz-mac-focusring;
  color: #222;
  outline: none;
}
.select-css option {
  font-weight: normal;
}

body {
  padding: 3rem;
}
</style>
