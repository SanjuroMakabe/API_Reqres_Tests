import requests
import logging
LOGGER = logging.getLogger(__name__)

#проверяем код ответа HTTP
def test_status_200_for_reqres_in():
	response = requests.get('https://reqres.in/api/users/2')
	assert response.status_code == 200
	LOGGER.info('***УСПЕХ: код ответа - 200!***')
    
#проверяем наличие имени на странице, извлекая его из 'data'
def test_name_Janet_for_reqres_in():
	response = requests.get('https://reqres.in/api/users/2')
	response_body = response.json()
	assert response_body['data']['first_name'] == 'Janet'
	LOGGER.info('***УСПЕХ: имя Janet найдено на странице!***')