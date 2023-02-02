﻿## Stack utilizada
**Back-end:** Python3.8, FastAPI, Uvicorn

##  Rodando localmente
```bash
docker-compose up --build
```

## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

`spotify_client_id`

`spotify_client_secret`

`spotify_url`

`spotify_url_token`

`open_weather_maps_weather_url`

`open_weather_maps_weather_id`

## Rotas

```http
  POST /music

  lat: float
  lon: float
  city: string

```
```http
  ex: http://0.0.0.0:8000/music
  body = {
    "city": "são paulo"
  }
```
```http
  ex: http://0.0.0.0:8000/music
  body = {
    "lat": -27.670094797245927
    "lon": -48.73918829600568
  }
```


