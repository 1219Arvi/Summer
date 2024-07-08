
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import 'package:flutter_application_1/Modals/MyNotification.dart';
import 'package:flutter_application_1/widgets/drawer.dart';
import 'package:flutter_application_1/widgets/view_widger.dart';


class Firstpage  extends StatefulWidget {
  const Firstpage ({super.key});

  @override
  State<Firstpage> createState() => _FirstpageState();
}

class _FirstpageState extends State<Firstpage> {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar:AppBar(
          centerTitle :true,
          title: const Text("Notify'me" ,
           style: TextStyle(
            fontSize: 25,
            color: Colors.black,
            fontWeight: FontWeight.bold,
          
           ),),
          
        ),

        body : Padding(
          padding:const EdgeInsets.all(8.0),
          child: (ManagerModel.myNotifications != null && ManagerModel.myNotifications.isNotEmpty)
          ? ListView.builder(
            
            itemCount:ManagerModel.myNotifications.length,
            itemBuilder: (context, index) {
              return  ViewWidget(
                myNotification: ManagerModel.myNotifications[index],
                );
            },
          )

          :Center(
            child: CircularProgressIndicator(),)
        ),
        

        drawer : const MyDrawer() ,
    );
  }
}