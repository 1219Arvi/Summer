import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class MyDrawer extends StatelessWidget {
  const MyDrawer({super.key});

  @override
  Widget build(BuildContext context) {
    
    return  Drawer(
      child: Container(
        color: Colors.white,
        child: ListView(
          padding: EdgeInsets.zero,
          children: const [
            DrawerHeader(
                
             padding:EdgeInsets.zero,
              child: UserAccountsDrawerHeader(
                margin: EdgeInsets.zero,
                accountName: Text("Arvi",
                  style: TextStyle(
                    fontSize: 20,
                    
                  ),),
                
                accountEmail: Text('arvi051023@gmail.com',
                style: TextStyle(
                    fontSize: 20,
                  
                  ),),
                currentAccountPicture: CircleAvatar(
                  backgroundImage: NetworkImage("https://t4.ftcdn.net/jpg/00/64/67/27/360_F_64672736_U5kpdGs9keUll8CRQ3p3YaEv2M6qkVY5.jpg"),
                  
                ),
              ),
            ),
            ListTile(
              leading: Icon(
                CupertinoIcons.person_crop_circle_badge_exclam,
                color: Colors.white,
              ),
              title:Text("About",
              style : TextStyle(
                color: Colors.black,
              ))
            ),
            ListTile(
              leading: Icon(
                CupertinoIcons.question_circle,
              ),
              title:Text("Permissions"
              ,style :TextStyle(
                color: Colors.black,
              )
              )
            ),
            ListTile(
              leading: Icon(
                CupertinoIcons.mail,
              ),
              title:Text("Contact Me"
              ,style :TextStyle(
                color: Colors.black,
              )
              )
            )
          ],
        
        ),
      ),
    );
  }
}