<template>
  <div class="app-container">
    <div style="margin: 0 0 5px 20px">固定表头，按照表头顺序排列</div>
    <fixed-thread />
    
    <div style="margin: 30px 0 5px 20px">不固定表头，按照点击顺序排列</div>
    <unfixed-thread />
  </div>
</template>


<script>
import fixedThread from './dynamictable/fixedThread'
import unfixedThread from './dynamictable/unfixedThread'

export default {
  components: {fixedThread, unfixedThread}
}
</script>