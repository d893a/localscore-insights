@echo off
setlocal enabledelayedexpansion

REM Download LocalScore leaderboard data from test 0000 to 1210
echo Downloading LocalScore leaderboard data...

for /L %%i in (0,10,1210) do (
    set "num=000%%i"
    set "padded=!num:~-4!"
    echo \\rDownloading offset !padded!...
    curl -Ls "https://localscore.ai/latest?offset=!padded!" -o "latest_!padded!.html"
    timeout /t 1 /nobreak >nul
)

echo Download complete! Files saved as latest_XXXX.html

