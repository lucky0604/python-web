<template>
    <h1>Register</h1>
    <form method="post" @submit.prevent="reg()">
        <div>
            <p>Username</p>
            <input type="text" placeholder="Username" v-model="user.name" id="username"/>
        </div>
        <div>
            <p>Email</p>
            <input type="email" placeholder="Email" v-model="user.email" id="email"/>
        </div>
        <div>
            <p>Password</p>
            <input type="password" v-model="user.password" id="password" />
        </div>
        <div>
            <p>Re-type Password</p>
            <input type="password" v-model="user.retype_password" id="retype_password" />
        </div>

        <input type="submit" value="Submit" />
    </form>
</template>

<script>
import {mapActions} from 'vuex'
export default {
    data() {
        user: {
            name: '',
            email: '',
            password: '',
            retype_password: ''
        }
    },
    computed: {
        ...mapActions({
            UserReg: 'UserReg'
        })
    },
    methods: {
        reg() {
            this.$store.dispatch('UserReg', this.user)
        }
    }
}
</script>