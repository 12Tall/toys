<template>
  <div id="app">
    <el-container>
      <el-header height="30px"></el-header>
      <!-- css 设置不生效 style="padding:0" -->
      <el-main>
        <el-aside width="50px"></el-aside>
      </el-main>
      <el-footer height="30px"></el-footer>
    </el-container>
  </div>
</template>

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

.el-container {
  .el-header {
    background-color: blue;
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
<style>
/* .el-main {
  padding: 0;
} */
</style>
