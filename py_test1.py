import requests
import logging
LOGGER = logging.getLogger(__name__)

#пытаемся получить статус код 201
def test_status_200_for_reqres_in():
	response = requests.get('https://reqres.in/api/users/2')
	assert response.status_code == 201
	LOGGER.info('***УСПЕХ: код ответа - 200!***')
    
#пытаемся найти имя 'Jean'
def test_name_Janet_for_reqres_in():
	response = requests.get('https://reqres.in/api/users/2')
	response_body = response.json()
	assert response_body['data']['first_name'] == 'Jean'
	LOGGER.info('***УСПЕХ: имя Janet найдено на странице!***')