<template>
    <article>
        {{ sensor.clave }}
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