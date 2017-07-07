<template>
  <div class="app-container calendar-list-container">
    <el-table :data="list" v-loading.body="listLoading" border fit highlight-current-row style="width: 100%">
      <el-table-column align="center" label="Number" width="65">
        <template scope="scope">
          <span>{{scope.row.id}}</span>
        </template>
      </el-table-column>

      <el-table-column width="180px" align="center" label="Time">
        <template scope="scope">
          <span>{{scope.row.timestamp | parseTime('{y}-{m}-{d} {h}:{i}')}}</span>
        </template>
      </el-table-column>

      <el-table-column min-width="300px" label="Title">
        <template scope="scope">
          <span>{{scope.row.title}}</span>
        </template>
      </el-table-column>

      <el-table-column width="110px" align="center" label="Author">
        <template scope="scope">
          <span>{{scope.row.user.username}}</span>
        </template>
      </el-table-column>

      <el-table-column width="80px" label="Importance">
        <template scope="scope">
          <span>**</span>
        </template>
      </el-table-column>

<!--
      <el-table-column align="center" label="Views" width="95">
        <template scope="scope">
          <span>{{scope.row.pageviews}}</span>
        </template>
      </el-table-column>
-->
      <el-table-column class-name="status-col" label="Status" width="90">
        <template scope="scope">
          <el-tag :type="scope.row.status | statusFilter">{{scope.row.status}}</el-tag>
        </template>
      </el-table-column>

      <el-table-column align="center" label="Draggable" width="95">
        <template scope="scope">
          <span>x</span>
        </template>
      </el-table-column>
    </el-table>

    <div class="show-d">Default ordering: {{olderList}}</div>
    <div class="show-d">After drag ordering: {{newList}}</div>
  </div>
</template>

<script>
import {getList} from 'api/article'
import Sortable from 'sortablejs'

export default {
  name: 'drag-table_demo',
  data() {
    return {
      list: null,
      total: null,
      listLoading: true,
      sortable: null,
      olderList: [],
      newList: []
    }
  },
  created() {
    this.fetchList()
  },
  filters: {
    statusFilter(status) {
      const statusMap = {
        Published: 'success',
        Draft: 'gray'
      }
      return statusMap[status]
    }
  },
  methods: {
    fetchList() {
      this.listLoading = true
      getList(this.listQuery).then(res => {
        this.list = res.data
        this.listLoading = false
        this.olderList = this.list.map(v => v.id)
        this.newList = this.olderList.slice()
        this.$nextTick(() => {
          this.setSort()
        })
      })
    },
    setSort() {
      const el = document.querySelectorAll('.el-table__body-wrapper > table > tbody')[0]
      this.sortable = Sortable.create(el, {
        onEnd: evt => {
          const tempIndex = this.newList.splice(evt.oldIndex, 1)[0]
          this.newList.splice(evt.newIndex, 0, tempIndex)
        }
      })
    }
  }
}
</script>


<style >
.drag-handler{
  width: 30px;
  height: 30px;
  cursor: pointer;
}
.show-d{
  margin-top: 15px;
}
</style>