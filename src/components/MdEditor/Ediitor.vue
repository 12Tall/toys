<template>
  <div class="container">
    <div class="editor">
      <textarea @scroll="EditorScroll" v-model="md"></textarea>
    </div>
    <div class="line"></div>
    <div class="pereviewer" v-html="Html"></div>
  </div>
</template>

<script>
import Vue from 'vue';

import 'markdown-it-highlight/dist/index.css';

import MarkdownIt from 'markdown-it';
import { default as ml } from 'markdown-it-highlight';
import { default as mk } from 'markdown-it-latex';
import 'markdown-it-latex/dist/index.css';
const md = new MarkdownIt();
md.enable(['link', 'image']);
md.use(mk);
md.use(ml);

export default {
  data() {
    return {
      md: '',
    };
  },
  computed: {
    Html() {
      return md.render(this.md);
    },
  },
  mounted() {
    this.Resize();
  },
  methods: {
    EditorScroll(e) {
      var editor = document.querySelector('textarea');
      var previewer = document.querySelector('.pereviewer');
      console.log(editor.scrollHeight / previewer.scrollHeight);
      let scale =
        (editor.scrollHeight - editor.clientHeight) /
        (previewer.scrollHeight - previewer.clientHeight);
      previewer.scrollTop = editor.scrollTop / scale;
    },
    Resize() {
      let cont = document.querySelector('.container'),
        line = document.querySelector('.line'),
        editor = document.querySelector('.editor'),
        pereviewer = document.querySelector('.pereviewer');
      cont.style.setProperty('--varW', '50%');
      line.onmousedown = (e) => {
        console.log('md');
        let startX = e.clientX;
        line.left = line.offsetLeft;
        let contW = editor.offsetWidth + pereviewer.offsetWidth;

        let p = parseFloat(
          cont.style
            .getPropertyValue('--varW')
            .trim()
            .replace('%', ''),
        );
        document.onmouseup = (e) => {
          cont.style.cursor = 'default';
          document.onmousemove = null;
          document.onmouseup = null;
        };
        document.onmousemove = (e) => {
          if (e.buttons !== 1) {
            cont.style.cursor = 'default';
            document.onmousemove = null;
            document.onmouseup = null;
            return;
          }
          let endX = e.clientX;
          if (Math.abs(endX - line.offsetLeft) < 10) {
            cont.style.cursor = 'ew-resize';
          }
          let per = parseFloat(((endX - startX) * 100) / contW + p);
          if (per < 100 && per > 0) {
            cont.style.setProperty('--varW', per + '%');
          }
        };
      };
    },
  },
};
</script>
<style lang="stylus" scoped>
* {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
}

.container {
  overflow: hidden;
  text-align: left;
  --varW: '50%';

  .editor {
    display: inline-block;
    width: calc(var(--varW) - 2px);
    height: 100%;
    background-color: red;

    textarea {
      margin: 0;
      padding: 0;
      font-family: Avenir, Helvetica, Arial, sans-serif;
    }
  }

  .line {
    display: inline-block;
    width: 4px;
    height: 100%;
    background-color: white;
    cursor: ew-resize;
  }

  .pereviewer {
    vertical-align: top;
    display: inline-block;
    width: calc(100% - var(--varW) - 4px);
    height: 100%;
    background-color: green;
    overflow-y: auto;
  }
}
</style>