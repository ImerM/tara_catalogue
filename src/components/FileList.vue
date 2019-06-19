<template>
  <div class="hello">
    <ul id="file-list">
      <li v-for="file in file_list">
        {{ file.parent_dir }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'FileList',
  props: ["file_list"]
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

</style>
