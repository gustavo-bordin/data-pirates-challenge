
BOT_NAME = 'dataPirates'

SPIDER_MODULES = ['dataPirates.spiders']
NEWSPIDER_MODULE = 'dataPirates.spiders'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 5

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'www.buscacep.correios.com.br',
    'Origin': 'http://www.buscacep.correios.com.br',
    'Referer': 'http://www.buscacep.correios.com.br/sistemas/buscacep/ResultadoBuscaFaixaCEP.cfm',
    'Upgrade-Insecure-Requests': 1,
}

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 10

ITEM_PIPELINES = {
    'dataPirates.pipelines.Duplicates': 0,
    'dataPirates.pipelines.WhitespacesRemover': 1,
    'dataPirates.pipelines.JsonlWriter': 2,
}

PROXY_POOL_ENABLED = True
