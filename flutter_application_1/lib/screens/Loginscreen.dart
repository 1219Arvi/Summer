import 'package:flutter/material.dart';
import 'package:flutter_application_1/utlitilies/routes.dart';



class Loginscreen  extends StatefulWidget {
  const Loginscreen ({super.key});

  @override
  State<Loginscreen> createState() => _LoginscreenState();
}

class _LoginscreenState extends State<Loginscreen> {

  bool changeButton=false;
  String name ="Arvi";
  final _formKey =GlobalKey<FormState>();

  moveToHome (BuildContext, Context)  async {


    if(_formKey.currentState!.validate()){

    setState(() {
        changeButton=true;
         });
         await Future.delayed(Duration(seconds: 1));
         Navigator.pushNamed(context, MyRoutes.homeRoute);
         setState(() {
         changeButton=false;
           });

  }}

  @override
  Widget build(BuildContext context) {
    return Material(
      color:Colors.white ,
      child:SingleChildScrollView(
       child :Form(
         key : _formKey,
           autovalidateMode: AutovalidateMode.onUserInteraction,
         
         child: Column(
          children: [
            Image.asset(
              "assets/images/login_page.png",
              fit: BoxFit.cover,
            ),
         
             SizedBox(
              height:20.0,
            ),
         
             Container(
               decoration: BoxDecoration(
                color: Color.fromARGB(255, 101, 42, 230),
               ),
               width: 1000,
               height: 70,
               child:Center(
                child: Text(
                "Welcome $name",
                style: TextStyle(
                  fontSize: 28,
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                  
                ),
              ),
              ),
             ),
            const SizedBox(
            height: 20.0,
            ),
            Padding(
              padding:
               const EdgeInsets.symmetric(vertical:16.0 , horizontal: 32.0),
              child: Column(
                children: [
                   TextFormField(
                    obscureText: true,
                    onChanged:(value){
                      name=value;
                      setState((){
                      });
                    } ,
                    decoration: InputDecoration(
                      hintText: "Enter UserName",
                      labelText: "Username",
                      ),
                    validator: (value){
                        if (value!.isEmpty){
                          return "Username Cannot be empty";}
                        else{
                          return null;
                    }}
                 ),
         
                   TextFormField(
                    obscureText: true,
                     decoration:InputDecoration(
                       hintText: "Enter password",
                       labelText:"Password",
                      ),
                      validator: (value){
                        if (value!.isEmpty){
                          return "Password Cannot be empty";}
                        else if (value.length<5){
                          return "Password length should not be greater then 5";
                        }
                        return null;
                      

                      }
                      ,
                    ),
         
                   SizedBox(
                    height: 40.0,
                   ),
         
                   Material(
                    color: Color.fromARGB(255, 101, 42, 230),
                    borderRadius: BorderRadius.circular(changeButton? 20: 10),
                     child: InkWell(
                       onTap: () async {
                        await moveToHome(BuildContext, context );
                        
                       },
                       child: AnimatedContainer(
                        duration: Duration(seconds:1),
                        width: changeButton? 50 :150,
                        height : 50,
                        alignment: Alignment.center,
                        
                        child: Text("Login",
                        style:TextStyle(
                          color: Colors.white,
                          fontWeight: FontWeight.bold,
                          fontSize:20),
                        )
                        ),
                     ),
                   ),
                    
         
                   
         
                  // ElevatedButton(
                   // onPressed: (){
                   //   Navigator.pushNamed(context, MyRoutes.homeRoute);
         
                   // }, 
                   // child: Text("Login"),
                    //style: TextButton.styleFrom(
                     // minimumSize: Size(120, 40),
         
                   // ),
         
         
                ],
              ),
            )
          ],
               ),
       ))
    );
  }
}