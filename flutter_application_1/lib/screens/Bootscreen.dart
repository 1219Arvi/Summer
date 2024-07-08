import'package:flutter/material.dart';
import 'package:flutter_application_1/utlitilies/routes.dart';

class BootScreen extends StatelessWidget {
  const BootScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return  Material(
      color: Colors.blue,
      child: Column(
        children: [
          Center(
            child: Image.asset(
             "assets/images/notifyme.png" ,
                     fit: BoxFit.cover,
                     ),
               
            
          ),
         ElevatedButton(
              child: Text("NOTIFY'ME"),
              onPressed:(){
                 Navigator.pushNamed(context, MyRoutes.loginRoute);}
                 )
  
        ],
            )
        
    );
     
  }
}
