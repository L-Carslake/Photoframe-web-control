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



<!-- PROJECT INTRO -->


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


<!-- TABLE OF CONTENTS -->

## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Theory of Operation](#theory-of-operation)
* [License](#license)
* [Roadmap](#roadmap)
* 



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
Feh is a basic image viewer. Controlled using keyboard shortcuts, which are sent from this python script using the PyUserInput library. [Documentation of  feh keyboard shortcuts](https://man.finalrewind.org/1/feh/#keys). Implemented are, next, previous, and action0.ln

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

