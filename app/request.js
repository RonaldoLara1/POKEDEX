import AsyncStorage from '@react-native-async-storage/async-storage';
import axios from 'axios';
import { navigate } from './navigation';
export const request = axios.create({
    baseURL:"https://fmp93vzr-5000.usw3.devtunnels.ms"
})
//Esto se va a ejecutar antes de hacer la peticion
request.interceptors.request.use(async(config) => {
    const token = await AsyncStorage.getItem("token");
    if (token){
        config.headers.Authorization = `Bearer ${token}`
    }
    return config;
});

//Esro se va a ejecutar INMEDIATAMENTE despues de recibir una respuesta
request.interceptors.response.use(
    (response) => response,
    async (error) => {
        if (error.response && error.response.status === 401){
            await AsyncStorage.removeItem("token");
            navigate("Login")
        }
        return Promise.reject(error);
    }
);