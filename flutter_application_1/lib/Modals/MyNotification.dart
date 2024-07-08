class ManagerModel{
   static var myNotifications = [
    MyNotification(
      notice: "Update your system",
      app: "Settings",
      date: "23 Jan 24",
      time: "2:40 PM",
      image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRWf6NgPJP3RWRkIHzZ1xK7ZQXpwXQs742ChAxbuO1i0Q&s",
    ),
    
  ];


}


class MyNotification {
  final String notice;
  final String app;
  final String date;
  final String time;
  final String image;

  MyNotification( {required this.notice, required this.app, required this.date, required this.time , required this.image, });

  factory MyNotification.fromMap(Map<String , dynamic> map){
  return MyNotification(
    app:map["app"],
    notice:map["notice"],
    date:map["date"],
    time:map["time"],
    image :map["image"],
    
  );

  }

  toMap() => {
    "app":app,
    "notice":notice,
    "date":date,
    "time":time,
    "image":image,


  };


}









  

  






