# Prodigy_SD
A collection of Python-based projects completed during my internship at Prodigy Infotech, including a temperature converter, number guessing game, contact manager, and a web scraper for extracting e-commerce data into CSV format.
📂 Prodigy Infotech Internship Tasks (Python)
This repository includes Python-based GUI and scripting projects completed during my internship with Prodigy Infotech. Each task is aimed at strengthening problem-solving and software development skills through hands-on experience.

🔥 Task 1: Temperature Converter GUI
Overview:
A graphical user interface (GUI) application built using tkinter to convert temperatures between Celsius, Fahrenheit, and Kelvin.

Features:

Simple and intuitive GUI layout.

Supports three units with auto-conversion.

Input validation using try-except.

Real-time result display on label.

Modules Used: tkinter, ttk, messagebox
UI Highlights: ComboBox for unit selection, colored result output.

🎯 Task 2: Number Guessing Game
Overview:
A fun interactive number guessing game built with tkinter. The program generates a random number between 1 and 1000, and the player tries to guess it.

Features:

Dynamic hinting: “Too high”, “Too low”, or “Almost there”.

Smart difference-based hints if the guess is far off.

Automatic game reset on correct guess.

Attempt counter with popup on win.

Modules Used: tkinter, random, messagebox
UI Highlights: Bright yellow background for visual appeal.

📇 Task 3: Contact Management System (Excel-backed)
Overview:
A console-based contact manager where users can add, view, and delete contact entries. All records are stored in an Excel file for persistence.

Features:

Add first record or multiple records.

Display all saved contacts in a tabular format.

Delete specific contacts using their phone number.

Data stored in an .xlsx file using pandas.

Modules Used: pandas, os
File Used: contact management system.xlsx

🌐 Task 4: Web Scraper with CSS Selectors (Selenium + Requests)
Overview:
A flexible command-line based scraper that allows users to input a URL and specify multiple CSS selectors to extract content. Great for e-commerce, education, and data listing sites.

Features:

Detects bot protection or CAPTCHA using HTTP headers and content checks.

Supports scraping multiple fields simultaneously.

Uses Selenium to load dynamic JavaScript pages.

Results are combined and saved as a CSV file.

Supports scraping structured data like product details, countries, population, etc.

Modules Used: selenium, requests, csv, os, time, webdriver_manager
Tech Used: Headless Chrome browser

Example Use Cases:

Scraping laptops from: https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops

Scraping country data from: https://www.scrapethissite.com/pages/simple/
