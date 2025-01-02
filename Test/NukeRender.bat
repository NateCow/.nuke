@echo off

title Batch Render Nuke Scripts!

rem Mode is the window size, in "columns, lines"
mode 45, 10

rem ======================
rem MAKE A CHOICE
rem ======================

echo.
echo                  WELCOME!
echo.
echo.

CHOICE /M "Would you like to begin rendering?"

IF ERRORLEVEL 2 GOTO :End
IF ERRORLEVEL 1 GOTO :Begin

rem ============================
rem BEGIN THE BATCH RENDER
rem ============================

:Begin

rem ======================================
rem SETTING PATH TO EXECUTE RENDER
rem ======================================

rem Add -f (full resolution) flag before -F (frame range) flag
rem Figure out how to keep console windows open so I know if they finished or spit out an error.

path="C:\Program Files\Nuke10.0v4\"



start "BJS_001_007_cmp_main_v001" Nuke10.0.exe -i -X CowWrite2 -F 1001-1320 "K:/Freelance/BenJerrys/5-SHOTS/001/BJS_001_007/Comp/Nuke/BJS_001_007_cmp_main_v001.nk"



:End
title No Renders made...
cls

exit