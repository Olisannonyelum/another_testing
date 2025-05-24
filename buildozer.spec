[app]

title = MyKivyMDApp
package.name = mykivymdapp
package.domain = org.example
version = 0.1

source.dir = .

requirements = python3,kivy==2.1.0,kivymd

orientation = portrait
fullscreen = 1

entrypoint = main.py

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.androidx = True
