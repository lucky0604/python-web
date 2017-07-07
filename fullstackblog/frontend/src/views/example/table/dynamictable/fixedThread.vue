<template>
  <div class="app-container">
    <div class="filter-container">
      <el-checkbox-group v-model="checkboxVal">
        <el-checkbox label="apple">apple</el-checkbox>
        <el-checkbox label="banana">banana</el-checkbox>
        <el-checkbox label="orange">orange</el-checkbox>
      </el-checkbox-group>
    </div>

    <el-table :data="tableData" :key="key" style="width: 100%">
      <el-table-column prop="name" label="fruitName" width="180"></el-table-column>
      <el-table-column :key="fruit" v-for="(fruit, index) in formThread" :label="fruit">
        <template scope="scope">
          {{scope.row[fruit]}}
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
const defaultFormThread = ['apple', 'banana']   // default checked box
export default {
  data() {
    return {
      tableData: [
        {
          name: 'fruit-1',
          apple: 'apple-10',
          banana: 'banana-10',
          orange: 'orange-10'
        }, {
          name: 'fruit-2',
          apple: 'apple-20',
          banana: 'banana-20',
          orange: 'orange-20'
        }
      ],
      key: 1,
      formThreadOptions: ['apple', 'banana', 'orange'],
      checkboxVal: defaultFormThread,
      formThread: defaultFormThread
    }
  },
  watch: {
    checkboxVal(valArr) {
      this.formThread = this.formThreadOptions.filter(i => valArr.indexOf(i) >= 0)
      this.key = this.key + 1
    }
  }
}
</script>
