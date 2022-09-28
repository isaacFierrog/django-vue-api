<template>
    <article>
        <h3>{{ sensor.clave }}</h3>
    </article>
</template>

<script>
export default {
    props: {
        sensor: {
            type: Object,
            required: true
        }
    }
}
</script>