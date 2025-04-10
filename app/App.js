import { NavigationContainer, useLinkProps } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { Login } from './login';
import { navigationRef } from './navigation';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { useState } from 'react';

const Stack = createNativeStackNavigator();
const Tab = createBottomTabNavigator();

function Tabs() {
  return (
    <Tab.Navigator initialRouteName='Home' screenOptions={({ route }) => ({
      headerShown: false,
      tabBarIcon: ({ focused, color, size }) => {
        let iconName;

        if (route.name === 'Home') {
          iconName = focused
            ? 'home'
            : 'home-outline';
        } else if (route.name === 'Favorites') {
          iconName = focused ? 'heart-sharp' : 'heart-outline';
        }
        return <Ionicons name={iconName} size={size} color={color} />;
      },
      tabBarActiveTintColor: 'green',
      tabBarInactiveTintColor: 'gray',
    })}>
      <Tab.Screen name="Home" component={Home} />
      <Tab.Screen name="Favorites" component={ListFavorites} />
    </Tab.Navigator>
  );
}
export default function App() {
  const [isLogged, setIsLogged] = useState(false);
  return (
    <NavigationContainer ref={navigationRef}>
      <Stack.Navigator initialRouteName="Login" screenOptions={{ headerShown: false }}>
        {
          isLogged ? (
            <>
              <Stack.Screen name="Tabs" component={Tabs} />
              <Stack.Screen name="UniquePokemon" component={Unique} />
            </>
          ) : (
            <Stack.Screen name="Login">
              {(props) => <Login {...props} onLogin={() => setIsLogged(true)} />}
            </Stack.Screen>
          )
        }
      </Stack.Navigator>
    </NavigationContainer>
  );
}