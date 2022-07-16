<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestiondawd
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.

![screenshot](https://user-images.githubusercontent.com/71042858/166175994-440cdf76-b214-4bf4-a853-7012868f80dc.png)

<!-- ABOUT THE PROJECT -->
# Sobre el proyecto

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/raztorr/sideam">
    <img src="https://user-images.githubusercontent.com/71042858/166176005-45116dd0-2ade-4dbc-af5f-6ce8afb2fcb5.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">SIDEAM</h3>

  <p align="center">
    Reconocimiento de armas en tiempo real
    <br />
    <a href="https://github.com/Raztorr/SIDEAM/wiki"><strong>Explorar la Wiki »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Raztorr/SIDEAM-launch">Revisa el script de inicio rapido</a>
    ·
    <a href="https://github.com/Raztorr/SIDEAM/wiki/Blog">Revisa nuestro Blog</a>
    ·
    <a href="https://github.com/Raztorr/SIDEAM/issues">Reporta un error</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>INDICE</summary>
  <ol>
    <li>
      <a href="#Sobre el proyecto">Sobre el proyecto</a>
      <ul>
        <li><a href="#Como funciona el proyecto">Como funciona el proyecto</a></li>
      </ul>
    </li>
    <li>
      <a href="#Empezando">Empezando</a>
      <ul>
        <li><a href="#Objetos necesarios">Objetos necesarios</a></li>
        <li><a href="#Instalacion">Instalacion</a></li>
      </ul>
    </li>
    <li><a href="#Pasos a seguir que se hicieron">Pasos a seguir que se hicieron</a></li>
    <li><a href="#Contacto">Contacto</a></li>
  </ol>
</details>


<!-- Sobre el proyecto -->
## Sobre el proyecto

[![Product Name Screen Shot][product-screenshot]](https://github.com/raztorr/sideam)

Sideam es un software de reconocimiento de armas (actualmente en esta versión 1.0 solo de pistolas) que se apoya del uso de una raspberry pi (con cámara) y un servidor que procese la imagen de preferencia con una tarjeta grafica buena.

### Porque crear esto

Esto puede servir para la seguridad en general ya que en caso de alguien quiera ocupar un arma en un lugar donde no esten permitidas Sideam podría llamar a las autoridades pertinentes o mandarle una notificación al usuario de sideam.

Actualmente sabemos que estados unidos están sufriendo una crisis con las armas de fuego debido a que los estudiantes de estos establecimientos usan estas para quitarles la vida a sus compañeros haciendo masacres de menores de edad, esto sucede por muchos factores, pero Sideam puede ayudar a detectar el uso del arma y mandar una notificación a las autoridades para tratar de minimizar la cantidad de muertes totales, y Sideam no solo se puede aplicar para estos casos si no que se puede aplicar a otros países e instituciones donde tener un arma de fuego sea malo para las personas del lugar.


<p align="right">(<a href="#top">back to top</a>)</p>



### Como Funciona el proyecto

Fue creado con una camara que esta conectada a una raspberry pi, esta camara manda el video a un computador externo(con preferencia una tarjeta grafica dedicada) que funciona de servidor para procesar el video de la raspberry con la inteligencia artificial esta detecta si en el video existe alguna pistola y se muestra en la pantalla un cuadro donde se muestra la ubicacion de la pistola.

El proyecto fue creado en su mayoria con Yolov 5(Un proyecto de Github) y una base de datos con fotos de pistolas para entrenar la I.A.

* [Yolov5](https://github.com/ultralytics/yolov5)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- Empezando -->
## Empezando

Se conecta el video producido de la raspberry a un servidor externo para que procese el video con la inteligencia artificial para que detecte el arma de fuego

### Objetos necesarios

- Una rasoberry pi
- Un servidor con una tarjeta grafica dedicada
- Alguna forma para conectarse(Mediante internet o por cable)

### Instalacion

NO se como se instalaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa supomgo que se descarga descarga toda la wea pero no lo se aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Pasos a seguir que se hicieron -->
## Pasos a seguir que se hicieron

- [x] Poner en funcionamiento la raspberry
- [x] Conseguir una base de datos con fotos de armas 
- [x] Entrenar a la inteligencia artificial
- [x] Conectar el servidor con la raspberry
- [x] Conectar el servidor con la inteligencia artificial
- [x] Probar el proyecto con una pistola o imitacion para saber que funciona
- [x] Terminar el github

<p align="right">(<a href="#top">back to top</a>)</p>





<!-- Contacto -->
## Contacto

Link del proyecto: [](https://github.com/Raztorr/SIDEAM)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/raztorr/sideam.svg?style=for-the-badge
[contributors-url]: https://github.com/raztorr/sideam/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/raztorr/sideam.svg?style=for-the-badge
[forks-url]: https://github.com/raztorr/sideam/network/members
[stars-shield]: https://img.shields.io/github/stars/raztorr/sideam.svg?style=for-the-badge
[stars-url]: https://github.com/raztorr/sideam/stargazers
[issues-shield]: https://img.shields.io/github/issues/raztorr/sideam.svg?style=for-the-badge
[issues-url]: https://github.com/raztorr/sideam/issues
[license-shield]: https://img.shields.io/github/license/raztorr/sideam.svg?style=for-the-badge
[license-url]: https://github.com/raztorr/sideam/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/raztorr
[product-screenshot]: https://user-images.githubusercontent.com/71042858/166176326-05f4b664-0eea-4099-b248-317622d4dc8f.png

