# Geocubes Finland - QGIS plugin
A QGIS plugin to access raster data on GeoCubes Finland, maintained by Finnish Geospatial Research Institute (FGI).

[Esittely suomeksi alla](https://github.com/tleppamaki/Geocubes-Finland-QGIS-plugin#mik%C3%A4-on-geocubes-finland)

## What is Geocubes Finland?
Geocubes Finland is a harmonised, multi-resolution raster geodata repository. The repository contains several key national datasets on themes such as elevation, land cover and forestry. Read more: [Geocubes Finland main site](http://86.50.168.160/geocubes) and [description on usage and citing](https://github.com/geoportti/GeoCubes).
#### Harmonised? What does that mean?
Simply that the data is as simple to access and use as can be. All of the data is in the same CRS (EPSG:3067), is georeferenced uniformly and is available as both a GeoTIFF image or a [VRT virtual file](https://gdal.org/drivers/raster/vrt.html). The data is available in resolutions ranging from 1 to 1000 meters and can be cropped flexibly with e.g. a bounding box or administrative area boundaries. Read more [here](http://86.50.168.160/geocubes/description/).
All of this means that **accessing raster datasets is easier than ever before**.
#### Who's the service for?
Geocubes Finland is aimed to support the needs of Finnish research community, but the service and its data is freely usable by anyone interested. Please see the [citing guidelines](https://github.com/geoportti/GeoCubes#usage-and-citing) if you use Geocubes Finland in your work.

## Geocubes Finland plugin
This QGIS 3.x plugin enables using all of the abovementioned features effortlessly in your QGIS 3 installation. Simply select three parameters: raster layers to download, cropping method and raster resolution. Crop with a bounding box, administrative areas or draw a polygon to crop with. Then select either GeoTIFF or VRT file. After download, a layer is added to QGIS, where you can use it for further analysis. You may use files from the Geocubes Finland server or save files to local storage: the former suits quick analysis on smaller rasters and the latter is beneficial for larger files.
#### Plugin installation
- Download the plugin to your computer from *Clone or download* -> *Download ZIP*
- Open QGIS, click *Plugins* drop-down menu and select *Manage and install plugins*
- Select *Install from ZIP* in the plugin manager. Navigate to the zip file.
#### I found a bug and/or want to suggest a new feature. What do I do now?
We are grateful for all feedback. If you find errors or have suggestions to improve the plugin, please open an issue in the repository or see infobox on top of *geocubes_plugin.py* for email information.
#### Layers can't sometimes be added directly to QGIS – what to do?
On some envinroments, attempting to add Geocubes layers to QGIS will always fail. One known reason for this is a GDAL driver called [DODS](https://gdal.org/drivers/raster/dods.html). Disabling this driver will fix the problem. [See here for details](https://trac.osgeo.org/gdal/ticket/6682). The easiest way to disable it is via QGIS settings. **Select Settings -> Options -> GDAL. Scroll the list and you should find a driver named DODS. Deselect it and click Ok.** You may do the same via terminals as well. Type the command GDAL_SKIP=DODS preceded by either SET or EXPORT depending on the platform. Read more on configuration options [here](https://trac.osgeo.org/gdal/wiki/ConfigOptions). 

If this didn't fix the problem, see above what to do in case of a bug. The problem can also be circumvented by only saving layers to disk.

## Mikä on Geocubes Finland?
Geocubes Finland on Paikkatietokeskus FGI:n ylläpitämä harmonisoidun moniresoluutioisen rasterigeodatan tietovarasto. Se sisältää keskeisiä kansallisia aineistoja liittyen esimerkiksi korkeusmalliin, maanpeitteeseen ja metsätalouteen. Lisätietoa englanniksi [Geocubes Finlandin pääsivulta](http://86.50.168.160/geocubes) sekä [käytön ja siteeraamisen kuvauksesta](https://github.com/geoportti/GeoCubes).
#### Harmonisoitu? Mitäs se tarkoittaa?
Että data on mahdollisimman helppoa saavuttaa ja käyttää. Kaikki aineistot ovat samassa koordinaattijärjestelmässä (EPSG:3067), yhtenäisesti georeferöityjä ja ovat saatavilla samoissa tiedostomuodoissa (GeoTIFF ja [Virtuaalinen tiedosto VRT](https://gdal.org/drivers/raster/vrt.html)). Moniresoluutioisuus tarkoittaa, että aineistot ovat saatavilla 1–1000 metrin resoluutioilla – rastereita voi myös rajata joustavasti mm. rajaavalla suorakaiteella tai hallinnollisten alueiden rajoilla. Tarkempi [kuvaus englanniksi](http://86.50.168.160/geocubes/description/).
Edellämainittu tarkoittaa, että **rasteridata on helpommin saatavilla ja käytettävissä kuin kuunaan**.
#### Kenelle palvelu on suunnattu?
Geocubes Finland on suunnattu suomalaisen tutkijayhteisön tarpeisiin, mutta palvelu ja sen data ovat avoimesti käytettävissä. Katsothan [viittausohjeet](https://github.com/geoportti/GeoCubes#usage-and-citing), jos käytät Geocubes Finlandia työssäsi.

## Geocubes Finland QGIS-laajennus
Tällä QGIS 3.x -laajennuksella edellämainittujen ominaisuuksien käyttö sujuu vaivatta. Käyttäjän tarvitsee valita kolme keskeistä parametriä: ladattavat tasot, rajaus ja rasteriresoluutio. Rajauksen voi tehdä suorakulmiolla (*bounding box*), hallinnollisilla alueilla tai piirtää mieleisensä polygonin. Tiedostomuodoksi voi valita joko GeoTIFF- tai VRT-tiedoston. Taso lisätään latauksen jälkeen QGIS:iin jatkoanalyysiä varten. Tiedostoja voi käyttää joko Geocubesin palvelimilta tai tallentaa paikallisesti: ensimmäinen soveltuu pienempien tiedostojen nopeisiin analyyseihin ja jälkimmäinen on hyödyllinen suuremmissa tiedostoko'oissa.
#### Laajennuksen asentaminen
- Lataa laajennus zip-tiedostona repositorion yläkulmasta kohdasta *Clone or download* -> *Download ZIP*
- Avaa QGIS 3 -versiosi, klikkaa *Plugins*-valikko ja valitse *Manage and install plugins*
- Valitse vasemmalta *Install from ZIP* ja etsi äsken ladattu tiedosto
#### Löysin bugin ja/tai tahdon ehdottaa uutta ominaisuutta. Mitä teen?
Vastaanotamme palautetta hyvin mielellään. Jos löydät virheitä tai sinulla on kehitysehdotuksia, avaa keskustelu repositorion *Issues*-välilehdellä tai ota yhteyttä sähköpostitse *geocubes-plugin.py*-tiedoston yläosan laatikosta löytyvään osoitteeseen.
#### Tasoja ei toisinaan voi lisätä QGIS:iin. Mitä teen?
Joissain ympäristöissä tason lisääminen suoraan QGIS:iin epäonnistuu aina. Eräs tunnettu syy tälle on GDAL-ajuri nimeltään [DODS](https://gdal.org/drivers/raster/dods.html). Ajurin poistaminen käytöstä korjaa ongelman. [Lisätietoja täältä](https://trac.osgeo.org/gdal/ticket/6682). Helpoiten ajurin saa pois käytöstä QGIS:n asetusten kautta. **Valitse Settings -> Options -> GDAL. Selaa listaa DODS:n kohdalle, klikkaa pois käytöstä ja paina Ok.** Saman voi tehdä terminaalin kautta: käyttäjän tulee kirjoittaa oikeaan terminaaliin käsky GDAL_SKIP=DODS jota edeltää joko SET tai EXPORT alustasta riippuen. Lue [GDAL:n asetusten määrittämisestä](https://trac.osgeo.org/gdal/wiki/ConfigOptions).

Jos ongelma jatkuu, katso ylhäältä toimet bugeja kohdatessa. Ongelman voi myös sivuuttaa lataamalla tasot aina kovalevylle.
