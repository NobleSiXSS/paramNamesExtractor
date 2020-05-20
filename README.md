# paramNamesExtractor
Simple tool to extract param names from a url

The script requires two CLI arguments, the first one is mandatory and should be the url, the second is the filename to save the params in.
If no filename is given to the script the params will be printed in the terminal.

#### Examples:
```
python3 paramNameExtractor.py "https://www.google.com?q=hello&id=lol"
```
###### Output:
```
q
id
```
------------
```
python3 paramNameExtractor.py "https://www.google.com?q=hello&id=lol" output.txt
```
###### Output

```
cat output.txt

q
id
```

