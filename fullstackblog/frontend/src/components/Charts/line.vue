<template>
  <div :class="className" :id="id" :style="{height: height, width: width}"></div>
</template>

<script>
// import echarts main module
const echarts = require('echarts/lib/echarts')
// import line chart
require('echarts/lib/chart/line')
// import tooltip and title components
require('echarts/lib/component/markLine')
require('echarts/lib/component/markPoint')
require('echarts/lib/component/tooltip')

export default {
  name: 'lineChart',
  props: {
    className: {
      type: String,
      default: 'line-chart'
    },
    id: {
      type: String,
      default: 'line-chart'
    },
    width: {
      type: String,
      default: '100%'
    },
    height: {
      type: String,
      default: '200px'
    },
    listData: {
      type: Array,
      require: true
    }
  },
  data() {
    return {
      chart: null
    }
  },
  watch: {
    listData(dataList) {
      this.setLine(dataList)
    }
  },
  mounted() {
    this.chart = echarts.init(document.getElementById(this.id))
    this.setLine(this.listData)
  },
  methods: {
    setLine(dataList) {
      const xAxisData = []
      const data = []
      for (let i = 0; i < dataList.length; i ++) {
        const item = dataList[i]
        xAxisData.push(item.week.substring(item.week.length - 2) + ' week')
        data.push(item.count)
      }
      const markLineData = []
      for (let i = 1; i < data.length; i ++) {
        markLineData.push([{
          xAxis: i - 1,
          yAxis: data[i - 1],
          value: data[i] - data[i - 1]
        }, {
          xAxis: i,
          yAxis: data[i]
        }])
      }
      this.chart.setOption({
        title: {
          text: 'Awesome Chart'
        },
        grid: {
          left: 0,
          right: 0,
          bottom: 20,
          containLabel: true
        },
        tooltip: {
          trigger: 'axis'
        },
        animationDelay: 1000,
        xAxis: {
          data:xAxisData,
          axisLine: {
            show: false
          },
          axisTick: {
            show: false
          }
        },
        yAxis: {
          splitLine: {
            show: false
          },
          show: false
        },
        series: [{
          name: 'Post articles',
          type: 'line',
          data,
          markPoint: {
            data: [
              {type: 'max', name: 'Max value'},
              {type: 'min', name: 'Min value'}
            ]
          },
          itemStyle: {
            normal: {
              color: '#30b08f'
            }
          },
          markLine: {
            silent: true,
            smooth: true,
            effect: {
              show: true
            },
            animationDuration(idx) {
              return idx * 100
            },
            animationDelay: 1000,
            animationEasing: 'quadraticInOut',
            distance: 1,
            label: {
              normal: {
                position: 'middle'
              }
            },
            symbol: ['none', 'none'],
            data:markLineData
          }
        }]
      })
    }
  }
}
</script>