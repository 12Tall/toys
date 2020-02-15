<template>
  <el-container>
    <Index></Index>
    <el-main>
      <textarea v-model="plain"></textarea>
      <div id="previewer" v-html="T"></div>
    </el-main>
  </el-container>
</template>

<script>
import Vue from 'vue';
import Index from '@/components/MdEditor/Index';
import 'markdown-it-highlight/dist/index.css';

import MarkdownIt from 'markdown-it';
import { default as highlight } from 'markdown-it-highlight';
const md = new MarkdownIt();
md.use(highlight);

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
      }
    }
  }
}
</style>