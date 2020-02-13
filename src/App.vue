<template>
  <div id="app">
    <el-container>
      <el-header height="30px" style="-webkit-app-region:drag">
        <!-- no-drag 属性在css 设置里面不生效 -->
        <div class="title">
          <el-avatar shape="square" size="small" :src="logo"></el-avatar>
          <span>toys</span>
        </div>
        <div class="button" style="-webkit-app-region: no-drag">
          <i class="el-icon-arrow-down" @click="MenubarEnvent(2)"></i>
          <i class="el-icon-arrow-up" @click="MenubarEnvent(1)"></i>
          <i class="el-icon-close" @click="MenubarEnvent(0)"></i>
        </div>
      </el-header>
      <!-- css 设置不生效 style="padding:0" -->
      <el-main>
        <el-aside width="50px"></el-aside>
        <el-container>
          <el-aside width="150px"></el-aside>
          <el-main></el-main>
        </el-container>
      </el-main>
      <el-footer height="30px"></el-footer>
    </el-container>
  </div>
</template>

<script>
import { ipcRenderer } from 'electron';
export default {
  data() {
    return {
      logo: require('@/assets/logo.png'),
    };
  },
  methods: {
    MenubarEnvent(index) {
      ipcRenderer.send('menu', index);
    },
  },
};
</script>


<style lang="stylus">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

// 推荐类风格样式
.el-container {
  height: 100%;

  .el-header {
    color: #8f8f8f;
    background-color: #333333;
    padding: 0 10px 0 10px;
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: space-between;
    align-items: center;

    .title {
      height: 20px;
      display: flex;

      span {
        padding: auto;
      }

      .el-avatar {
        height: 20px;
        width: 20px;
        margin-right: 20px;
        background-color: #333333;
      }
    }

    .button {
      i {
        margin: 0 5px 0 1px;
        font-weight: bolder;
      }

      i:hover {
        color: #ffffff;
      }
    }
  }

  .el-main {
    display: flex;
    padding: 0;

    .el-aside {
      background-color: #333333;
    }

    .el-container {
      .el-aside {
        background-color: #252525;
      }

      .el-main {
        background-color: #1e1e1e;
      }
    }
  }

  .el-footer {
    background-color: #333333;
  }
}
</style>