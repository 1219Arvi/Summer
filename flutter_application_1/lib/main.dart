

import 'package:flutter/material.dart';
import 'package:flutter_application_1/screens/Bootscreen.dart';
import 'package:flutter_application_1/screens/Firstpage.dart';
import 'package:flutter_application_1/screens/Loginscreen.dart';
import 'package:flutter_application_1/utlitilies/routes.dart';




void main(){
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
    
     darkTheme: ThemeData(
      brightness : Brightness.light),
     theme : ThemeData(
      primarySwatch: Colors.deepPurple,
      appBarTheme: const AppBarTheme(
        color:Colors.white,
        elevation: 0,
        iconTheme: IconThemeData(color: Colors.black,),

      )

     ),
     debugShowCheckedModeBanner: false,
     themeMode: ThemeMode.dark,
     initialRoute: "/boot",
     routes: {
       MyRoutes.homeRoute :(context) => const Firstpage() ,
       MyRoutes.loginRoute :(context) => const Loginscreen(),
       MyRoutes.bootRoute :(context) => const BootScreen()
     },
    );
  }
}

