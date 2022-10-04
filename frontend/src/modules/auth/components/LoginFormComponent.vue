<template>
    <div>
        <h2>Formulario</h2>
        <form @submit.prevent="autenticarUsuario">
            <input 
                type="text" 
                placeholder="Correo de usuario"
                v-model="correo">
            <input 
                type="password" 
                placeholder="Password de usuario"
                v-model="password">
            <input type="submit" value="Ingresar">
        </form>
        <pre>{{ $data }}</pre>
    </div>
</template>

<script>
    import VueJwtDecode from 'vue-jwt-decode'

export default {
    data(){
        return {
            correo: '',
            password: ''
        }
    },
    methods: {
        async autenticarUsuario() {
            const url = 'http://127.0.0.1:8000/api/login/';

            try{
                const res = await fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-type': 'application/json; charset=utf-8',
                    },
                    body: JSON.stringify({
                        correo: this.correo,
                        password: this.password
                    })
                });
                const data = await res.json();
                const { status, statusText } = res;
                
                if(!res.ok) throw { status, statusText };
                
                const { refresh, access } = data;
                console.log({ refresh, access });
                console.log(VueJwtDecode.decode(access));
            }catch({ status, statusText }){
                const mensaje = statusText || 'Ocurrio un error';
                console.log(`Error ${status}: ${mensaje}`);
            }
        }
    }
}
</script>