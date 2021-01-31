import 'package:flutter/material.dart';
import 'package:pruebagg/pages/login.dart';
import 'package:pruebagg/pages/perfil.dart';
import 'package:pruebagg/pages/adopcionForm.dart';
import 'package:pruebagg/pages/adoptarForm.dart';
import 'pages/menu.dart';

void main() {
  runApp(MaterialApp(
    title: 'Adopt Me',
    theme: ThemeData(
      visualDensity: VisualDensity.adaptivePlatformDensity,
    ),
    initialRoute: LoginPage.id,
    routes: {
      LoginPage.id : (context) => LoginPage(),
    },
  ));
}
