import 'package:flutter/material.dart';
import 'package:flutter_application_1/Modals/MyNotification.dart';

class ViewWidget extends StatelessWidget {
  final MyNotification myNotification;

  const ViewWidget({super.key, required this.myNotification});




  

  @override
  Widget build(BuildContext context) {
    return Card (
      child :ListTile(
      leading: Image.network(myNotification.image),
      title: Text (myNotification.app),
      subtitle: Text(myNotification.notice),
      trailing: Text(myNotification.date  ), 
      

   
    )
    );
  }
}