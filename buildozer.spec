[app]

# (str) Title of your application
title = PetPal Assistant

# (str) Package name
package.name = petpal

# (str) Package domain (needed for android packaging)
package.domain = org.petpal

# (str) Source files where the app lives (relative to dir)
source.dir = .

# (list) Source files to include (let it decide)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.min_api = 21

# Automatically accept Android SDK licenses to allow build-tools and aidl to download properly
android.accept_sdk_license = True
