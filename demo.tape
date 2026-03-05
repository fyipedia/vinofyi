# vinofyi — Python Wine Encyclopedia Demo
Output demo.gif

Set FontSize 14
Set Width 920
Set Height 620
Set Shell "zsh"
Set Theme "Catppuccin Mocha"
Set TypingSpeed 35ms
Set Padding 20

Type `curl -s 'https://vinofyi.com/api/search/?q=pinot+noir' | jq '.results[:3][] | {name, type}'`
Enter
Sleep 3s

Type `curl -s 'https://vinofyi.com/api/grape/pinot-noir/' | jq '{name, color, body, acidity}'`
Enter
Sleep 3s

Type `curl -s 'https://vinofyi.com/api/random/' | jq '{name, type}'`
Enter
Sleep 3s

Sleep 2s
