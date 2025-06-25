import { useEffect } from "react";
import { Text, View, StyleSheet, Alert } from "react-native";

export default function Index() {
  const styles = StyleSheet.create({
    a:{ flex: 1,
        justifyContent: "center",
        alignItems: "center",
        flexWrap:"wrap",
        flexDirection:"row",
      },
    title:{fontSize:20}
  })
  const notifications = async () => {
    const response = await fetch('http://10.21.81.77:5000/getnotifications', {
    method:'GET'});
    const data = await response.json();
    Alert.alert("Conexão estabelecida", "Conexão estabelecida com sucesso")
  }
  useEffect(() =>{
    notifications();
  }, [])
  return (
    <View style={styles.a}>
      <View>
        <Text style={styles.title}>Conexão das Esp's-32</Text>
      </View>
      <View>
        
      </View>
    </View>
  );
}
