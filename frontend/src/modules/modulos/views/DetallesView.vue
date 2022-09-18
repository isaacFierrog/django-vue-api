<template>
    <div>
        <h1>Detalles del Modulo {{ id }}</h1>
    </div>
</template>

<script>
export default {
    props: {
        id: {
            type: Number,
            required: true
        }
    },  
    created(){
        this.obtenerPokemon();
    },
    data(){
        return {
            pokemon: null
        }
    },
    methods: {
        async obtenerPokemon(){
            try{
                const res = await fetch(`https://pokeapi.co/api/v2/pokemon/${ this.id }`);
                
                if(!res.ok) throw { status, statusText };
                
                const data = await res.json();
                const { status, statusText } = res;

                console.log(data);
                this.pokemon = data;
            }catch({ status, statusText }){
                this.$router.push({ name: 'not-found' });
            }
        }
    },
    watch: {
        id(){
            this.obtenerPokemon();
        }
    }
}
</script>