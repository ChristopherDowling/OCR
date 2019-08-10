#SingleInstance force
#CommentFlag, //
#InstallKeybdHook

::/label::
Send ^a
Send ^c
Run "C:\Users\Admin\Desktop\Folder\Python\Programs\OCR\EmailFormat.bat"
Sleep, 1000
Send ^v
Send {Enter}
return
