import servicio from '../services/moduloServicio.js';


const recurso = 'modulos';

export default {
    get(){
        return servicio.get(recurso);
    },
    post(data){
        return servicio.post(recurso, data);
    }
}