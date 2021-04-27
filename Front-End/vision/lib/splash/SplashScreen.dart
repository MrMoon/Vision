import 'dart:async';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:vision/main.dart';

class SplashScreen extends StatefulWidget {
  final Color splashBackgroundColor = Colors.white;
  final TextStyle splashTextStyle = TextStyle(fontSize: 18.0 , fontWeight: FontWeight.bold , color: Colors.black);

  @override
  State<StatefulWidget> createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  String _versionName = 'V0.0.1';
  final splashDelay = 1;

  @override
  void initState() {
    super.initState();
    _loadWidget();
  }

  _loadWidget() async {
    var _duration = Duration(seconds: splashDelay);
    return Timer(_duration, visionHomePage);
  }

  void visionHomePage() {
    Navigator.pushReplacement(context, MaterialPageRoute(builder: (BuildContext context) => MyHomePage()));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: InkWell(
        child: Stack(
          fit: StackFit.expand,
          children: <Widget>[
            Column(
              mainAxisAlignment: MainAxisAlignment.start,
              children: <Widget>[
                Expanded(
                  flex: 7,
                  child: Container(
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: <Widget>[
                          Image.asset(
                            'images/img_splash.png',
                            height: 300,
                            width: 300,
                          ),
                          Padding(
                            padding: const EdgeInsets.only(top: 10.0),
                          ),
                        ],
                      )),
                ),
                Expanded(
                  child: Column(
                    children: <Widget>[
                      CircularProgressIndicator(),
                      Container(
                        height: 10,
                      ),
                      Row(
                          mainAxisAlignment: MainAxisAlignment.spaceAround,
                          children: <Widget>[
                            Spacer(),
                            Text(_versionName),
                            Spacer(
                              flex: 4,
                            ),
                            Text('androing'),
                            Spacer(),
                          ])
                    ],
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}