<template>
    <div class="layout-usuario-form" :class="ocultarForm">
        <button class="txt-upper blanco-a titulo-usuario boton-cerrar" @click="ocultarFormulario">x</button>
        <h2 class="txt-upper blanco-a titulo-usuario">Crear usuario</h2>
        <form class="form" @submit.prevent="crearUsuario">
            <p class="blanco-a form__label">Correo</p>
            <input type="email" class="form__input" v-model="correo">
            <p class="blanco-a form__label">Nombre</p>
            <input type="text" class="form__input" v-model="nombre">
            <p class="blanco-a form__label">Apellido</p>
            <input type="text" class="form__input" v-model="apellido">
            <p class="blanco-a form__label">Contraseña</p>
            <input type="password" class="form__input" v-model="password">
            <p class="blanco-a form__label">Verifica password</p>
            <input type="password" class="form__input" v-model="password2">
            <p class="blanco-a form__label">Mina</p>
            <select class="form__input" v-model="mina">
                <option
                    v-for="(m, index) in minas"
                    :key="m"
                    :value="m">
                    {{ etiquetasMinas[index] }}
                </option>
            </select>
            <p class="blanco-a form__label">Zona</p>
            <select class="form__input" v-model="zona">
                <option 
                    v-for="(z, index) in zonas"
                    :key="z"
                    :value="z">
                    {{ etiquetasZonas[index] }}
                </option>
            </select>
            <!-- <button class="boton-crear boton-usuario blanco-a txt-upper">
                Guardar 
                <i class="fa-solid fa-user"></i>
            </button> -->
            <input type="submit" class="boton-crear boton-usuario blanco-a txt-upper" value="Guardar">
        </form>
    </div>
</template>

<script>
export default {
    props: {
        mostrarForm: {
            type: Boolean
        },
        usuario: {
            type: Object,
            required: false
        }
    },
    data() {
        return {
            correo: '',
            nombre: '',
            apellido: '',
            password: '',
            password2: '',
            mina: '',
            zona: '',
            ocultar: true,
            minas: [1, 2],
            zonas: [1,2,3,4],
            etiquetasMinas: ['HERMOSILLO', 'CANANEA'],
            etiquetasZonas: ['A', 'B', 'C', 'D']
        }
    },
    methods: {
        async crearUsuario() {
            try{
                const url = 'http://127.0.0.1:8000/api/usuarios/';
                const res = await fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-type': 'application/json; charset=utf-8'
                    },
                    body: JSON.stringify({
                        correo: this.correo,
                        nombre: this.nombre,
                        apellido: this.apellido,
                        password: this.password,
                        mina: this.mina,
                        zona: this.zona
                    })
                });
                const data = await res.json();
                const { status, statusText } = res;

                if(!res.ok) throw { status, statusText };

                console.log(data);
            }catch({ status, statusText }){
                const mensaje = statusText || 'Ocurrio un error';
                console.log(`Error ${status}: ${mensaje}`);
            }
        },  
        ocultarFormulario() {
            this.$emit('ocultarFormulario');
        },
        reiniciarCampos() {
            this.correo = '';
            this.nombre = '';
            this.apellido = '';
            this.password = '';
            this.mina = '';
            this.zona = '';
        }
    },
    computed: {
        ocultarForm() {
            return { 'ocultar-layout': this.mostrarForm }
        },
        passwordCorrecto() {
            return this.password === this.password2;
        },
        camposCompletados() {
            return (!this.correo)
                ? false
                : (!this.nombre)
                ? false
                : (!this.apellido)
                ? false
                : (!this.password)
                ? false
                : (!this.mina)
                ? false
                : !!this.zona
        }
    },
    watch: {
        usuario(newUsuario, oldUsuario){
            const { correo, nombre, apellido, mina, zona } = newUsuario;
            this.correo = correo;
            this.nombre = nombre;
            this.apellido = apellido;
            this.mina = mina;
            this.zona = zona;
        }
    }
}
</script>

<style scoped>
    .layout-usuario-form{
        position: fixed;
        top: 0;
        left: 0;
        z-index: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 100%;
        height: 100vh;
        background-color: rgba(17, 16, 16, 0.8);
        transition: all .8s ease-in-out;
    }
    .titulo-usuario{
        margin-bottom: 1rem;
    }
    .boton-usuario{
        margin-top: 1.8rem;
    }
    .ocultar-layout{
        transform: translateY(-100vh);
        visibility: hidden;        
    }
</style>