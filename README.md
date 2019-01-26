# vk_streaming
Простой интрумент для сбора данных для научных и маркетинговых исследований через VK Streaming API

[![GitHub last commit](https://img.shields.io/github/last-commit/marinskiy/vk_streaming.svg)](https://github.com/marinskiy/vk_streaming) 
[![GitHub commit activity the past week, 4 weeks, year](https://img.shields.io/github/commit-activity/y/marinskiy/vk_streaming.svg)](https://github.com/marinskiy/vk_streaming)
[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/marinskiy/vk_streaming.svg)](https://github.com/marinskiy/vk_streaming) 
[![GitHub stars](https://img.shields.io/github/stars/marinskiy/vk_streaming.svg)](https://github.com/marinskiy/vk_streaming)

## Получение сервисного ключа для доступа к API

Для получения сервисного ключа доступа нужно:
1) перейти на https://vk.com/dev 
2) создать новое Standalone-приложение
3) перейти в раздел "Настройки" и скопировать оттуда сервисный ключ

## Установка правил
Правила задаются в файле rules_list.txt. Каждая строчка - отдельное правило

## Запуск сбора данных
Для запуска сбора данных нужно вставить свой сервисный ключ в соответствующую строчку main.py и запустить файл
