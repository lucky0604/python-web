<template>
  <div class="components-container">
    <code>富文本编辑器选择之前做集团门户后台CMS系统使用的TinyMCE，之前是通过Django框架的模版引擎来进行页面渲染，此次第一次使用纯js来配置。</code>
  <div>
    <Tinymce :height="200" ref="editor" v-model="content"></Tinymce>
  </div>
  <div class="editor-content" v-html="content"></div>
  </div>
</template>

<script>
import Tinymce from 'components/Tinymce'

export default {
  components: {Tinymce},
  data() {
    return {
      content: 'Tinymce'
    }
  }
}
</script>

<style scoped>
.editor-content{
  margin-top: 20px;
}
</style>