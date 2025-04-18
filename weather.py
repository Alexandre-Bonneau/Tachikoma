# weather.py

from meteofrance_api import MeteoFranceClient
import datetime

client_meteo = MeteoFranceClient()

def meteo(ville: str) -> str:
    try:
        place = client_meteo.search_places(ville)[0]
        forecast = client_meteo.get_forecast_for_place(place)
        today = forecast.daily_forecast[0]

        min_temp = today["T"]["min"]
        max_temp = today["T"]["max"]
        precip = today["precipitation"].get("24h", 0)
        desc = today["weather12H"]["desc"]
        sunrise = datetime.datetime.fromtimestamp(today["sun"]["rise"]).strftime('%H:%M')
        sunset = datetime.datetime.fromtimestamp(today["sun"]["set"]).strftime('%H:%M')

        return (
            f"📍 Météo à {place.name} aujourd’hui :\n"
            f"🌡️ {min_temp}°C → {max_temp}°C\n"
            f"🌧️ Précipitations : {precip} mm\n"
            f"📝 Conditions : {desc}\n"
            f"☀️ Lever : {sunrise} | 🌇 Coucher : {sunset}"
        )
    except Exception as e:
        return f"⚠️ Erreur météo ({ville}) : {e}"

def wind_direction(deg):
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SO', 'O', 'NO']
    emojis = ['⬆️', '↗️', '➡️', '↘️', '⬇️', '↙️', '⬅️', '↖️']
    ix = round(deg / 45) % 8
    return f"{emojis[ix]} {directions[ix]}"


def pluie(ville: str) -> str:
    try:
        place = client_meteo.search_places(ville)[0]
        forecast = client_meteo.get_forecast_for_place(place)
        today = datetime.date.today()

        result = [f"🌧️ Pluie prévue à {place.name} aujourd’hui :"]
        for h in forecast.forecast:
            time = datetime.datetime.fromtimestamp(h["dt"])
            if time.date() != today:
                continue
            pluie_dic = h.get("rain", {})
            pluie_keys = list(pluie_dic.keys())[0]
            pluie_mm=pluie_dic.get(pluie_keys,-1)
            desc = h.get("weather", {}).get("desc", "")

            # Emoji selon la quantité de pluie
            if pluie_mm == 0:
                emoji = "☀️"
            elif pluie_mm < 1:
                emoji = "🌤️"
            elif pluie_mm < 3:
                emoji = "🌦️"
            elif pluie_mm < 6:
                emoji = "🌧️"
            elif pluie_mm < 15:
                emoji = "🌧️🌧️"
            else:
                emoji = "🌩️🌧️🌊"

            result.append(
                f"{time.strftime('%H:%M')} - {emoji} {pluie_mm:.1f} mm   - {desc}"
            )

        return "\n".join(result[:20]) if len(result) > 1 else "Pas de pluie prévue aujourd’hui."
    except Exception as e:
        return f"⚠️ Erreur pluie ({ville}) : {e}"

def vent(ville: str) -> str:
    try:
        place = client_meteo.search_places(ville)[0]
        forecast = client_meteo.get_forecast_for_place(place)
        today = datetime.date.today()

        result = [f"💨 Vent prévu à {place.name} aujourd’hui :"]
        for h in forecast.forecast:
            time = datetime.datetime.fromtimestamp(h["dt"])
            if time.date() != today:
                continue

            wind = h.get("wind", {})
            speed = wind.get("speed", -1)
            gust = wind.get("gust", -1)
            direction = wind_direction(wind.get("direction", 0))

            result.append(f"{time.strftime('%H:%M')} - 💨 {speed:.0f} km/h {direction}, rafales {gust:.0f} km/h")

        return "\n".join(result[:20]) if result else "Pas de données de vent pour aujourd’hui."
    except Exception as e:
        return f"⚠️ Erreur vent ({ville}) : {e}"





