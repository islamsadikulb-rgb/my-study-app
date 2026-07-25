[app]

title = My Study App
package.name = mystudyapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0

android.api = 34
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a,armeabi-v7a

presplash.color = #FFFFFF

log_level = 2

[buildozer]

warn_on_root = 1
