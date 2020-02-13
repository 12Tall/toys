<template>
  <div id="app">
    <el-container>
      <el-header height="30px"></el-header>
      <el-aside width="50px"></el-aside>
      <el-footer height="30px"></el-footer>
    </el-container>
  </div>
</template>

<style lang="stylus">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0;
  padding: 0;
}

.el-footer {
  height: 100%;
}

.header {
  height: 30px;
  display: flex;
  margin: 0;
  padding: 0;
}
</style>
