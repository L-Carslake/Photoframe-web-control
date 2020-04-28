<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the Photoframe-web-control and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** L-Carslake, Photoframe-web-control, twitter_handle, email
-->





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->



<!-- PROJECT LOGO -->
<!--
<br />
<p align="center">
  <a href="https://github.com/L-Carslake/Photoframe-web-control">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
-->

  <h3 align="center">Photoframe: Web interface and API</h3>

  <p align="center">
    A python web interface and API for controlling a digital photoframe. Using <a href="https://flask.palletsprojects.com/en/1.1.x/quickstart/"> Flask </a> and <a href="https://pypi.org/project/PyUserInput/"> PyUserInput</a>.
    <!--
    <br />
    <a href="https://github.com/L-Carslake/Photoframe-web-control"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/L-Carslake/Photoframe-web-control">View Demo</a>
    ·
    <a href="https://github.com/L-Carslake/Photoframe-web-control/issues">Photoframe-web-control Bug</a>
    ·
    <a href="https://github.com/L-Carslake/Photoframe-web-control/issues">Request Feature</a>
    -->
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project
An addition for the digital photoframe project; based on a [feh](https://feh.finalrewind.org) slideshow. Providing control for next/previous image and viewing the current image.
Implemented as a web page, and REST API.  


### Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
* [PyUserInput](https://pypi.org/project/PyUserInput/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites
1. Install the required python packages
```sh
pip3 install flask pyuserinput
```
2. Start a feh slideshow with the required action
```sh
feh --slideshow-delay 600 --action ";echo %f > /Images/currentImage.txt" /Images  
```

### Installation
 
1. Clone the Photoframe-web-control repo
```sh
git clone https://github.com/L-Carslake/Photoframe-web-control.git
```
2. Start the Flask server
```sh
/usr/bin/python3 -u -m flask run --host=0.0.0.0
```


<!-- USAGE EXAMPLES -->
## Usage

With the server running you can access the link printed by the script or http://YOUR-IP:5000. 

<!-- Theory of Operation -->
## Theory of Operation

### Feh Slideshow
Feh is a basic image viewer. This project sends keyboard shortcuts to feh controlling the slideshow.
[Documentation of the keyboard shortcuts](https://man.finalrewind.org/1/feh/#keys).

The image that is currently being viewed is written to a file for reading by the python script. Feh implements this as an  action, controlled as a command line argument:
```sh
 --action ";echo %f > /Images/currentImage.txt"
```
When called the current image name is written to the "/Images/currentImage.txt" file.

### Flask server
 - Webpage with functions
 
### REST API
 - Homeassistant
 - Volumio API
 - URLS


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/L-Carslake/Photoframe-web-control/issues) for a list of proposed features (and known issues).


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
