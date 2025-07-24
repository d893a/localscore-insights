@echo off
setlocal enabledelayedexpansion
echo Downloading LocalScore test results...

for /L %%i in (0,10,1210) do (
    set "num=000%%i"
    set "padded=!num:~-4!"
    echo \\rOffset !padded!...
    curl -Ls "https://localscore.ai/latest?offset=!padded!" -o "latest_!padded!.html"
    timeout /t 1 /nobreak >nul
)

echo Download complete. Files saved as latest_*.html
