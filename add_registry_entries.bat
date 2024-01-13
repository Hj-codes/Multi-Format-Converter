@echo off

:: List of supported file formats
set FILE_FORMATS=.gif .jpg .png .bmp .jpeg .mp4 .avi .mkv .mov .mp3 .wav

:: Set the MUIVerb value
reg add "HKEY_CLASSES_ROOT\*\shell\Convert" /v MUIVerb /t REG_SZ /d Convert /f

:: Set the SubCommands value
reg add "HKEY_CLASSES_ROOT\*\shell\Convert" /v SubCommands /t REG_SZ /d "" /f

:: Loop through each file format and create registry entries
for %%F in (%FILE_FORMATS%) do (
  reg add "HKEY_CLASSES_ROOT\*\shell\Convert\shell\%%F\command" /ve /t REG_SZ /d "\"C:\Path\To\Your\Python\python.exe\" \"C:\Path\To\Your\Script\Converter.py\" \"%%1\" \"%%F\"" /f
)

echo Registry entries added successfully.
pause
