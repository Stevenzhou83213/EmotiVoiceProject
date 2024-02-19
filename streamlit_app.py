Notepad++ v8.6.3 bug-fixes & new enhancements:

 1. Restore multi-editing option & add "Column To Multi-editing" option on GUI.
 2. Make "copy/cut line while no selection" optional.  
 3. Fix all open files lost after restarting as Admin to save a file.  
 4. Fix "Replace All" crash & performance issue.  
 5. Fix calltip crash due to the division by zero.  
 6. Enhance Function List for Python to support "async def" & colons in argument list.  
 7. Fix Copy/Cut/Paste issue in Vertical Edge text field in preferences dialog.  
 8. Fix macro recording twice for some commands.  
 9. Fix "Open File" command not working with TAB preceded.  
10. Add auto-completion keywords for PHP, JavaScript and CSS.

Get more info on
https://notepad-plus-plus.org/downloads/v8.6.3/


Included plugins:

1.  NppExport v0.4
2.  Converter v4.6
3.  Mime Tool v3.1


Updater (Installer only):

* WinGUp (for Notepad++) v5.2.8


import os

def run_project():
    # 运行项目
    os.system("streamlit run demo_page.py --server.port 6006 --logger.level debug")

if __name__ == "__main__":
    run_project()

import streamlit as st

def main():
    st.title("My Streamlit App")
    st.write("Hello, world!")

if __name__ == "__main__":
    main()
