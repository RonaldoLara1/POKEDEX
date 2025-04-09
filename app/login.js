import { useNavigation } from "@react-navigation/native";
import React, { useState } from "react";
import { Alert } from "react-native";
import { request } from "./request";
import AsyncStorage from "@react-native-async-storage/async-storage";

export const Login = () => {
    const [data, setData] = useState({});
    const [loading, setLoading] = useState(false);
    const {navigate}=useNavigation();

    const onChange = (target,value) =>{
        const newData = data;
        console.log(target, value)
        newData[target] = value;
        setData(newData)
    }

    const submit = async ()=>{
        try {
            setLoading(true)
            const res = await request.post("/users/login", data)
            const {token} = res.data;
            AsyncStorage.setItem("token", token);
            navigate("Home")
        } catch (error) {
            Alert.alert("Ocurrio un error", "Credenciales Invalidas")
        }
        setLoading(false)

    }
    return(
        <View style={styles.container}>
              
              <View>{/*container-image*/}
                <Image source={{uri:"https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Pok%C3%A9_Ball_icon.svg/2052px-Pok%C3%A9_Ball_icon.svg.png"}}
                width={200}
                height={200}
                />
              </View>
              <View>{/*container-form*/}
                <Text style={styles.title}>Iniciar Sesion</Text>
                <Text style={styles.label}>Correo:</Text>
                <TextInput style={styles.input}onChangeText={(text)=>onChange("email",text)} autoCapitalize='none'/>
                <Text style={styles.label}>Contraseña:</Text>
                <TextInput style={styles.input}onChangeText={(text)=>onChange("password",text)} secureTextEntry/>
                <Pressable style={styles.send}onPress={submit} disable={loading}>
                  <Text style={styles.textButton}>Enviar</Text>
                </Pressable>
              </View>
              <View style={styles.containerFooter}>
                <Text style={styles.containerFooter}>¿Olvidaste tu Contraseña?</Text>
                <Text style={styles.containerFooter}>Registrate</Text>
              </View>
            </View>
    )
}
const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#fff',
      alignItems: 'center',
      justifyContent: 'center',
      padding: 10
    },
    title:{
      fontSize:24,
      fontWeight:"hold"
    },
    label:{
      fontSize:15,
      fontWeight:'bold'
    },
    input:{
      borderRadius:10,
      borderWidth:2,
      borderColor:"black",
      fontSize:15,
      width:"auto"
    },
    send:{
      backgroundColor:"red",
      width:"auto",
      height:"auto",
      borderRadius:10,
      marginTop:15,
      alignItems:"center",
      textButton:{
        color:"white",
        fontSize:20,
        fontWeight:"bold",
      }
    },
    containerFooter:{
      justifyContent:'center',
      alignItems:"center",
      texts:{
        fontSize:20,
        margin:5
      }
    }
  });
  