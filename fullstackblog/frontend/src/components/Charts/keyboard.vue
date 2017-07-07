<template>
  <div :class="className" :id="id" :style="{height: height, width: width}"></div>
</template>

<script>
// import echarts core module
const echarts = require('echarts/lib/echarts')
// import the bar line
require('echarts/lib/chart/bar')
require('echarts/lib/chart/line')
// import the tooltip and title components
require('echarts/lib/component/tooltip')
require('echarts/lib/component/title')

require('echarts/lib/component/visualMap')

export default {
  name: 'barPercent',
  props: {
    className: {
      type: String,
      default: 'chart'
    },
    id: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '200px'
    },
    height: {
      type: String,
      default: '200px'
    }
  },
  data() {
    return {}
  },
  mounted() {
    this.initBar()
  },
  methods: {
    initBar() {
      this.chart = echarts.init(document.getElementById(this.id))

      const xAxisData = []
      const data = []
      for (let i = 0; i < 20; i ++) {
        xAxisData.push(i + '号')
        data.push(Math.round(Math.random() * 2 + 3))
      }

      this.chart.setOption(
        {
          backgroundColor: '#08263a',
          tooltip: {
            trigger: 'axis'
          },
          xAxis: {
            show: false,
            data:xAxisData
          },
          visualMap: {
            show: false,
            min: 0,
            max: 50,
            dimension: 0,
            inRange: {
              color: ['#4a657a', '#308e92', '#b1cfa5', '#f5d69f', '#f5898b', '#ef5055']
            }
          },
          yAxis: {
            axisLine: {
              show: false
            },
            axisLabel: {
              textStyle: {
                color: '#4a657a'
              }
            },
            splitLine: {
              show: true,
              lineStyle: {
                color: '#08263f'
              }
            },
            axisTick: {}
          },
          series: [{
            type: 'bar',
            data,
            name: 'posts',
            itemStyle: {
              normal: {
                barBorderRadius: 5,
                shadowBlur: 10,
                shadowColor: '#111'
              }
            },
            animationEasing: 'elasticOut',
            animationEasingOut: 'elasticOut',
            animationDelay(idx) {
              return idx * 20
            },
            animationDelayUpdate(idx) {
              return idx * 20
            }
          }]
        }
      )
    }
  }
}
</script>
