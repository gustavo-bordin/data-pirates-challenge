# Data Pirates Challenge - Neoway 

## 📜 What this project uses?
  - Python3  `as language`
  - Scrapy  `as framework`
  - Docker `as tool`
  - Docker-compose `as tool`


___
<br>

## ❓ What do i need?
To run this crawler you gonna need:
  - 🐳 Docker <p style="opacity: 50%">v19.03.8+</p> https://www.docker.com/products/docker-desktop
  - 🐳 Docker-compose <p style="opacity: 50%">v1.25.4+</p> https://docs.docker.com/compose/install/


<br>

<p style="background: #dae3b3; color: black">P.S: If you are using windows or MacOs, your docker-compose already comes with the default installation. <p>

❔ What about Python3 and Scrapy?
Do not worry, docker will take care of their installation
<br>
<br>

### Check if they are installed correctly by typing:
```
$ docker-compose --version; docker --version
```
`The above code must output the version of each tool`
___

<br>
 

## 💻 Installation


#### 1. Clone this repo:
```
$ git clone https://github.com/gustavobordinho/data-pirates-challenge.git
```
#### 1.1. Enter in the generated folder:
```
$ cd data-pirates-challenge
```
#### 1.2. Switch to correios-crawler branch:
```
$ git checkout correios-crawler
```
#### 1.3. Build the container:
```
$ docker-compose build
```
#### 1.4. Run the container:
```
$ docker-compose up -d
```
#### 1.5. Start the crawler:
```
$ docker-compose exec crawler bash -c 'scrapy crawl correios'
```
___

<br>

Once the crawling is done, all the information will be inside `scrapy` folder as `.jsonl` files, separeted by UF.
