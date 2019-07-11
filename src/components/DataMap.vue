<template>
  <div>
    <div class="map">
      <div id="map_bombs" style="overflow:hidden"></div>
    </div>
  </div>
</template>

<script>
import * as Datamap from "datamaps";
import * as d3 from "d3";

export default {
  name: "DataMap",
  data: function() {
    return {
      width: 950,
      height: 550,
      scale: 1
    };
  },
  props: ["toUseBombs"],
  mounted() {
    this.drawMap();
  },
  watch: {
    toUseBombs: function() {
      // watch it
      this.drawMap();
    }
  },
  methods: {
    drawMap() {
      document.getElementById("map_bombs").innerHTML =
        "<div id='map_bombs'></div>";
      //const pm = this;
      const datamap = new Datamap({
        height: 450,
        width: 1000,
        element: document.getElementById("map_bombs"),
        scope: "world",
        geographyConfig: {
          popupOnHover: false,
          highlightOnHover: false
        },
        fills: {
          defaultFill: "#EDDC4E",
          Hotmix: "#1e53e6",
          Malaspina: "#e6751e",
          Blank: "#a3a5a8"
        },
        data: {}
      });
      //var vm = this;
      datamap.bubbles(this.toUseBombs);
      /*
      datamap.svg.selectAll(".datamaps-bubble").on("click", function(bubble) {
        
        var loc = bubble.latitude + "-" + bubble.longitude;
        vm.$emit('bubble-selected', [loc, bubble.stations, bubble.location_name])
        /*vm.$store.commit("setLoc", loc);

        vm.$store.commit("setCurrentDepthProfile", bubble.stations);
        vm.$store.commit("setStation", bubble.location_name);
      });*/
      this.datamap = datamap;

      d3.select("svg").call(
        d3.behavior.zoom().on("zoom", function() {
          d3.select("svg").attr(
            "transform",
            "translate(" +
              d3.event.translate +
              ")" +
              " scale(" +
              d3.event.scale +
              ")"
          );
        })
      );
    }
  }
};
</script>
