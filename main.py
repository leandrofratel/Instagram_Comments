from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import choice, randint

class InstagramBot():
    def __init__(self, username, password):
        """Inicialização dos atributos."""
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path=r'chromedriver.exe')

    def login(self):
        """Inicia o Chrome."""
        driver = self.driver
        driver.get('https://www.instagram.com')
        sleep(2)

        # Identifica o user_name, limpa o campo e preenche com o nome de usuário.
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        sleep(1)
        user_element.send_keys(self.username)

        # Identifica o campo senha, limpa e preenche com a senha.
        pass_element = driver.find_element_by_xpath("//input[@name='password']")
        pass_element.clear()
        sleep(1)
        pass_element.send_keys(self.password)
        pass_element.send_keys(Keys.RETURN)
        sleep(7)

        # Encontra a foto salva e comenta.
        self.localizar()

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Este código irá basicamente permitir que você 
        simule a digitação como uma pessoa """
        for letter in sentence:
            single_input_field.send_keys(letter)
            sleep(randint(1, 5) / 30)

    def localizar(self):
        driver = self.driver
        driver.get('https://www.instagram.com/fratel.l/saved/?hl=pt-br')
        sleep(3)

        # Clica na primeira foto.
        pic = driver.find_element_by_class_name("_9AhH0")
        pic.click()
        sleep(3)

        # Lista de Comentários.
        while True:
            
            """Troque essa lista por uma lista de comentários ou perfis
            para serem comentados na foto.
            """
            users_or_comment = [
                '@exemplo ' '@exemplo',
                '@exemplo ' '@exemplo',
                '@exemplo ' '@exemplo',
                '@exemplo ' '@exemplo',
                '@exemplo ' '@exemplo',
                '@exemplo ' '@exemplo',
                '@exemplo ' '@exemplo',
                '@exemplo ' '@exemplo',
                '@exemplo ' '@exemplo',
                '@exemplo ' '@exemplo',
                '@exemplo ' '@exemplo',
                '@exemplo ' '@exemplo',
                '@exemplo ' '@exemplo',
                '@exemplo ' '@exemplo'
            ]

            # Identifica o campo de comentários.
            driver.find_element_by_class_name("Ypffh")
            driver.find_element_by_class_name("Ypffh").click()
            comment_input_box = driver.find_element_by_class_name("Ypffh")

            # Insere o comentário.
            for user in users_or_comment:

                self.type_like_a_person(user, comment_input_box)
                sleep(randint(5, 10))
            
                # Publica.
                driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
                sleep(10)


insta = InstagramBot('[seu usuario]', '[sua senha]')
insta.login()
