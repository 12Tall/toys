<template>
  <el-container>
    <Index></Index>
    <el-main>
      <Editor></Editor>
    </el-main>
  </el-container>
</template>

<script>
import Vue from 'vue';
import Index from '@/components/MdEditor/Index';
import Editor from '@/components/MdEditor/Ediitor';

import 'markdown-it-highlight/dist/index.css';

import MarkdownIt from 'markdown-it';
import { default as ml } from 'markdown-it-highlight';
import { default as mk } from 'markdown-it-latex';
import 'markdown-it-latex/dist/index.css';
const md = new MarkdownIt();
md.enable(['link', 'image']);
md.use(mk);
md.use(ml);

let editor, w;
export default {
  name: 'Home',
  data() {
    return {
    };
  },
  computed: {
    T() {
      return md.render(this.plain);
    },
  },
  components: {
    Index,
    Editor,
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
      flex-direction: row;
      flex-wrap: nowrap;
    }
  }
}
</style>