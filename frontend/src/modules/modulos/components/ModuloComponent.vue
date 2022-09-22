<template>
    <div>
        <h3>{{ modulo.mac }}</h3>
        <p>{{ modulo.mina }} | {{ modulo.area }}</p>
    </div>
</template>

<script>
export default {
    props: {
        modulo: {
            type: Object,
            required: true
        }
    }
}
</script>