import { Text, View, StyleSheet } from "react-native";

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
