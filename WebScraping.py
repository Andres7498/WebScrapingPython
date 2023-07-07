#importar librerias necesarias
from bs4 import BeautifulSoup
import requests
import csv

#Extraer la pagina web del sitio y asignarlo en formato de texto
websites = ['https://www.gerflor.es/professionals-products/Pavimento/mipolam-planet.html',
            'https://www.gerflor.es/professionals-products/Pavimento/mipolam-bio-planet.html',
            'https://www.gerflor.es/professionals-products/Pavimento/mipolam-affinity.html',
            'https://www.gerflor.es/professionals-products/Pavimento/mipolam-classic-1-5-mm.html',
            'https://www.gerflor.es/professionals-products/Pavimento/mipolam-classic-2-mm.html',
            'https://www.gerflor.es/professionals-products/Pavimento/mipolam-symbioz.html',
            'https://www.gerflor.es/professionals-products/Pavimento/mipolam-accord.html',
            'https://www.gerflor.es/professionals-products/Pavimento/mipolam-cosmo.html',
            'https://www.gerflor.es/professionals-products/Pavimento/mipolam-elegance.html',
            'https://www.gerflor.es/professionals-products/Pavimento/mipolam-troplan.html',
            #2
            'https://www.gerflor.es/professionals-products/Pavimento/taralay-impression-acoustic.html',
            'https://www.gerflor.es/professionals-products/Pavimento/taralay-impression-hop-acoustic.html',
            'https://www.gerflor.es/professionals-products/Pavimento/nerok-70-acoustic.html',
            'https://www.gerflor.es/professionals-products/Pavimento/nerok-55-acoustic.html',
            'https://www.gerflor.es/professionals-products/Pavimento/taralay-premium-comfort.html',
            'https://www.gerflor.es/professionals-products/Pavimento/taralay-initial-comfort.html',
            'https://www.gerflor.es/professionals-products/Pavimento/libertex-2020.html',
            #3
            'https://www.gerflor.es/professionals-products/Pavimento/nerok-55-compact.html',
            'https://www.gerflor.es/professionals-products/Pavimento/taralay-impression-compact.html',
            'https://www.gerflor.es/professionals-products/Pavimento/nerok-70-compact.html',
            'https://www.gerflor.es/professionals-products/Pavimento/taralay-premium-compact.html',
            'https://www.gerflor.es/professionals-products/Pavimento/taralay-initial-compact.html',
            #4
            'https://www.gerflor.es/professionals-products/Pavimento/creation-70.html',
            'https://www.gerflor.es/professionals-products/Pavimento/creation-70-connect.html',
            'https://www.gerflor.es/professionals-products/Pavimento/creation-70-clic.html',
            'https://www.gerflor.es/professionals-products/Pavimento/creation-70-looselay.html',
            'https://www.gerflor.es/professionals-products/Pavimento/saga2.html',
            #5
            'https://www.gerflor.es/professionals-products/Pavimento/creation-55.html',
            'https://www.gerflor.es/professionals-products/Pavimento/creation-55-solid-clic.html',
            'https://www.gerflor.es/professionals-products/Pavimento/creation-55-looselay.html',
            'https://www.gerflor.es/professionals-products/Pavimento/creation-55-looselay-acoustic.html',
            'https://www.gerflor.es/professionals-products/Pavimento/creation-55-rigid-acoustic.html',
            #6
            'https://www.gerflor.es/professionals-products/Pavimento/creation-40.html',
            'https://www.gerflor.es/professionals-products/Pavimento/creation-40-solid-clic.html',
            'https://www.gerflor.es/professionals-products/Pavimento/creation-40-rigid-acoustic.html',
            #7
            'https://www.gerflor.es/professionals-products/Pavimento/creation-30.html',
            'https://www.gerflor.es/professionals-products/Pavimento/creation-30-solid-clic.html']
    
for i in range(len(websites)):
    result = requests.get(websites[i])
    content = result.text

    #imprimer el HTML de la pagina web para poder buscar lo valores
    soup = BeautifulSoup(content, 'lxml')
    #Examinando los tags de la pagina
    #print([tag.name for tag in soup.find_all()])

    #Mostrar la pagina lo mas clara posible
    #print(soup.prettify())

    #NOMBRE PRODUCTO                            <h1 class="title">Mipolam Planet</h1>
    #IMAGEN                                     <img class="image tns-lazy-img loaded tns-complete" data-object-fit="cover" src="https://www.gerflor.es/cache/media/gerflor-slider-planet/cr,1134,598-6ff68f.jpg" data-src="https://www.gerflor.es/cache/media/gerflor-slider-planet/cr,1134,598-6ff68f.jpg" alt="">
    #DESCRIPCION                                <p class="slogan">
    '''COLORES POSIBLES Y NUMERO DE REFERENCIA <a id="ajoutpanier" class="shopping-cart-hover js-add-sample-to-cart" data-prod-id="400192083" data-prod-title="Mipolam Planet" data-colo-code="5402" data-colo-title="Ivory Dust" data-code-echantillon="ZC125402">
                        <svg height="25" width="25">
                            <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="static/apps/gerflor_template/src/img/sprites.svg#icon-shopping"></use>
                        </svg>
                    </a>
                    
                    <div class="title"> 5402 Ivory Dust </div>
                    '''
    title = soup.find('h1',  class_='title').get_text()
    description = soup.find('p',  class_='slogan').get_text()
    image = soup.find('img',  class_='image').attrs['data-src']
    firstcolor = soup.find('div',  class_="card-product").attrs['data-colo-title']
    data = [title,description,image,firstcolor]

    with open('Scraping.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)
        file.close()
    i=i+1