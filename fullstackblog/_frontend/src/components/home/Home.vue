<template>
    <div>
        <el-menu theme="dark" :default-active="activeIndex" class="el-menu-demo" mode="horizontal">
            <el-menu-item index="1"><router-link to="/">Homepage</router-link></el-menu-item>
            <el-menu-item index="2" :style="{float: 'right'}">
                <router-link v-show="!user.name" to="/login">Login</router-link>
                <el-dropdown @command="loginOut">
                    <span :style="{color: '#fff'}" v-show="user.name">
                        {{user.name}}<i class="el-icon-caret-bottom el-icon--right"></i>
                    </span>
                    <el-dropdown-menu slot="dropdown">
                        <el-dropdown-item>Logout</el-dropdown-item>
                    </el-dropdown-menu>
                </el-dropdown>
            </el-menu-item>
        </el-menu>
        <el-card class="box-card">
            <p>Hello {{user.name}}</p>
        </el-card>
    </div>
</template>

<script>
export default {}
</script>