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
  });
  const sleep = (ms:any) => {return new Promise(resolve => setTimeout(resolve, ms))}
  const notifications = async () => {
    while(true){
      const response = await fetch('http://10.21.81.77:5000/get_notifications', {method:'GET'});
      const data = await response.json();
      data.notifications.forEach((notification:any, index:any) => {
        Alert.alert(notification.token_key+" was seen at "+String(notification.ts));
        alert(notification.token_key+" was seen at "+String(notification.ts));
      });
      await sleep(1000);
    }
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
