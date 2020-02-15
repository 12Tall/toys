<template>
  <el-container>
    <Index></Index>
    <el-main>
      <textarea v-model="plain" v-on:scroll="EditorScroll"></textarea>
      <div id="previewer" v-html="T"></div>
    </el-main>
  </el-container>
</template>

<script>
import Vue from 'vue';
import Index from '@/components/MdEditor/Index';
import 'markdown-it-highlight/dist/index.css';

import MarkdownIt from 'markdown-it';
import { default as ml } from 'markdown-it-highlight';
import { default as mk } from 'markdown-it-latex';
import 'markdown-it-latex/dist/index.css';
const md = new MarkdownIt();
md.use(mk);
md.use(ml);

export default {
  name: 'Home',
  data() {
    return {
      // md: new MarkdownIt(),
      plain: '',
    };
  },
  computed: {
    T() {
      return md.render(this.plain);
    },
  },
  methods: {
    EditorScroll(e) {
      var editor = document.querySelector('textarea');
      var previewer = document.querySelector('#previewer');
      console.log(editor.scrollHeight / previewer.scrollHeight);
      let scale =
        (editor.scrollHeight - editor.clientHeight) /
        (previewer.scrollHeight - previewer.clientHeight);
      previewer.scrollTop = editor.scrollTop / scale;
    },
  },
  components: {
    Index,
  },
};
</script>
<style lang="stylus">
.el-container {
  display: flex;
  padding: 0;

  .el-aside {
    background-color: #333333;
  }

  .el-container {
    .el-main {
      background-color: #1e1e1e;
      display: flex;
      flex-direction: row;
      flex-wrap: nowrap;

      textarea {
        flex-grow: 1;
        font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', '微软雅黑', Arial, sans-serif;
      }

      #previewer {
        background-color: #ffffff;
        padding-left: 20px;
        margin: 0;
        text-align: left;
        flex-grow: 1;
        overflow-y: scroll;
      }
    }
  }
}
</style>