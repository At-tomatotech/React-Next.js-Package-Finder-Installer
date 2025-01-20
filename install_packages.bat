@echo off
for /f "delims=" %%p in (packages.txt) do (
    echo Installing package: %%p
    npm install %%p
)
