[app]

# (str) Title of your application
title = MyKivyMDApp

# (str) Package name (unique identifier)
package.name = mykivymdapp

# (str) Package domain (reverse DNS style)
package.domain = org.example

# (str) Source code directory (default is current dir)
source.dir = .

version = 0.1
# (list) Application requirements
# Add kivymd, kivy, python-for-android, and other python libs you use
requirements = python3,kivy==2.1.0,kivymd

# (str) Entry point, main python file to launch
# If your main app is main.py, set this; otherwise adjust accordingly
entrypoint = main.py

# (str) Supported orientation: portrait, landscape or all
orientation = portrait

# (bool) Indicate if the application is fullscreen or not
fullscreen = 1

# (str) Icon of the app (relative path to image)
# icon.filename = %(source.dir)s/icon.png

# (list) Permissions your app needs
android.permissions = INTERNET

# (int) Target API level (set according to latest stable, 33+ recommended)
android.api = 33

# (int) Minimum API your app supports (Android version)
android.minapi = 21

# (int) Android SDK build tools version
android.sdk = 33

# (str) Android NDK version (usually pinned for compatibility)
android.ndk = 25b

# (bool) Use Android X support libraries
android.androidx = True

# (list) Additional Java classes or libraries, if needed
# android.add_jars =

# (str) Presplash screen image file (optional)
# presplash.filename = %(source.dir)s/presplash.png

# (bool) Copy assets (images/fonts) automatically
copy_assets = True

# (list) Include additional files or folders
# e.g. include data files your app loads at runtime
# source.include_exts = py,png,jpg,kv,atlas,ttf,json

# (int) Number of python threads (optional)
# p4a.threads = 2

# (bool) Enable or disable logcat logging
log_level = 2

# (bool) Run in debug mode
debug = 1
