@echo off
for %%F in (*) do (
    if "%%~xF"=="" (
        ren "%%~F" "%%~nF.txt"
    )
)