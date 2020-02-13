<template>
  <div id="app">
    <el-container>
      <el-header height="30px" style="-webkit-app-region:drag">
        <!-- no-drag 属性在css 设置里面不生效 -->
        <span>toys</span>
        <div style="-webkit-app-region: no-drag">
          <v-icon @click="MenubarEnvent(2)" scale="1.5" name="window-minimize"></v-icon>
          <v-icon @click="MenubarEnvent(1)" scale="1.5" name="window-maximize"></v-icon>
          <v-icon @click="MenubarEnvent(0)" scale="1.5" name="window-close"></v-icon>
        </div>
      </el-header>
      <!-- css 设置不生效 style="padding:0" -->
      <el-main>
        <el-aside width="50px"></el-aside>
      </el-main>
      <el-footer height="30px"></el-footer>
    </el-container>
  </div>
</template>

<script>
import { ipcRenderer } from 'electron';
export default {
  data() {
    return {};
  },
  methods: {
    MenubarEnvent(index) {
      ipcRenderer.send('menu', index);
    },
  },
};
</script>


<style lang="stylus">
* {
  margin: 0;
  padding: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

// 推荐类风格样式
.el-container {
  .el-header {
    background-color: gray;
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-items: center;
    width: 100%;

    span {
      height: 20px;
    }

    div {
      svg {
        margin: 0 1px 0 1px;
        padding: 0;
      }

      svg:hover {
        color: #000;
      }
    }
  }

  .el-main {
    padding: 0;

    .el-aside {
      background-color: green;
    }
  }

  .el-footer {
    background-color: red;
  }
}
</style>
