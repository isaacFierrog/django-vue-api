<template>
    <div>
        <h1>Esta es la vista de Login</h1>
        <LoginForm/>
    </div>
</template>

<script>
    import { defineAsyncComponent } from 'vue';
export default {
    components: {
        LoginForm: defineAsyncComponent(
            () => import('../components/LoginFormComponent.vue')
        )
    }
}
</script>