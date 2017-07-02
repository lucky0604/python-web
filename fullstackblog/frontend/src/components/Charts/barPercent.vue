<template>
  <div :class="className" :id="id" :style="{height: height, width: width}"></div>
</template>

<script>
// import echarts main module
const echarts = require('echarts/lib/echarts')
// import the bar charts
require('echarts/lib/chart/bar')
// import the tooltip
require('echarts/lib/component/tooltip')

export default {
  name: 'barPercent',
  props: {
    className: {
      type: String,
      default: 'bar-percent-chart'
    },
    id: {
      type: String,
      default: 'bar-percent-chart'
    },
    width: {
      type: String,
      default: '100px'
    },
    height: {
      type: String,
      default: '80px'
    },
    dataNum: {
      type: Number,
      default: 0
    }
  },
  data() {
    return {
      chart: null
    }
  },
  watch: {
    dataNum() {
      this.setOptions()
    }
  },
  mounted() {
    this.initBar()
  },
  methods: {
    initBar() {
      this.chart = echarts.init(document.getElementById(this.id))
      this.setOptions()
    },
    setOptions() {
      this.chart.setOption({
        tooltip: {
          show: true,
          formatter(params) {
            return 'Done ' + params.value + 'articles<br/>Target: 90 Articles.<br/>Progress: ' + Math.round((params.value / 90) * 100) + '%'
          }
        },
        grid: {
          left: 0,
          right: 0,
          bottom: 0,
          top: 0,
          containLabel: false
        },
        xAxis: [{
          type: 'category',
          data: ['Done articles']
        }],
        yAxis: [{
          type: 'value',
          data: [],
          show: false
        }],
        animationDelay: 1000,
        series: [{
          type: 'bar',
          name: 'First',
          itemStyle: {
            normal: {
              color: '#e5e5e5'
            }
          },
          silent: true,
          barGap: '-100%',    // make series be overlap
          data: [150]
        }, {
          type: 'bar',
          name: 'app',
          itemStyle: {
            normal: {
              color: '#30b08f'
            }
          },
          z: 10,
          data: [this.dataNum]
        }]
      })
    }
  }
}
</script>