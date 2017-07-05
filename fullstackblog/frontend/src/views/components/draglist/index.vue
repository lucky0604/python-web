<template>
  <div class="components-container">
    <code>基于Vue.Draggable可拖动列表组件</code>
    <div class="editor-container">
      <Draglist :list1="list1" :list2="list2" list1Title="Hot" list2Title="Articles" />
    </div>
  </div>
</template>

<script>
import Draglist from 'components/Draglist'
import {getList} from 'api/article'
export default {
  components: {Draglist},
  data() {
    return {
      list1: [],
      list2: []
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.listLoading = true
      getList(this.listQuery).then(res => {
        this.list1 = res.data.splice(0, 2)
        this.list2 = res.data
      })
    }
  }
}
</script>