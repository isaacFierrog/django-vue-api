<template>
    <article 
        class="modulo"
        :class="estilosBorde">
        <div class="modulo-container">
            <p class="modulo-titulo blanco-a">Modulo</p>
            <h3 class="modulo-mac blanco-a">{{ modulo.mac }}</h3>
            <p class="blanco-b">{{ modulo.mina }} | {{ modulo.area }}</p>
        </div>
    </article>
</template>

<script>
export default {
    props: {
        modulo: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            bordes: ['red', 'blue', 'green', 'yellow']
        }
    },
    computed: {
        estilosBorde() {
            const color = Math.floor(Math.random() * 4);
            const colorBorde = this.bordes[color];
            return `border-${colorBorde}`; 
        }
    }
}
</script>
<style scoped>
    .border-red{
        border-top: 2rem solid rgb(219, 41, 41);
    }
    .border-blue{
        border-top: 2rem solid rgb(74, 41, 219);
    }
    .border-green{
        border-top: 2rem solid rgb(151, 219, 41);
    }
    .border-yellow{
        border-top: 2rem solid rgb(213, 216, 53);
    }
</style>