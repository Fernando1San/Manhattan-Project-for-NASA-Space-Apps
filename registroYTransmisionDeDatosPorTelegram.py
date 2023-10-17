import pandas as pd
import telebot
from datetime import datetime, timedelta
import time
import schedule
from geopy.geocoders import Nominatim

def main():
  
  fecha_actual = datetime.now()

  fecha_menos_un_dia = fecha_actual - timedelta(days=1)

  FECHA = fecha_actual.strftime("%Y-%m-%d")
  
  print(FECHA)
  
  def encontrar_ciudad_cercana(latitud, longitud):
    geolocator = Nominatim(user_agent="mi_app")
    ubicacion = geolocator.reverse((latitud, longitud))
    return ubicacion.address
  
  MAP_KEY = '724791d412a82892de4d71d974d5e727'

  CHAT_ID="@SpaceAppsFireAlarm" #ID del chat

  TOKEN = "6572209256:AAHG_HN9EbMMstm78xZysh0QzBwJzQfBGQ8" #token de la API de telegram

  bot = telebot.TeleBot(TOKEN)

  def enviarMensaje(mensaje):
      bot.send_message(CHAT_ID, mensaje) 

  #We get the data from the
  mex_url = 'https://firms.modaps.eosdis.nasa.gov/api/country/csv/' + MAP_KEY + '/VIIRS_SNPP_NRT/MEX/1/' + FECHA
  mex_data = pd.read_csv(mex_url)
  #print(mex_data)
  print('Number of Possible fires: ', len(mex_data))

  #Filtred data
  filtred_mex_data = mex_data[(mex_data['confidence'] == 'n') | (mex_data['confidence'] == 'h')]
  filtred_mex_data = filtred_mex_data[filtred_mex_data['frp'] > 5]
  #This would be the fires
  #print('Mexico subset contains', len(filtred_mex_data), 'fires.')

  #here I print and get the latitudes and longitudes
  coordenadas = [(row['latitude'], row['longitude']) for index, row in filtred_mex_data.iterrows()]

  #here I print my latitudes and longitudes to check
  puntero = 0
  while puntero < len(coordenadas):
      latitud, longitud = coordenadas[puntero]
      #print(f'Latitud: {latitud}, Longitud: {longitud}')
      puntero += 1

  #How many fires I have in the zone
  #print(f"Longitud del vector: {len(coordenadas)}")
  print(f"How many real fires are there: {puntero}")

  filtred_mex_data['acq_time'] = filtred_mex_data['acq_time'].astype(str).str.zfill(4)
  # Extrae las horas y minutos y crea una columna acq_datetime solo con la hora en formato 'H:M'
  filtred_mex_data['acq_datetime'] = pd.to_datetime(filtred_mex_data['acq_time'], format='%H%M').dt.strftime('%H:%M')
  # Extrae las horas en el formato 'H:M' y guárdalas en un vector
  horas = filtred_mex_data['acq_datetime']
  #print(horas.tolist())

  puntero = 0
  while puntero < len(coordenadas):
      latitud, longitud = coordenadas[puntero]
      ciudad= encontrar_ciudad_cercana(latitud, longitud)
      horas_actual=horas.iloc[puntero]
      mensaje = f'*¡¡ALERTA DE INCENDIO!!* Se ha detectado un posible incendio cerca de la siguiente localidad/ciudad: {ciudad}. La hora del sinsiestro registrado es {horas_actual}'
      enviarMensaje(mensaje)
      puntero += 1

if __name__ == "__main__":

  main()
  
  schedule.every(30).minutes.do(main)

  # Ejecuta el programa de forma indefinida
  while True:
    schedule.run_pending()
    time.sleep(1)
