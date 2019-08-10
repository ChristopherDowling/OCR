OCR
===
Edits, scans, and formats text from shipping labels

Alpha functionality:
Drag and drop .zip on to OCR.bat to run
(Poor) post-OCR error correction
Requires "requests" module to run

TODO:
Test to make sure images come out in proper order
Make program automatically open .csv when completed?
More post-processing (get ALL the labels)
Make program print off the labels too?
Format .csv in proper form
Create a sister program that formats email contents?
Test for portability (between computers, between OSes)
Add more comments for future support

EmailFormat
===========
Requires easygui

Run EmailFormat.ahk first
Open email with labels
Type /label and hit enter or space
Copy the text that pops up
Paste text in to Manifest Column
