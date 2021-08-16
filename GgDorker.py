#!/usr/bin/python3
import requests
from termcolor import colored 
import re
from multiprocessing.dummy import Pool
import csv
import argparse
from urllib.parse import quote


def logo():
    print(" ")
    print(" ")
    print(colored("          .oooooo.               oooooooooo.                      oooo                           ", "red", attrs=['bold']))
    print(colored("         d8P'  `Y8b              `888'   `Y8b                     `888                           ", "red", attrs=['bold']))
    print(colored("        888            .oooooooo  888      888  .ooooo.  oooo d8b  888  oooo   .ooooo.  oooo d8b ", "red", attrs=['bold']))
    print(colored("        888           888' `88b   888      888 d88' `88b `888""8P    888 .8P'  d88' `88b `888""8P ", "red", attrs=['bold']))
    print(colored("        888     ooooo 888   888   888      888 888   888  888      888888.   888ooo888  888     ", "red", attrs=['bold']))
    print(colored("        `88.    .88'  `88bod8P'   888     d88' 888   888  888      888 `88b. 888    .o  888     ", "red", attrs=['bold']))
    print(colored("         `Y8bood8P'   `8oooooo.  o888bood8P'   `Y8bod8P' d888b    o888o o888o `Y8bod8P' d888b    ", "red", attrs=['bold']))
    print(colored("                       d'     YD                                                                  ", "red", attrs=['bold']))
    print(colored("                       'Y88888P'                                                              ", "red", attrs=['bold'])+"v1.0")
    print(" ")
    print(colored("                  Coded by ", "white", attrs=['bold']) + colored("Mohamed Tarek", "yellow", attrs=['bold']))
    print(colored("         Twitter: ", "white", attrs=['bold']) + colored("https://twitter.com/timooon107", "yellow", attrs=['bold']))
    print(colored("         linkedin:","white", attrs=['bold']) + colored("https://www.linkedin.com/in/mohammed-tarekq", "yellow", attrs=['bold']))                                                                     
    print(" ")
    print(" ")

parser = argparse.ArgumentParser(description=colored("Simple python Tool That Automates The Process of Google Dorking","green", attrs=['bold']))
parser.add_argument("-d", "--dorks", help="dorks file ")
parser.add_argument("-t", "--target", help="Your target (-t site:tesla.com| -t tesla.com | -t tesla)")
parser.add_argument("-q", "--query", help="only query one dork")
parser.add_argument("--subs", help="collect subdomains from Google",action="store_true")
parser.add_argument("-s", "--silent", help="Silent Mode only Show The Results",action="store_true")
parser.add_argument("-n", "--threads", help="Maximum n threads, default=5",default=5,type=int)
parser.add_argument("-p", "--page", help="Number of pages, default=1",default=1,type=int)
parser.add_argument("-o", "--output", help="output to file name")
args = parser.parse_args()

dorks_file = args.dorks
threads = args.threads
page = args.page
threads = args.threads
query = args.query
output = args.output
subs = args.subs 


dorks_list = []


if args.target or query:
    domain = args.target
else :
    raise SystemExit(colored("domain name is required","red",attrs=['bold'])  )

if dorks_file and args.target: 
    f = open(dorks_file, 'r')
    for line in f:
        dorks_list.append(f"{args.target} "+line.strip())
elif query:
    dorks_list.append(query)

elif subs and args.target :
    domain = args.target
    dork1 =  f'site:*.{domain} -www'
    dork2 = f'site:*.*.{domain}'
    dorks_list.append(dork1)
    dorks_list.append(dork2)

else:
    raise SystemExit(colored("dorks file or your query is required ","red",attrs=['bold'])  )  


def filter_subs(links):
    domains = []
    for link in links :
        split_site = link.strip().split('/')
        if len(split_site) > 1:
            domain = split_site[2]
            domains.append(domain)                    
    return set(domains)
         
def startpage(word,page):
    links = []
    headers={"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"}
    for page_number in range(1,page+1):
        try:
            req = requests.get(f'https://www.startpage.com/do/search?q={word}&segment=startpage.brave&page={page_number}',headers=headers).text
            if "<title></title>" in req:
                break
            else :   
                reg = re.findall('''(?:class="w-gl__result-url result-link"
                            href=")(.*?)"''',req)
                if not reg:
                    break
                for link in reg:   
                    links.append(link)                             
        except Exception as e:
            print(e)
    return links 

def main(dork): 
    dork_encode = quote(dork)
    searcher = startpage(dork_encode ,page)
    if subs :
        domains = filter_subs(searcher)
        for domain in domains :
            print(domain)
            if output :
                save_txt(domain,output)
            
    elif searcher :
        if args.silent :
            for link in searcher:
                prin(link)   
        else:
            print("\n["+colored("*","red",attrs=['bold'])+"] Checking " + "[" +colored(dork,"magenta",attrs=['bold']) + "]" + colored(f" ({len(searcher)}) Results","cyan",attrs=['bold']))
            for link in searcher:           
                print("\t["+colored("+","green",attrs=['bold'])+"] "+ link) 
                if output :
                    if "csv" in output:
                        out = [link , dork]
                        save_csv(out,output)
                    else:
                        out = link +" , "+dork    
                        save_txt(out,output)
    else:
        if not args.silent :
            print("["+colored("*","red",attrs=['bold'])+"] Checking " + "[" + colored(dork,"magenta",attrs=['bold']) +"] ["+ colored("-","yellow",attrs=['bold'])+"] "+ colored("No Results","yellow",attrs=['bold']))         

def save_csv(out,output):
    with open(output, "a") as csvfile:
        r = csv.writer(csvfile)
        r.writerow(out)

def save_txt(out,output):
    with open(output,'a') as txt:
        txt.write(str(out)+"\n")

if __name__ == "__main__" :
    if not args.silent :
        logo()
    pool = Pool(threads)
    pool.map(main,dorks_list)
    pool.close()
    pool.join()
    if output :
        print(colored(f"\nAll Results Saved In {output} file","green",attrs=['bold']) )          


