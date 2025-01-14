<div align="center">
    <a href="https://github.com/hurfy/rf4-api"><img src="https://github.com/user-attachments/assets/c1890100-fb8b-4ac4-a28d-5b097eb536b9" alt="rf4-api" /></a>
</div>

<div align="center">
    <img src="https://img.shields.io/github/issues/hurfy/rf4-api?style=for-the-badge" alt="open issues" />
    <img src="https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge" alt="version" /></a>
    <a href="LICENSE"><img src="https://img.shields.io/github/license/hurfy/rf4-api?style=for-the-badge" alt="license" /></a>
</div>

<br />

<div align="center">
  Unofficial catch API for Russian Fishing 4
</div>

<div align="center">
  <sub>
    Built with love 
    &bull; Brought to you by <a href="https://github.com/hurfy">@hurfy</a>
    and other <a href="https://github.com/hurfy/rf4-api/graphs/contributors">contributors</a>
  </sub>
</div>

## Introduction
**This project is still in development!**<br><br>
The main objective of this project is the periodic collection of data regarding records, ratings, and winners from the official Russian Fishing 4 website, followed by processing and presenting it in a convenient format. The parsing covers all regions, including various rod types and other classifications for each table.

Currently, only one language is supported. The frequency of parsing can be configured for each table.

*I do not own the data but collect it to present in a convenient and accessible format. All rights are reserved by FishSoft LLC.*

## Quick Start
Doesn't carry the full CI/CD pipelines yet.<br>So, just run this:
```shell
# Django
python manage.py runserver
```
```shell
# Celery
celery -A worker.app worker -l INFO -c 1 -P solo
```
*Only development mode is available atm!*
