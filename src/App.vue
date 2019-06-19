<template>
  <v-app>
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Tara</span>
        <span class="font-weight-light">Oceans Catalogue</span>
      </v-toolbar-title>

    </v-toolbar>

    <v-content>
      <PageHandler/>
    </v-content>
  </v-app>
</template>

<script>

import PageHandler from './components/PageHandler.vue'

export default {
  name: 'App',
  components: {
    PageHandler
  },
  data () {
    return {
      //
    }
  }
}
</script>
