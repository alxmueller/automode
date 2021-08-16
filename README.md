# Automatic Light/Dark Mode Switching for iTerm2

[iTerm2](https://iterm2.com) doesn't come with built-in support for automatically switching between color schemes based on macOS's appearance settings.  Fortunately, however, it has a powerful Python API that will allow you to do this programmatically.  Hence the idea for ✨**automode**✨.  This little Python script will automatically switch between two given profiles depending on your system's appearance.

## Installation

1. Create a _\~/Library/ApplicationSupport/iTerm2/Scripts/AutoLaunch_ folder if it doesn't already exist.  If you can't find your _\~/Library_ folder that's because it's hidden by default in newer macOS versions.  In this case, go to the _Go_ menu in _Finder_ while holding down the _Option_ (⌥) key – there it is.

2. Copy  _automode.py_ to the _\~/Library/ApplicationSupport/iTerm2/Scripts/AutoLaunch_ folder.

3. Open _automode.py_ in your editor of choice and replace _"Light Profile"_ and _"Dark Profile"_ with the names of the actual profiles you want to use for light and dark mode.

4. Enable Python support in iTerm2.

   ![Enable Python support](https://user-images.githubusercontent.com/1433751/129531101-e77084aa-d17f-4f07-87a4-4cfe779e807e.png)

5. Activate _automode.py_.

   ![Activate automode.py](https://user-images.githubusercontent.com/1433751/129531189-d8642634-a3c9-4467-b250-68b79a234c46.png)
