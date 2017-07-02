<template>
  <div class="dashboard-container">
    <component v-bind:is="currentRole"></component>
  </div>  
</template>

<script>
  import {mapGetters} from 'vuex'
  import EditorDashboard from './editor/index'
  import DefaultDashboard from './default/index'
  export default {
    name: 'dashboard',
    components: {
      EditorDashboard,
      DefaultDashboard
    },
    data() {
      return {
        currentRole: 'EditorDashboard'
      }
    },
    computed: {
      ...mapGetters([
        'name',
        'groups'
      ])
    },
    created() {
      if (this.groups.indexOf(1) >= 0) {
        return
      }
      this.currentRole = 'DefaultDashboard'
    }
  }
</script>
