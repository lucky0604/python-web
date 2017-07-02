<template>
  <div class="app-container">
    <div style="margin-bottom: 15px;">Your groups: {{groups}}</div>
    Change Permission:
    <el-radio-group v-model="group">
      <el-radio-button label="editor"></el-radio-button>
    </el-radio-group>
  </div>
</template>

<script>
  import {mapGetters} from 'vuex'
  export default {
    data() {
      return {
        group: ''
      }
    },
    computed: {
      ...mapGetters([
        'groups'
      ])
    },
    watch: {
      group(val) {
        this.$store.dispatch('ChangeRole', val).then(() => {
          this.$router.push({path: '/permission/index?' + +new Date()})
        })
      }
    },
    created() {
      alert('permission')
    }
  }
</script>
