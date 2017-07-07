<template>
  <div class="components-container" style="height: 100vh">
    <div class="chart-container">
      <mixChart id="apple" height="100%" width="100%" />
    </div>
  </div>
</template>

<script>
import mixChart from 'components/Charts/mixChart'
export default {
  components: {mixChart}
}
</script>

<style scoped>
.chart-container{
  position: relative;
  width: 100%;
  height: 90%;
  padding-bottom: 40px;
}
</style>