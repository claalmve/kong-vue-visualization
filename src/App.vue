<template>
  <div id="app">
    <h1>Latency DashBoard</h1>
    <h2 style=top:50px class="lineChartHeader">Avg. Latency Over The Past Hour (measured by minutes ago)</h2>
    <GChart
      type="LineChart"
      :data="lineData"
      :options="chartOptions"
    />
  </div>
</template>

<script>
import { GChart } from 'vue-google-charts'
import json from '../data/traffic.json'

export default {
  name: 'app',
  components: {
    GChart
  },
  data() {
    return {

      // Keeps track of the current json file of data (JSON was constructed with a Python script in a
      // Jupyter Notebook in the data folder)
      myJson: json,

      // Keeps track of the past hour of requests (latest request - 1 hour)
      latestHour: "",

      // Keeps track of the requests that were in the past hour of requests
      filteredItems: "hello",
      
      // Constructs the data in the proper format for the GChart package
      lineData: [['Time', 'Latency']],
      
      // Chart configurations for good UI
      chartOptions: {
        series: {
          0: {color: '#20B2AA'}
        },
        fontName: 'Avenir',
        height: 600,
        legend: 'none',
        hAxis: {
          title: 'Number of Minutes Elapsed Since Most Recent Request',
          titleTextStyle: {
            bold: true
          }
        },
        vAxis: {
          title: 'Avg. Latency Over 5 Min',
          titleTextStyle: {
            bold: true
          }
        }
      }
    }
  },

  created() {

    // Finding the past hour marker, and filtering through all the requests that were within this past hour
    this.latestHour = new Date(this.myJson[this.myJson.length - 1].request_time);
    this.latestHour.setHours(this.latestHour.getHours() - 1);
    this.filteredItems = this.myJson.filter(item =>
      new Date(item.request_time) > this.latestHour
    )

    // Keeps track of the latency for all requests within a 5 min interval within the latest hour (from above)
    var counts = {};

    for (var i=0; i<this.filteredItems.length; i++) {
      var diffTime = Math.abs(new Date(this.filteredItems[i].request_time).getTime() - this.latestHour)
      var diffMinutes = Math.round(Math.round(diffTime) / 60 / 1000 / 5) * 5;
      var latency = parseFloat(this.filteredItems[i].latency_in_seconds);
      if (counts[diffMinutes]) {
        counts[diffMinutes].push(latency);
      } else {
        counts[diffMinutes] = [latency]
      }
    }

    // Finds the average latency of every 5 min interval and appends them to the this.lineData variable,
    // which will be rendered above in the template to construct the proper line graph visualization.
    for (var key in counts) {
      var counter = 0;
      for (var j=0; j<counts[key].length; j++) {
        counter += counts[key][j];
      }
      var avg = counter / counts[key].length;
      this.lineData = [...this.lineData, [key, avg]];
    }

  }
}

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
