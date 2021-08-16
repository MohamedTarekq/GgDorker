![Alt text](images/GgDorker.jpg)

[![Github All Releases](https://img.shields.io/static/v1?label=GgDorker&message=V1.0&color=green)]()
[![Github All Releases](https://img.shields.io/badge/support-python%203.7%2F3.8%20%2B-brightgreen)]()
[![Github All Releases](https://img.shields.io/badge/platform-windows%20%7C%20linux-lightgrey)]()
[![License](https://img.shields.io/badge/license-MIT-_red.svg)](https://opensource.org/licenses/MIT)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/MohamedTarekq/GgDorker/issues)
![Twitter Follow](https://img.shields.io/twitter/follow/timooon107?style=social)


# GgDorker : 
**GgDorker**  is a simple python tool that automates the process of ***Google Dorking*** 
(*current Version 1.0*)  



  

## Installation :

```bash
git clone https://github.com/MohamedTarekq/GgDorker.git
cd GgDorker
python3 -m pip install -r requirements.txt
python3 GgDorker.py -h
```

# Usage :
Run dorks only on your target, you must add `site:` before your domain name such as **site:example.com** when using `dorks.txt` list
```
▶ python3 GgDorker.py -t site:twitter.com -d dorks.txt
```
Run dorks on your target in another sites like (trello,pastebin,stackoverflow,coggle ..etc)
```
▶ python3 GgDorker.py -t twitter.com -d OSINT_dorks.txt
▶ python3 GgDorker.py -t twitter -d OSINT_dorks.txt
```
## Specific dork
You can run specific dork and set the number of pages by `-p` flag: 
```
▶ python3 GgDorker.py -q "site:hackerone.com intext:information disclosure" -p 5
```
## Extract subdomains from Google Engine
By using `--subs` and `silent mode` by set `-s` flag:
```
▶  python3 GgDorker.py -t twitter.com --subs -p 50 -s
```

## Concurrency

You can set the concurrency level with the `-n` flag:

```
▶ python3 GgDorker.py -t twitter.com -d OSINT_dorks.txt -n 10
```

## Output 
you can save your results in `cvs` or `txt` file
```
▶ python3 GgDorker.py -t site:twitter.com -d dorks.txt -o twitter_output.cvs
▶ python3 GgDorker.py -t site:twitter.com -d dorks.txt -o twitter_output.txt
```

# wordlist
I used two wordlists `dorks.txt` and `OSINT_dorks.txt` 
If you have a good wordlist feel free to issue pull requests with it! :)

# Demo 
![Alt text](images/demo.gif)



# Credits

- This tool was inspired by [@knassar702](https://github.com/knassar702/startpage-parser)'s module. Thanks to him for the great idea!
- Special thanks to [@Asem Eleraky](https://github.com/Melotover) who incouraged and supported me to write this tool

# Donation
If this tool helped you to get a bounty and you like it , feel free to give me a cup of coffee :) 

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://paypal.me/mtarek107)
 

# Disclaimer

This Tool is Made For Educational and Ethical testing purposes only.
Usage of this tool for Attacking targets without permission is illegal.
Developers Assume no liability and are not responsible for any misuse or damage caused by this tool.
