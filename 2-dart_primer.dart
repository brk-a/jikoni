void main(){
    print("staring simulation...");
    print("=======================================");
    print("scenario 1: no async-await");
    print(getData());
    print(greet("Kaka Sungura"));
    print("done");
    print("=======================================");
    print("scenario 2: async-await");
    print(getData());
    print(greet("Kaka Tai"));
    print("done");
    print("=======================================");
}

Future<String> getData() async {
    //simulate a network request for a uname
    await Future.delayed(Duration(seconds: 2), (){
        print("username: kakambwamwitu");
    });

    String Function() greeting = () => greet("Kaka Mbwamwitu");

    return greeting();
}

String greet(String name){
    return "Hi, $name!";
}